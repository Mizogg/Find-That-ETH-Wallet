import random
import eth_keys
from eth_keys import keys
import requests
import atexit
from time import time
from datetime import timedelta, datetime
import colorama
from colorama import Fore, Back, Style
colorama.init()

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")
count=0
while True:
    count+=1
    ran= random.randint(x,y)
    seed=str(ran)
    myhex = "%064x" % ran
    private_key = myhex[:64]
    private_key_bytes = bytes.fromhex(private_key)
    public_key_hex = keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
    ethadd = keys.PublicKey(public_key_bytes).to_address()
    blocs = requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd + "?apiKey=freekey")
    ress = blocs.json()
    balance = dict(ress)["countTxs"]
    print(Fore.BLUE + "ETHR.py---" + Fore.RED + "Random Scan for ETH Addresses Transactions------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---ETHR.py"  + Style.RESET_ALL)
    print (Fore.GREEN + "Scan Number" + ' : ' + Style.RESET_ALL + str (count)+ ' --Time--->'  + seconds_to_str())
    print (Fore.YELLOW + 'Ethereum Address    :  ' +  Style.RESET_ALL + ethadd + Fore.YELLOW + '     : Transactions = ' + Fore.RED +  str(balance))
    print(Fore.YELLOW + 'PrivateKey' + ' : ' +  Style.RESET_ALL + myhex + '\n')
    if int(balance) > 0:
        print(Fore.BLUE + "ETHR.py---" + Fore.RED + "Random Scan for ETH Addresses Transactions------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---ETHR.py"  + Style.RESET_ALL + seconds_to_str())
        print (Fore.BLUE +  ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' '\n' +  Style.RESET_ALL)
        print (Fore.GREEN +'Ethereum Address    : '  + ethadd) #Ethereum winner
        print(Fore.GREEN +"Matching Key ==== Ethereum Address Found!!!\n PrivateKey HEX : " + myhex)
        print(Fore.GREEN +"Matching Key ==== Ethereum Address Found!!!\n PrivateKey DEC: " + seed)
        print (Fore.BLUE +  ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' '\n' +  Style.RESET_ALL)
        f=open(u"winner.txt","a")
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\nPrivateKey (hex): ' + myhex)
        f.write('\nPrivateKey (dec): ' + seed)
        f.write('\n Eth Address: ' + ethadd)
        f.write('\n=============Ethereum Address With Transactions=====================')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
        f.close()