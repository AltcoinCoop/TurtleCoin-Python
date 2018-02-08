from win10toast import ToastNotifier
import requests
import time
import os

print("Loading...")

rs = requests.get(url='https://tradesatoshi.com/api/public/getmarketsummary?market=TRTL_BTC')
highS = (rs.json()['result']['high'])
lastS = (rs.json()['result']['last'])
lowS = (rs.json()['result']['low'])

highS = highS * 100000000
lastS = lastS * 100000000
lowS = lowS * 100000000

highS = round(highS)
lastS = round(lastS)
lowS = round(lowS)

ro = requests.get(url='https://tradeogre.com/api/v1/ticker/BTC-TRTL')
highO = (ro.json()['high'])
lastO = (ro.json()['price'])
lowO = (ro.json()['low'])

highO = float(highO) * 100000000
lastO = float(lastO) * 100000000
lowO = float(lowO) * 100000000

highO = round(highO)
lastO = round(lastO)
lowO = round(lowO)

os.system("cls")
print("Select which values you would like to see:\n")
highAnswer = input("24/hour high? [Y/N]: ")
lastAnswer = input("Last price? [Y/N]: ")
lowAnswer = input("24/hour low? [Y/N]: ")

if highAnswer == ("Y") or highAnswer == ("y"):
    highS = ("[High: "+str(highS)+" sats]   ")
    highO = ("[High: "+str(highO)+" sats]   ")
elif highAnswer == ("N") or highAnswer == ("n"):
    highS = ("")
    highO = ("")

if lastAnswer == ("Y") or lastAnswer == ("y"):
    lastS = ("[Last: "+str(lastS)+" sats]   ")
    lastO = ("[Last: "+str(lastO)+" sats]   ")
elif lastAnswer == ("N") or lastAnswer == ("n"):
    lastS = ("")
    lastO = ("")

if lowAnswer == ("Y") or lowAnswer == ("y"):
    lowS = ("[Low: "+str(lowS)+" sats]   ")
    lowO = ("[Low: "+str(lowO)+" sats]   ")
elif lowAnswer == ("N") or lowAnswer == ("n"):
    lowS = ("")
    lowO = ("")

def notify_ts_prices(highS, lastS, lowS, highO, lastO, lowO):
    toaster = ToastNotifier()
    toaster.show_toast("TurtleCoin Prices (TradeSatoshi)"
                       ,str(highS) + str(lastS) + str(lowS),
                       icon_path="TRTL.ico",
                       duration=5)
    while toaster.notification_active(): time.sleep(0.1)

def notify_to_prices(highS, lastS, lowS, highO, lastO, lowO):
    toaster = ToastNotifier()
    toaster.show_toast("TurtleCoin Prices (TradeOgre)"
                       ,highO + lastO + lowO,
                       icon_path="TRTL.ico",
                       duration=5)
    while toaster.notification_active(): time.sleep(0.1)

print("\nWhat would you like your updates to be in?")
print("           [M]inutes  [H]ours")
answer = input("")

if answer == ("M") or answer == ("m"):
    freq = input("\nWhat would you like the frequency of updates to be: ")
    freq = (int(freq) * 60)
    print("\nLeave this program running otherwise you wont get notifications...")

elif answer == ("H") or answer == ("h"):
    freq = input("\nWhat would you like the frequency of updates to be: ")
    freq = (int(freq) * 60 ** 2)
    print("\nLeave this program running otherwise you wont get notifications...")

def main():
    notify_ts_prices(highS, lastS, lowS, highO, lastO, lowO)
    notify_to_prices(highS, lastS, lowS, highO, lastO, lowO)
    time.sleep(freq)
    return main()

main()
