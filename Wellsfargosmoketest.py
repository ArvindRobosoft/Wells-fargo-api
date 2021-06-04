import json
from builtins import print


import requests
# import sys

# sys.stdout = open('D:\Project\kite.txt', 'w')

from Generic import *

# Populate Access Token for Accounts App
data = {'grant_type': grant_type, 'username': Username, 'password': Password, 'scope': INC_Scope,
        'acr_values': ACR_VALUES}

# Get access token
access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=True,
                                      auth=(INC_client_id, INC_client_secret))

# Print access token
print(access_token_response.text)
tokens = json.loads(access_token_response.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

# POST WellsFargo Setup Details
print("POST WellsFargo Setup Details")
parameters = {
    "vendorType": vendorType,
    "companyId": companyId,
    "dateFormat": dateFormat,

}
response = requests.post(url + setup, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result1 = 'PASS'
else:
    result1 = 'FAIL'

# GET WellsFargo Setup Details
print("GET Fargo Setup Details")
response = requests.get(url + setup, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result2 = 'PASS'
else:
    result2 = 'FAIL'

# POST WellsFargo sftp folder setup
print("POST WellsFargo sftp folder setup")
parameters = {
    "credentialName": credentialName,
    "password": password,
    "userId": userId,

}
response = requests.post(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result3 = 'PASS'
else:
    result3 = 'FAIL'

# GET WellsFargo tenant search
print("GET WellsFargo tenant search")
response = requests.get(url + setup, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result4 = 'PASS'
else:
    result4 = 'FAIL'

# ADD Bank Account
print("ADD Bank Account")
parameters = {
    "credentialName": credentialName,
    "password": password,
    "userId": userId,

}
response = requests.post(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

# GET Bank Accounts for tenant
print("GET Bank Accounts for tenant")
response = requests.post(url + vendors, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
VendorID = data['result']['vendorRemittanceCCList'][0]['id']
if response.status_code == ExpectedCode200:
    result6 = 'PASS'
else:
    result6 = 'FAIL'

# Add Card Account
print("Add Card Account")
parameters = {
    "credentialName": credentialName,
    "password": password,
    "userId": userId,

}
response = requests.post(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

# GET card accounts for tenant
print("GET card accounts for tenant")
response = requests.get(url + setup, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

# POST validate payments
print("POST validate payments")
parameters = {
    "vendorType": vendorType,
    "companyId": companyId,
    "dateFormat": dateFormat,

}
response = requests.post(url + payments, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result9 = 'PASS'
else:
    result9 = 'FAIL'

# POST supported payment types
print("POST supported payment types")
parameters = {
    "vendorType": vendorType,
    "companyId": companyId,
    "dateFormat": dateFormat,

}
response = requests.post(url + payments, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result10 = 'PASS'
else:
    result10 = "FAIL"

# POST sftp setup details
print("POST sftp setup details")
parameters = {
    "vendorType": vendorType,
    "companyId": companyId,
    "dateFormat": dateFormat,

}
response = requests.post(url + setup, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result11 = 'PASS'
else:
    result11 = 'FAIL'

# POST sftp ssh key
print("POST sftp ssh key")
parameters = {
    "vendorType": vendorType,
    "companyId": companyId,
    "dateFormat": dateFormat,

}
response = requests.post(url + setup, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result12 = 'PASS'
else:
    result12 = 'FAIL'

# GET SFTP public key
print("GET SFTP public key")
response = requests.get(url + setup, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result13 = 'PASS'
else:
    result13 = 'FAIL'

# POST sftp credential
print("POST sftp credential")
parameters = {
    "credentialName": credentialName,
    "password": password,
    "userId": userId,

}
response = requests.post(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result14 = 'PASS'
else:
    result14 = 'FAIL'

# POST sftp connection
print("POST sftp connection")
parameters = {
    "credentialName": credentialName,
    "password": password,
    "userId": userId,

}
response = requests.post(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode201:
    result15 = 'PASS'
else:
    result15 = 'FAIL'

# PUT update Bank Account
print("PUT update Bank Account")
response = requests.put(url + credentials  , data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result16 = 'PASS'
else:
    result16 = 'FAIL'

# PUT Update card account
print("PUT Update card account")
response = requests.put(url + credentials, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result17 = 'PASS'
else:
    result17 = 'FAIL'

#  DELETE bank account
print("DELETE bank account")
response = requests.delete(url + credentials, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result18 = 'PASS'
else:
    result18 = 'FAIL'

# DELETE card account
print("DELETE card account")
response = requests.delete(url + credentials, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result19 = 'PASS'
else:
    result19 = 'FAIL'

# DELETE sftp credential
print("DELETE sftp credential")
response = requests.delete(url + credentials, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result20 = 'PASS'
else:
    result20 = 'FAIL'

# DELETE sftp ssh key
print("DELETE sftp ssh key")
response = requests.delete(url + credentials, headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode200:
    result21 = 'PASS'
else:
    result21 = 'FAIL'

print("POST WellsFargo Setup Details: " + result1)
print("GET WellsFargo Setup Details: " + result2)
print("POST WellsFargo sftp folder setup: " + result3)
print("GET WellsFargo tenant search: " + result4)

print("ADD Bank Account: " + result5)
print("GET Bank Accounts for tenant: " + result6)

print("Add Card Account: " + result7)
print("GET card accounts for tenant: " + result8)

print("POST validate payments: " + result9)
print("POST supported payment types: " + result10)

print("POST sftp setup details: " + result11)
print("POST sftp ssh key: " + result12)
print("GET SFTP public key: " + result13)
print("POST sftp credential: " + result14)
print("POST sftp connection: " + result15)

print("PUT update Bank Account: " + result16)
print("PUT Update card account: " + result17)

print("DELETE bank account: " + result18)
print("DELETE card account: " + result19)
print("DELETE sftp credential: " + result20)
print("DELETE sftp ssh key: " + result21)
