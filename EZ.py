# OpenOPS - PowerStore, Dell EMC PowerStore Monitor
# PowerStore Version: 1.0.0.0.5.109
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 2nd Aug. 2020

# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote


# Set up endpoint and authentication credentials
endpoint = 'https://IP address/api/rest/'
username = 'username'
password = 'password'
auth = HTTPBasicAuth(username, password)

# Prepare query string, if any
api = 'appliance'
query = { 'select': 'id,name,nodes' }
encoded_query = urlencode(query)
url = endpoint + api + '?' + encoded_query

# Get response
res = requests.get(url, auth=auth, verify=False)

# Retrieve header token
token = dict(res.headers)['DELL-EMC-TOKEN']

# Append token in following requests
# For GET requests
headers = {
    'DELL-EMC-TOKEN': token
}
response=requests.get(url, headers=headers, verify=False, cookies=res.cookies)
payload = json.loads(response.text)


# For POST requests
api = 'metrics/generate'
data = {  "entity": "performance_metrics_by_node",  "entity_id": "N2"}

headers = {
    'Content-Type': "application/json",
	'Accept': "application/json",
	'Accept-Language': 'en-US',
    'DELL-EMC-TOKEN': token
}

url = endpoint + api
response2 = requests.post(url, headers=headers, json=data, cookies=res.cookies, verify=False)
