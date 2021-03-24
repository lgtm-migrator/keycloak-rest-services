import logging

from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE
import requests
from rest_tools.server import from_environment


logger = logging.getLogger('krs.ldap')

class LDAP:
    """
    LDAP client with a few basic actions to suppliment Keycloak
    """
    def __init__(self):
        self.config = from_environment({
            'LDAP_URL': None,
            'LDAP_ADMIN_USER': 'cn=admin,dc=icecube,dc=wisc,dc=edu',
            'LDAP_ADMIN_PASSWORD': 'admin',
            'LDAP_USER_BASE': 'ou=people,dc=icecube,dc=wisc,dc=edu',
        })

    async def keycloak_ldap_link(self, keycloak_token=None):
        cfg = from_environment({
            'KEYCLOAK_URL': None,
            'KEYCLOAK_REALM': None,
        })
        url = f'{cfg["KEYCLOAK_URL"]}/auth/admin/realms/{cfg["KEYCLOAK_REALM"]}/components'

        args = {
            "name": "ldap",
            "providerId": "ldap",
            "providerType": "org.keycloak.storage.UserStorageProvider",
            "config": {
                "connectionUrl": [self.config['LDAP_URL']],
                "bindCredential": [self.config['LDAP_ADMIN_PASSWORD']],
                "bindDn": [self.config['LDAP_ADMIN_USER']],
                "usersDn": [self.config['LDAP_USER_BASE']],
                "userObjectClasses": ["inetOrgPerson, organizationalPerson"],
                "usernameLDAPAttribute": ["uid"],
                "uuidLDAPAttribute": ["uid"],
                "rdnLDAPAttribute": ["uid"],
                "fullSyncPeriod": ["604800"],
                "pagination": ["true"],
                "connectionPooling": ["true"],
                "cachePolicy": ["DEFAULT"],
                "useKerberosForPasswordAuthentication": ["false"],
                "importEnabled": ["true"],
                "enabled": ["true"],
                "changedSyncPeriod": ["60"],
                "lastSync": ["-1"],
                "vendor": ["other"],
                "allowKerberosAuthentication": ["false"],
                "syncRegistrations": ["true"],
                "authType": ["simple"],
                "debug": ["false"],
                "searchScope": ["1"],
                "useTruststoreSpi": ["ldapsOnly"],
                "trustEmail": ["false"],
                "priority": ["0"],
                "editMode": ["WRITABLE"],
                "validatePasswordPolicy": ["false"],
                "batchSizeForSync": ["1000"]
            }
        }
        r = requests.post(url, headers={'Authorization': f'bearer {keycloak_token}'}, json=args)
        r.raise_for_status()

    def list_users(self, attrs=None):
        """
        List user information in LDAP.

        Args:
            attrs (list): attributes from each user to return (default: ALL)

        Returns:
            dict: username: attr dict
        """
        # define the server
        s = Server(self.config['LDAP_URL'], get_info=ALL)

        # define the connection
        c = Connection(s, auto_bind=True)

        # search for the user
        ret = c.search(self.config['LDAP_USER_BASE'], '(uid=*)', attributes=ALL_ATTRIBUTES)
        if not ret:
            raise Exception(f'Search users failed: {c.result["message"]}')
        ret = {}
        for entry in c.entries:
            entry = entry.entry_attributes_as_dict
            if attrs:
                val = {k: (entry[k][0] if len(entry[k]) == 1 else entry[k]) for k in entry if k in attrs}
            else:
                val = {k: (entry[k][0] if len(entry[k]) == 1 else entry[k]) for k in entry}
            ret[entry['uid'][0]] = val
        return ret

    def get_user(self, username):
        """
        Get user information from LDAP.

        Args:
            username (str): username of user

        Returns:
            dict: user info

        Raises:
            KeyError
        """
        # define the server
        s = Server(self.config['LDAP_URL'], get_info=ALL)

        # define the connection
        c = Connection(s, auto_bind=True)

        # search for the user
        ret = c.search(self.config['LDAP_USER_BASE'], f'(uid={username})', attributes=ALL_ATTRIBUTES)
        if not ret:
            raise KeyError(f'user {username} not found')
        return c.entries[0]

    def create_user(self, username, firstName, lastName, email):
        """
        Add a user to LDAP.

        Args:
            username (str): username of user
            firstName (str): first name of user
            lastName (str): last name of user
            email (str): email of user
        """
        # define the server
        s = Server(self.config['LDAP_URL'], get_info=ALL)

        # define the connection
        c = Connection(s, user=self.config['LDAP_ADMIN_USER'], password=self.config['LDAP_ADMIN_PASSWORD'], auto_bind=True)

        # check if user already exists
        ret = c.search(self.config['LDAP_USER_BASE'], f'(uid={username})')
        if ret:
            raise Exception(f'User {username} already exists')

        # perform the Add operation
        objectClasses = ['inetOrgPerson', 'organizationalPerson', 'person', 'top']
        attrs = {
            'cn': f'{firstName} {lastName}',
            'sn': lastName,
            'givenName': firstName,
            'mail': email,
            'uid': username,
        }
        ret = c.add(f'uid={username},{self.config["LDAP_USER_BASE"]}', objectClasses, attrs)
        if not ret:
            raise Exception(f'Create user {username} failed: {c.result["message"]}')

        # close the connection
        c.unbind()

    def modify_user(self, username, attributes=None, objectClass=None, removeObjectClass=None):
        """
        Modify a user in LDAP.

        Args:
            username (str): username in LDAP
            attributes (dict): attributes to modify
            objectClass (str): objectClass to add (default: None)
            removeObjectClass (str): objectClass to remove (default: None)
        """
        if not attributes:
            attributes = {}

        # define the server
        s = Server(self.config['LDAP_URL'], get_info=ALL)

        # define the connection
        c = Connection(s, user=self.config['LDAP_ADMIN_USER'], password=self.config['LDAP_ADMIN_PASSWORD'], auto_bind=True, raise_exceptions=True)

        # check if user exists
        ret = c.search(self.config['LDAP_USER_BASE'], f'(uid={username})', attributes=ALL_ATTRIBUTES)
        if not ret:
            raise Exception(f'User {username} does not exist')
        ret = c.entries[0]

        vals = {}
        for a in attributes:
            v = attributes[a] if isinstance(attributes[a], list) else [attributes[a]]
            if attributes[a] is None:
                if a in ret:
                    vals[a] = [(MODIFY_DELETE, [])]
                else:
                    continue  # trying to delete an attr that doesn't exist
            elif a in ret:
                vals[a] = [(MODIFY_REPLACE, v)]
            else:
                vals[a] = [(MODIFY_ADD, v)]

        if objectClass and removeObjectClass:
            raise Exception('cannot add and remove object classes at once')
        elif objectClass and objectClass not in ret['objectClass']:
            vals['objectClass'] = [(MODIFY_ADD, [objectClass])]
        elif removeObjectClass and removeObjectClass in ret['objectClass']:
            vals['objectClass'] = [(MODIFY_DELETE, [removeObjectClass])]

        # perform the operation
        logger.debug(f'ldap change for user {username}: {vals}')
        try:
            ret = c.modify(f'uid={username},{self.config["LDAP_USER_BASE"]}', vals)
        except Exception:
            logger.debug('ldap exception', exc_info=True)
            raise Exception(f'Modify user {username} failed')

        # close the connection
        c.unbind()
