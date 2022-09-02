import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except:
        sys.exit()

    out = response.json()
    amount= out["bpi"]["USD"]["rate"]
    amount = amount.replace(",","")
    amount = float(amount) * float(sys.argv[1])
    print(f"${amount:,.4f}")

