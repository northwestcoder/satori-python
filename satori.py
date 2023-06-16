import json
import requests
import time

def auth(apihost, serviceaccount_id, serviceaccount_key):

	creation_time = time.time()
	headers = {'content-type': 'application/json', 'accept': 'application/json'}
	url = "https://{}/api/authentication/token".format(apihost)
	try:
		r = requests.post(url, 
						  headers=headers, 
						  data='{"serviceAccountId": "' + serviceaccount_id + 
						  '", "serviceAccountKey": "' + serviceaccount_key + '"}')
		response = r.json()
		satori_token = response["token"]
	except Exception as err:
		print("Exception TYPE:", type(err))
	else:
		#print("new token created at: " + str(creation_time))
		#print("token: " + str(satori_token))
		headers = {
		'Authorization': 'Bearer {}'.format(satori_token), 
		'Content-Type': 'application/json', 'Accept': 'application/json'
		}
		return headers

#test_auth = satori_auth(apihost, serviceaccount_id, serviceaccount_key)
#print(test_auth)

def get_datastores(apihost, headers, account_id):

	url =  "https://{}/api/v1/datastore?accountId={}&pageSize=500".format(apihost, account_id)
	#print("trying to find all datastores: " + url)

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
	except requests.exceptions.RequestException as err:
		print("EXCEPTION: ", type(err))
	else:
		return response.json()

#test_datastores = satori_get_datastores(apihost, account_id, satori_auth(apihost, serviceaccount_id, serviceaccount_key))
#print(test_datastores)

def get_datastore_connection(apihost, headers, datastore_id):

	url =  "https://{}/api/v1/datastore/{}".format(apihost, datastore_id)
	#print("trying to find datastore : " + datastore_id)

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
	except requests.exceptions.RequestException as err:
		print("EXCEPTION: ", type(err))
	else:
		return response.json()

