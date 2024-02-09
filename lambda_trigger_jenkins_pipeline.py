import requests
import time

## this code trigger jenkin pipeline 

def lambda_handler(event, context):
    time.sleep(60)
    res = requests.get('http://<user>:<password>@<build_url>/build?token=<token_value>', verify=False)
    print(res)
    
