import time
import os
import web3
from web3 import Web3
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")
while True:
    privateKey = os.urandom(32)
    privateKey = '0x'+privateKey.hex()
    acct = web3.eth.Account.privateKeyToAccount(privateKey)
    ethadd= acct.address
    blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey=freekey") #Ethereum API Must create account to be better API
    ress = blocs.json()
    balance = dict(ress)["countTxs"]
    print (Fore.GREEN + 'Ethereum Address    :  ' + Style.RESET_ALL + ethadd + Fore.GREEN +'     : Transactions = ' + Fore.RED +  str(balance)+ Style.RESET_ALL) #Ethereum address display
    print(Fore.GREEN + 'PrivateKey  : ' + Style.RESET_ALL + privateKey + '\n') # Running Display Output
    if int(balance) > 0:
        print (Fore.YELLOW +' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + Style.RESET_ALL + '\n')
        print (Fore.GREEN + 'Ethereum Address    :  ' + Style.RESET_ALL + ethadd + Fore.GREEN +'     : Transactions = ' +  str(balance)+ Style.RESET_ALL) #Ethereum winner
        print(Fore.GREEN +  +"Matching Key ==== Ethereum Address Found!!!\n PrivateKey HEX : "+ Style.RESET_ALL + privateKey) #Ethereum winner
        print (Fore.YELLOW +' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' + Style.RESET_ALL + '\n')
        f=open(u"winner.txt","a")
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\nPrivateKey (hex): ' + privateKey)
        f.write('\n Eth Address: ' + ethadd)
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
        f.close()