import time
import requests

def check_price(coin):
  # Make an API call to get the current price of the coin
  url = f"https://api.coinmarketcap.com/v1/ticker/{coin}/"
  r = requests.get(url)
  data = r.json()
  # Get the current price of the coin from the API response
  price = float(data[0]["price_usd"])
  return price

def get_balance(coin):
  # Make an API call to get the current balance of the coin
  # You will need to replace this with a call to your own exchange's API
  balance = 0
  return balance

def buy_coin(coin, amount):
  # Place a buy order for the specified coin and amount
  # You will need to replace this with a call to your own exchange's API
  print(f"Buying {amount} {coin}")

def sell_coin(coin, amount):
  # Place a sell order for the specified coin and amount
  # You will need to replace this with a call to your own exchange's API
  print(f"Selling {amount} {coin}")

def main():
  while True:
    # Check the current price of XRP and FLR every 10 minutes
    xrp_price = check_price("xrp")
    flr_price = check_price("flr")
    # Get the current balance of XRP and FLR
    xrp_balance = get_balance("xrp")
    flr_balance = get_balance("flr")
    # If the price of XRP is higher than the price of FLR and we have more FLR than XRP, sell FLR and buy XRP
    if xrp_price > flr_price and flr_balance > xrp_balance:
      sell_coin("flr", flr_balance - xrp_balance)
      buy_coin("xrp", flr_balance - xrp_balance)
    # If the price of FLR is higher than the price of XRP and we have more XRP than FLR, sell XRP and buy FLR
    elif flr_price > xrp_price and xrp_balance > flr_balance:
      sell_coin("xrp", xrp_balance - flr_balance)
      buy_coin("flr", xrp_balance - flr_balance)
    # Sleep for 10 minutes before checking the prices again
    time.sleep(600)

if __name__ == "__main__":
  main()
