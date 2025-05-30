import requests
import json
client_id='3MVG9GXbtnGKjXe4bAmlqdLk4s2THEbv2ksYmbc7R.X6uqBsSyr29oib.rDQcD79ZgvcBYRJuTnGmKApk4AwS'
client_secret='0D9E9542023305D1463E42D6BFB557019B745154A2E3EB6735EB696E1AFAB8CB'



GraviteeKeyAut= "3f1ced76-1584-4337-ab64-d8617b29ec20"
GraviteeKeyGet= "91429100-b750-4268-bc6c-c2f062bd8a73"
url='https://api.ari.np.auchan.com/pl/customer-diamond/v1/crm/oauth2/token' 
# url='https://api-private-yoda.ari.internal.auchan.com/pl/customer-diamond/v1/crm/oauth2/token'
params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
    
}

headers = {
    'X-Gravitee-Api-Key': GraviteeKeyAut,
    'Content-Type': 'application/json',
    'Cookie': 'CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

response = requests.post(url,params=params, headers=headers)


if response.status_code == 200:
    access_token = response.json().get('access_token')
    print("Access token:", access_token)
else:
    print("Błąd pobierania tokenu:", response.status_code, response.text)
    exit()

customer='001KI00000BZzyKYAT' 
# url=f'https://api.ari.np.auchan.com/pl/customer-diamond/v1/customers/{customer}/attributes/type-code'
url=f'https://api.ari.np.auchan.com/pl/customer-diamond/v1/customers/{customer}/attributes'

# url=f'https://api-private-yoda.ari.internal.auchan.com/pl/customer-diamond/v1/customers/{customer}/attributes'
headers = {
    'X-Gravitee-Api-Key': GraviteeKeyGet,
    'Authorization': f'Bearer {access_token}',
    
    'Content-Type': 'application/json',
    'Cookie': 'CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
}

params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'filters': 'channels'
}


res=requests.get(url,params=params,headers=headers)
data=res.json()
data=json.dumps(data,indent=4)
print(data)
# print(json.dumps(res.json(), indent=4, ensure_ascii=False))