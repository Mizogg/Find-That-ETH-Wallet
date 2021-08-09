import time
import os
import web3
from web3 import Web3
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

filename ='ethlist.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1

with open(filename) as file:
    add = file.read().split()
add = set(add)

print(Fore.RED, 'Starting search... Please Wait Total Addresses in ethlist.txt =  ', Style.RESET_ALL, line_count)
print(Fore.RED, "=====================================================")
while True:
    privateKey = os.urandom(32)
    privateKey = '0x'+privateKey.hex()
    acct = web3.eth.Account.privateKeyToAccount(privateKey)
    ethadd= acct.address
    print(Fore.RED, 'Total Addresses in ethlist.txt =  ', Style.RESET_ALL, line_count)
    print (Fore.GREEN, 'Ethereum Address    :  ', Style.RESET_ALL, ethadd) #Ethereum address display
    print(Fore.GREEN, 'PrivateKey  : ', Style.RESET_ALL, privateKey, '\n') # Running Display Output
    if ethadd in add:
        print (Fore.YELLOW, ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>', Style.RESET_ALL, '\n')
        print (Fore.GREEN, 'Ethereum Address    :  ', Style.RESET_ALL, ethadd) #Ethereum winner
        print(Fore.GREEN, 'Matching Key ==== Ethereum Address Found!!!\n PrivateKey HEX : ', Style.RESET_ALL, privateKey) #Ethereum winner
        print (Fore.YELLOW, ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>', Style.RESET_ALL, '\n')
        f=open(u"winner.txt","a")
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\nPrivateKey (hex): ', privateKey)
        f.write('\n Eth Address: ', ethadd)
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====', '\n')
        f.close()