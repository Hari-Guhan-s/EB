import requests
import json

url = 'http://localhost:8089/user_EB_data'
headers = {'Content-Type': 'application/json'}
data = {
    
        "name":"vignesh",
        "value":"20000"
        
    
}	
data_json = json.dumps(data)
r = requests.post(url=url, data=data_json, headers=headers)
print (r)