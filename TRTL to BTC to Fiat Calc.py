# TRTL to BTC, GBP, USD Calculator V4 (Made by TildeSnake)
from forex_python.bitcoin import BtcConverter
import requests
import os

# Fetching BTC prices in GBP and USD
b = BtcConverter()
bitcoinGBP = b.get_latest_price('GBP')
bitcoinUSD = b.get_latest_price('USD')

# TRTL price (TradeSatoshi)
r = requests.get(url='https://tradesatoshi.com/api/public/getmarketsummary?market=TRTL_BTC')
priceSatoshi = (r.json()['result']['last'])
satsSatoshi = float(priceSatoshi) * 100000000
satsSatoshi = round(satsSatoshi)

# TRTL price (TradeOgre)
r = requests.get(url='https://tradeogre.com/api/v1/ticker/BTC-TRTL')
priceOgre = (r.json()['price'])
satsOgre = float(priceOgre) * 100000000
satsOgre = round(satsOgre)
    
# Opener
print("Welcome, the current TRTL prices are:")
print("TradeSatoshi:",satsSatoshi,"sats")
print("TradeOgre:",satsOgre,"sats\n")
amountTurtle = input("Enter the amount of TRTL: ")

# Value of BTC, GBP and USD (TradeSatoshi)
valueBitcoinSatoshi = (float(priceSatoshi) * float(amountTurtle))
valueBitcoinSatoshi = round(valueBitcoinSatoshi,5)
valueGBPSatoshi = bitcoinGBP * valueBitcoinSatoshi
valueGBPSatoshi = round(valueGBPSatoshi, 2)
valueUSDSatoshi = bitcoinUSD * valueBitcoinSatoshi
valueUSDSatoshi = round(valueUSDSatoshi, 2)

# Value of BTC, GBP and USD (TradeOgre)
valueBitcoinOgre = (float(priceOgre) * float(amountTurtle))
valueBitcoinOgre = round(valueBitcoinOgre,5)
valueGBPOgre = bitcoinGBP * valueBitcoinOgre
valueGBPOgre = round(valueGBPOgre, 2)
valueUSDOgre = bitcoinUSD * valueBitcoinOgre
valueUSDOgre = round(valueUSDOgre, 2)

print("\n----------------------------------")
print("By TradeSatoshi's prices you have:")
print("----------------------------------")
print("-",valueBitcoinSatoshi,"BTC")
print("-",valueGBPSatoshi,"GBP")
print("-",valueUSDSatoshi,"USD\n")

print("-------------------------------")
print("By TradeOgre's prices you have:")
print("-------------------------------")
print("-",valueBitcoinOgre,"BTC")
print("-",valueGBPOgre,"GBP")
print("-",valueUSDOgre,"USD")

os.system("pause")

'''
Idea...

With tradeogre prices you have:
- n BTC
- n GBP
- n USD

With tradesatoshi prices you have:
- n BTC
- n GBP
- n USD
'''
