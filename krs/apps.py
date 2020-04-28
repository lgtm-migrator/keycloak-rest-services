"""
Managing applications ("clients") in Keycloak.

App structure:

1. Keycloak client
  - access type = confidential
    - can only get tokens through the app
  - roles:
    - can be tied to groups or individual users
  - scopes:
    - can be a list of other app scopes available
    - default available scopes:
      - "profile" - username, name, groups
      - "email" - email
      - "institution" - institution
2. Keycloak client scope
  - same name as client
  - when selected, puts the app roles into the token

Also available: a generic "public" app for public access to scopes,
if the application scope is allowed to be public.
"""
import requests

from .util import config, ConfigRequired
from .groups import list_groups, group_info

def list_apps(token=None):
    """
    List applications ("clients") in Keycloak.

    Returns:
        dict: app name: app info
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })
    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    clients = r.json()
    ret = {}
    for c in clients:
        if 'app' not in c['attributes'] or not c['attributes']['app']:
            continue
        ret[c['clientId']] = {k:c[k] for k in c if k in ('clientId','defaultClientScopes','id','optionalClientScopes','rootUrl','serviceAccountsEnabled')}
    return ret

def app_info(appname, token=None):
    """
    Get application ("client") information.

    Args:
        appname (str): app name ("clientID")

    Returns:
        dict: app info
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients?clientId={appname}'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    ret = r.json()

    if not ret:
        raise Exception(f'app "{appname}" does not exist')
    data = ret[0]

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{data["id"]}/client-secret'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    ret = r.json()
    data['clientSecret'] = ret['value']

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{data["id"]}/roles'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    ret = r.json()
    data['roles'] = [r['name'] for r in ret]

    return data

def list_scopes(only_apps=True, mappers=False, token=None):
    """
    List scopes in Keycloak.

    Args:
        only_apps (bool): only list app scopes (default True)
        mappers (bool): list mappers (default False)

    Returns:
        dict: scope name: info
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/client-scopes'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    scopes = r.json()
    ret = {}
    for s in scopes:
        if s['protocol'] != 'openid-connect':
            continue
        if only_apps and 'app' not in s['attributes']:
            continue
        ret[s['name']] = {k:s[k] for k in s if k in ('id','name','attributes')}
        if mappers and 'protocolMappers' in s:
            ret[s['name']]['protocolMappers'] = s['protocolMappers']
    return ret

def create_app(appname, appurl, roles=['read','write'], builtin_scopes=[], access='public', service_account=False, token=None):
    """
    Create an application ("client") in Keycloak.

    Args:
        appname (str): appname ("clientId") of application to create
        appurl (str): base url of app
        roles (list): roles of app
        builtin_scopes (list): builtin Keycloak scopes to allow (profile, email, institution) (default: none)
        access (str): app scope access to roles (public, apps, none) (default: public)
        service_account (bool): enable the service account (default: False)
    """
    if access not in ('public','apps','none'):
        raise Exception('access is not one of the options: ["public", "apps", "none"]')
    if any(True for s in builtin_scopes if s not in ('profile', 'email', 'institution')):
        raise Exception('builtin_scopes has invalid scope. options are ["profile", "email", "institution"]')
    if not appurl.startswith('http'):
        raise Exception('bad appurl')

    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    # create app
    try:
        app_info(appname, token=token)
    except Exception:
        print(f'creating app "{appname}"')
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients'
        args = {
            'access': {'configure': True, 'manage': True, 'view': True},
            'adminUrl': appurl,
            'attributes': {
                'app': 'true',
                'display.on.consent.screen': 'false',
                'exclude.session.state.from.auth.response': 'false',
                'saml.assertion.signature': 'false',
                'saml.authnstatement': 'false',
                'saml.client.signature': 'false',
                'saml.encrypt': 'false',
                'saml.force.post.binding': 'false',
                'saml.multivalued.roles': 'false',
                'saml.onetimeuse.condition': 'false',
                'saml.server.signature': 'false',
                'saml.server.signature.keyinfo.ext': 'false',
                'saml_force_name_id_format': 'false',
                'tls.client.certificate.bound.access.tokens': 'false',
            },
            'authenticationFlowBindingOverrides': {},
            'bearerOnly': False,
            'clientAuthenticatorType': 'client-secret',
            'clientId': appname,
            'consentRequired': True,
            'defaultClientScopes': [],
            'directAccessGrantsEnabled': False,
            'enabled': True,
            'frontchannelLogout': False,
            'fullScopeAllowed': True,
            'implicitFlowEnabled': False,
            'nodeReRegistrationTimeout': -1,
            'notBefore': 0,
            'optionalClientScopes': [],
            'protocol': 'openid-connect',
            'publicClient': False,
            'redirectUris': [f'{appurl}/*'],
            'rootUrl': appurl,
            'serviceAccountsEnabled': service_account,
            'standardFlowEnabled': True,
            'surrogateAuthRequired': False,
            'webOrigins': [appurl],
        }
        r = requests.post(url, json=args, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()

        ret = app_info(appname, token=token)
        client_id = ret['id']

        # create roles
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{client_id}/roles'
        for name in roles:
            args = {'name': name}
            r = requests.post(url, json=args, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()

        # create scope
        all_scopes = list_scopes(token=token)
        if appname not in all_scopes:
            url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/client-scopes'
            args = {
                'attributes': {
                    'app': 'app',
                    'access': access,
                    'display.on.consent.screen': 'false',
                    'include.in.token.scope': 'true',
                },
                'name': appname,
                'protocol': 'openid-connect',
            }
            r = requests.post(url, json=args, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()
            all_scopes = list_scopes(token=token)
            scope_id = all_scopes[appname]['id']

            url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/client-scopes/{scope_id}/protocol-mappers/models'
            args = {
                'config': {
                    'access.token.claim': 'true',
                    'claim.name': f'roles.{appname}',
                    'id.token.claim': 'false',
                    'jsonType.label': 'String',
                    'multivalued': 'true',
                    'userinfo.token.claim': 'false',
                    'usermodel.clientRoleMapping.clientId': appname,
                },
                'name': 'role-mapper',
                'protocol': 'openid-connect',
                'protocolMapper': 'oidc-usermodel-client-role-mapper'
            }
            r = requests.post(url, json=args, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()

        # apply scope to client
        scope_id = all_scopes[appname]['id']
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{client_id}/optional-client-scopes/{scope_id}'
        r = requests.put(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()

        if access == 'public':
            # apply scope to "public" app
            ret = app_info("public", token=token)
            url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{ret["id"]}/optional-client-scopes/{scope_id}'
            r = requests.put(url, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()
        if access in ('public', 'apps'):
            # apply scope to all "apps"
            ret = list_apps(token=token)
            for app in ret.values():
                if appname not in app['optionalClientScopes']:
                    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{app["id"]}/optional-client-scopes/{scope_id}'
                    r = requests.put(url, headers={'Authorization': f'bearer {token}'})
                    r.raise_for_status()

        if service_account:
            # get service account
            url = f'{cfg["keycloak_url"]}/auth/admin/realms/master/clients/{client_id}/service-account-user'
            r = requests.get(url, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()
            svc_user = r.json()

            # get service roles
            url = f'{cfg["keycloak_url"]}/auth/admin/realms/master/users/{svc_user["id"]}/role-mappings/clients/{realm_client}'
            r = requests.get(url, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()
            svc_roles = r.json()

            for role in svc_roles:
                if role['name'] == 'uma_authorization': # delete this to prevent self-administration
                    url = f'{cfg["keycloak_url"]}/auth/admin/realms/master/users/{svc_user["id"]}/role-mappings/clients/{realm_client}'
                    r = requests.delete(url, [role], headers={'Authorization': f'bearer {token}'})
                    r.raise_for_status()

        print(f'app "{appname}" created')
    else:
        print(f'app "{appname}" already exists')

def delete_app(appname, token=None):
    """
    Delete an application ("client") in Keycloak.

    Args:
        appname (str): appname ("clientId') of application to delete
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    ret = list_scopes(token=token)
    if appname in ret:
        scope_id = ret[appname]['id']
        # delete scope usage in apps
        for app in list_apps(token=token).values():
            if appname in app['optionalClientScopes']:
                url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{app["id"]}/optional-client-scopes/{scope_id}'
                r = requests.delete(url, headers={'Authorization': f'bearer {token}'})
                r.raise_for_status()
        ret = app_info('public', token=token)
        if appname in ret['optionalClientScopes']:
            url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{ret["id"]}/optional-client-scopes/{scope_id}'
            r = requests.delete(url, headers={'Authorization': f'bearer {token}'})
            r.raise_for_status()

        # delete scope
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/client-scopes/{scope_id}'
        r = requests.delete(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()

    try:
        ret = app_info(appname, token=token)
    except Exception:
        print(f'app "{appname}" does not exist')
    else:
        client_id = ret['id']
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{client_id}'
        r = requests.delete(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        print(f'app "{appname}" deleted')

def get_app_role_mappings(appname, role=None, token=None):
    """
    Get an application's role-group mappings.

    Args:
        appname (str): appname ("clientId") of application
        role (str): application role name (optional, default: all roles)

    Returns:
        dict: role: list of groups
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    try:
        app_data = app_info(appname, token=token)
    except Exception:
        raise Exception(f'app "{appname}" does not exist')

    if role and role not in app_data['roles']:
        raise Exception(f'role "{role}" does not exist in app "{appname}"')
    
    client_id = app_data['id']

    groups_with_role = {}
    groups = list_groups(token=token)
    for g in groups:
        gid = groups[g]['id']
    
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/groups/{gid}/role-mappings/clients/{client_id}'
        r = requests.get(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        ret = r.json()
        for mapping in ret:
            role_name = mapping['name']
            if (not role) or role == role_name:
                if role_name in groups_with_role:
                    groups_with_role[role_name].append(g)
                else:
                    groups_with_role[role_name] = [g]
    return groups_with_role

def add_app_role_mapping(appname, role, group, token=None):
    """
    Add a role-group mapping to an application.

    Args:
        appname (str): appname ("clientId") of application
        role (str): application role name
        group (str): group name
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    try:
        app_data = app_info(appname, token=token)
    except Exception:
        raise Exception(f'app "{appname}" does not exist')

    if role not in app_data['roles']:
        raise Exception(f'role "{role}" does not exist in app "{appname}"')

    gid = group_info(group, token=token)['id']
    client_id = app_data['id']

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/groups/{gid}/role-mappings/clients/{client_id}'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    mappings = r.json()
    if any(role == mapping['name'] for mapping in mappings):
        print(f'app "{appname}" role mapping {role}-{group} already exists')
    else:
        # get full role info
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{client_id}/roles'
        r = requests.get(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        ret = r.json()
        for r in ret:
            if r['name'] == role:
                role_info = r
                break
        else:
            raise Exception('could not get role representation')
        
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/groups/{gid}/role-mappings/clients/{client_id}'
        args = [role_info]
        r = requests.post(url, json=args, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        print(f'app "{appname}" role mapping {role}-{group} created')

def delete_app_role_mapping(appname, role, group, token=None):
    """
    Delete a role-group mapping to an application.

    Args:
        appname (str): appname ("clientId") of application
        role (str): application role name
        group (str): group name
    """
    cfg = config({
        'realm': ConfigRequired,
        'keycloak_url': ConfigRequired,
    })

    try:
        app_data = app_info(appname, token=token)
    except Exception:
        raise Exception(f'app "{appname}" does not exist')

    if role not in app_data['roles']:
        raise Exception(f'role "{role}" does not exist in app "{appname}"')

    gid = group_info(group, token=token)['id']
    client_id = app_data['id']

    url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/groups/{gid}/role-mappings/clients/{client_id}'
    r = requests.get(url, headers={'Authorization': f'bearer {token}'})
    r.raise_for_status()
    mappings = r.json()
    if not any(role == mapping['name'] for mapping in mappings):
        print(f'app "{appname}" role mapping {role}-{group} does not exist')
    else:
        # get full role info
        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/clients/{client_id}/roles'
        r = requests.get(url, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        ret = r.json()
        for r in ret:
            if r['name'] == role:
                role_info = r
                break
        else:
            raise Exception('could not get role representation')

        url = f'{cfg["keycloak_url"]}/auth/admin/realms/{cfg["realm"]}/groups/{gid}/role-mappings/clients/{client_id}'
        args = [role_info]
        r = requests.delete(url, json=args, headers={'Authorization': f'bearer {token}'})
        r.raise_for_status()
        print(f'app "{appname}" role mapping {role}-{group} deleted')

def main():
    import argparse
    from pprint import pprint
    from .token import get_token

    parser = argparse.ArgumentParser(description='Keycloak application management')
    subparsers = parser.add_subparsers()
    parser_list = subparsers.add_parser('list', help='list apps')
    parser_list.set_defaults(func=list_apps)
    parser_info = subparsers.add_parser('info', help='app info')
    parser_info.add_argument('appname', help='application name')
    parser_info.set_defaults(func=app_info)
    parser_list_scopes = subparsers.add_parser('list_scopes', help='list scopes')
    parser_list_scopes.add_argument('--include-builtin', dest='only_apps', action='store_false', default=True, help='include builtin Keycloak scopes')
    parser_list_scopes.add_argument('--mappers', action='store_true', help='include mappers')
    parser_list_scopes.set_defaults(func=list_scopes)
    parser_create = subparsers.add_parser('create', help='create a new app')
    parser_create.add_argument('appname', help='application name')
    parser_create.add_argument('appurl', help='app base url')
    parser_create.set_defaults(func=create_app)
    parser_delete = subparsers.add_parser('delete', help='delete an app')
    parser_delete.add_argument('appname', help='application name')
    parser_delete.set_defaults(func=delete_app)
    parser_get_role_mappings = subparsers.add_parser('get_role_mappings', help='get app role-group mappings')
    parser_get_role_mappings.add_argument('appname', help='application name')
    parser_get_role_mappings.add_argument('-r','--role', help='role name')
    parser_get_role_mappings.set_defaults(func=get_app_role_mappings)
    parser_add_role_mapping = subparsers.add_parser('add_role_mapping', help='add an app role-group mapping')
    parser_add_role_mapping.add_argument('appname', help='application name')
    parser_add_role_mapping.add_argument('role', help='role name')
    parser_add_role_mapping.add_argument('group', help='group name')
    parser_add_role_mapping.set_defaults(func=add_app_role_mapping)
    parser_delete_role_mapping = subparsers.add_parser('delete_role_mapping', help='delete an app role-group mapping')
    parser_delete_role_mapping.add_argument('appname', help='application name')
    parser_delete_role_mapping.add_argument('role', help='role name')
    parser_delete_role_mapping.add_argument('group', help='group name')
    parser_delete_role_mapping.set_defaults(func=delete_app_role_mapping)
    args = parser.parse_args()

    token = get_token()

    args = vars(args)
    func = args.pop('func')
    ret = func(token=token, **args)
    if ret is not None:
        pprint(ret)

if __name__ == '__main__':
    main()