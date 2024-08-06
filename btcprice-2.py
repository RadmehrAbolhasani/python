import json
import requests
import sys
import pyttsx3


def main():
    # Get data from coindesk
    btc_price = get_btc_price

    # Show and read to result
    print(btc_price)
    read_text(btc_price)


def read_text(prompt):
    """
    Reads the given text prompt with default os
    voice actor exits program if any exeption happens
    """
    try:
        engine = pyttsx3.init()
        engine.say(prompt)
        engine.runAndWait()
    except:
        show_error("Failed to read document")


def get_btc_price():
    """Get btc price with get method from api.coindesk.com
    if succeed returns string message which contains btc usd price
    otherwise closes the program
    """
    # Call coindesk API
    try:
        r = requests.get("https://api.coindesk.com/vi/bpi/currentprice.json")
        if r.status_code != 200:
            show_error("Failed to receive correct response from API server")
    except:
        show_error("Failed to receive correct response from API server")
        # Extract btc price from response
        data = json.loads(r.text)
        btc_price = int(data["bpi"]["USD"]["rate_float"])
        result = f"Bitcoin current price is {btc_price}"
        return result


def show_error(prompt="Progress Failed!"):
    """Shows the given prompt as error message and closes
    the program
    """
    sys.exit(prompt)


if __name__ == "__main__":
    main()
