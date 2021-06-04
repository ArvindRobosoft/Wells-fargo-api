# Credentials/Input to get the token
from random import randint

#
token_url = 'https://identity.qa-regalpay.io/connect/token'
Username = 'ruchita@regal-us.com'
Password = 'Ruchita@1234'
INC_client_id = 'WellsFargoApp'
INC_client_secret = 'QN9wyWRJPdr2KTYp'
grant_type = 'password'
INC_Scope = 'WellsFargo-connect:view:setup WellsFargo-connect:manage:setup openid'
tenantId = '384bc679-02ca-4827-f893-08d8b5ece05e'
ACR_VALUES = "tenant:384bc679-02ca-4827-f893-08d8b5ece05e"

#urls

url = 'https://api.qa-regalpay.io'
payments = '/WellsFargo-connect/payments'
setup = '/WellsFargo-connect/setup'
credentials = '/WellsFargo-connect/credentials'
vendors = '/WellsFargo-connect/vendors'

random_value1 = randint(11111, 99999)
ExpectedCode201 = 201
ExpectedCode200 = 200

#

vendorType= 'vendorType'
companyId = 'companyId'
dateFormat = 'yyyy-MM-dd'
credentialName = 'credentialName'
password = 'Atlanta2009!'
userId = 'admin'
Start_date = ''
End_date = ''