import sys
import json
import requests
bitapi = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o=bitapi.json()
usd_price=o["bpi"]['USD']['rate_float']
try:
    amount = usd_price*float((sys.argv[1]))
    print(f"${amount:,.4f}")
except ValueError :
    sys.exit("Command-line argument is not a number")
except IndexError :
    sys.exit("Command-line argument is not a number")

