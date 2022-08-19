import requests

api = input('Enter api key: ')
choice = input('Enter your choice:\n1. Load a script\n2. Enable a script: ')
headers = {
  'Accept': 'application/json',
  'X-ZAP-API-Key': api
}


port = input('Enter port number: ')
scriptName = input('Enter script name: ')
if choice == '1':
    scriptType = input('Enter script type: ')
    scriptPath = input('Enter script path: ')
    r = requests.get(f'http://127.0.0.1{port}/JSON/script/action/load/', params={
    'scriptName': scriptName,  'scriptType': scriptType,  'scriptEngine': 'Oracle Nashorn',  'fileName': scriptPath
    }, headers = headers)
elif choice == '2':
    r = requests.get('http://zap/JSON/script/view/scriptVars/', params={
    'scriptName': scriptName
    }, headers = headers)
    
print(r.json())
