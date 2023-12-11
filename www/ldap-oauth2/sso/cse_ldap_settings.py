from django_auth_ldap.config import LDAPSearch
import ldap3


AUTH_LDAP_SERVER_URI = "ldap://1.ldap.cse.iitb.ac.in"
# [
#     "ldap://1.ldap.cse.iitb.ac.in",
#     "ldap://2.ldap.cse.iitb.ac.in",
#     "ldap://3.ldap.cse.iitb.ac.in",
#     "ldap://4.ldap.cse.iitb.ac.in",
# ]                                                                                                                                                                                                                                                                                                                                                
AUTH_LDAP_BIND_DN = ''
AUTH_LDAP_BIND_PASSWORD = ''
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'ou=People,dc=cse,dc=iitb,dc=ac,dc=in',
    ldap3.SUBTREE,
    '(employeeNumber=%(user)s)'
)


AUTH_LDAP_USER_ATTR_MAP = {
    'cse_first_name': 'cn',
    'cse_last_name': 'sn',
    'cse_email': 'mail',
    'cse_employee_type': 'employeeType',
    'cse_username': 'uid',
    'cse_role': 'description',
}


AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_START_TLS = True
PERMIT_EMPTY_PASSWORD = True