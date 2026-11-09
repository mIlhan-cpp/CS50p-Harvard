import requests
import sys

try:
    
    if len(sys.argv)==2 :
       response=requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=7fe56f6568844ac22a433ef48bccf426d289b01f4c4e62fb43dfa14f7c183d1b')
       response=response.json()
       x=response['data']['priceUsd']
       x=float(x)
       amount=float(sys.argv[1])
       print(f'${amount*x:,.4f}')
    else:
        sys.exit('Missing command-line argument')
except requests.RequestException :
    sys.exit()
except ValueError:
    sys.exit('Command-line argument is not a number')