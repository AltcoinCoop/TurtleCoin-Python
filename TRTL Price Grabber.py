import requests
import time
import os

def get_price_tradesatoshi():
    r = requests.get(url='https://tradesatoshi.com/api/public/getmarketsummary?market=TRTL_BTC')
    last = (r.json()['result']['last'])
    high = (r.json()['result']['high'])
    low = (r.json()['result']['low'])

    high = high * 100000000
    low = low * 100000000
    last = last * 100000000

    last = round(last)
    high = round(high)
    low = round(low)

    print("-------------------")
    print("TradeSatoshi Stats:")
    print("-------------------")
    print("High   ",high,"sats")
    print("Last   ",last,"sats")
    print("Low    ",low,"sats")

def get_price_tradeogre():
    r = requests.get(url='https://tradeogre.com/api/v1/ticker/BTC-TRTL')
    last = (r.json()['price'])
    high = (r.json()['high'])
    low = (r.json()['low'])

    high = float(high) * 100000000
    low = float(low) * 100000000
    last = float(last) * 100000000

    last = round(last)
    high = round(high)
    low = round(low)

    print("\n----------------")
    print("TradeOgre Stats:")
    print("----------------")
    print("High   ",high,"sats")
    print("Last   ",last,"sats")
    print("Low    ",low,"sats")
    

def get_price_trtl():
    print("\nGrabbing info...\n")

    get_price_tradesatoshi()
    get_price_tradeogre()

    time.sleep(60)
    os.system('cls')
    
    return get_price_trtl()

get_price_trtl()

