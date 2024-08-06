import requests
import pyttsx3
import json
import sys

# Call coindesk API
try:
    r = requests.get("https://api.coindesk.com/vi/bpi/currentprice.json")
    if r.status_code != 200:
        sys.exit("Failed to receive correct response from API server")
except:
    sys.exit("Failed to receive correct response from API server")

# Extract btc price from response
data = json.loads(r.text)
btc_price = int(data["bpi"]["USDT"]["rate_float"])
result = f"Bitcoin current price is {btc_price}"

# Read result
engine = pyttsx3.init()
engine.say(result)
print(result)
engine.runAndWait()
