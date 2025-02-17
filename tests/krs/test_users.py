import pytest

from krs.token import get_token
from krs import users

from ..util import keycloak_bootstrap

@pytest.mark.asyncio
async def test_list_users_empty(keycloak_bootstrap):
    ret = await users.list_users(rest_client=keycloak_bootstrap)
    assert ret == {}

@pytest.mark.asyncio
async def test_list_users(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    ret = await users.list_users(rest_client=keycloak_bootstrap)
    assert list(ret.keys()) == ['testuser']
    assert ret['testuser']['firstName'] == 'first'
    assert ret['testuser']['lastName'] == 'last'
    assert ret['testuser']['email'] == 'foo@test'

@pytest.mark.asyncio
async def test_user_info(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['firstName'] == 'first'
    assert ret['lastName'] == 'last'
    assert ret['email'] == 'foo@test'

@pytest.mark.asyncio
async def test_create_user(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)

@pytest.mark.asyncio
async def test_modify_user(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', attribs={'foo': 'bar'}, rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert 'foo' in ret['attributes']
    assert ret['attributes']['foo'] == 'bar'

@pytest.mark.asyncio
async def test_modify_user_asserts(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    with pytest.raises(RuntimeError):
        await users.modify_user('testuser', {'foo': 'bar'}, rest_client=keycloak_bootstrap)
    with pytest.raises(RuntimeError):
        await users.modify_user('testuser', first_name={'foo': 'bar'}, rest_client=keycloak_bootstrap)
    with pytest.raises(RuntimeError):
        await users.modify_user('testuser', last_name={'foo': 'bar'}, rest_client=keycloak_bootstrap)
    with pytest.raises(RuntimeError):
        await users.modify_user('testuser', email={'foo': 'bar'}, rest_client=keycloak_bootstrap)

@pytest.mark.asyncio
async def test_modify_user_firstName(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', first_name='bar', rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['firstName'] == 'bar'

@pytest.mark.asyncio
async def test_modify_user_lastName(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', last_name='bar', rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['lastName'] == 'bar'

@pytest.mark.asyncio
async def test_modify_user_email(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', email='bar@test', rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['email'] == 'bar@test'

@pytest.mark.asyncio
async def test_modify_user_existing_attr(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', attribs={'foo': 'bar'}, rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', attribs={'baz': 'foo'}, rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['attributes'] == {'foo': 'bar', 'baz': 'foo'}

@pytest.mark.asyncio
async def test_modify_user_del_attr(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', attribs={'foo': 'bar'}, rest_client=keycloak_bootstrap)
    await users.modify_user('testuser', attribs={'foo': None, 'baz': 'foo'}, rest_client=keycloak_bootstrap)
    ret = await users.user_info('testuser', rest_client=keycloak_bootstrap)
    assert ret['attributes'] == {'baz': 'foo'}

@pytest.mark.asyncio
async def test_set_user_password(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.set_user_password('testuser', 'foo', rest_client=keycloak_bootstrap)

@pytest.mark.asyncio
async def test_set_user_password_bad(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    with pytest.raises(Exception):
        await users.set_user_password('testuser', ['f', 'o', 'o'], rest_client=keycloak_bootstrap)

@pytest.mark.asyncio
async def test_delete_user(keycloak_bootstrap):
    await users.create_user('testuser', first_name='first', last_name='last', email='foo@test', rest_client=keycloak_bootstrap)
    await users.delete_user('testuser', rest_client=keycloak_bootstrap)
