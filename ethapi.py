#ethapi.py Mizogg 07/08/2021 mizogg.co.uk Random Scan for ETH Addresses and Transactions Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import random
import eth_keys
from eth_keys import keys
import requests
import multiprocessing
from multiprocessing import Pool

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336

r = 0
cores=2 #CPU Control Set Cores

def seek(r):
    while True:
        api1="?apiKey=freekey"
        api2="?apiKey=freekey"
        #api3="?apiKey=freekey"
        #api4="?apiKey=freekey"
        #api5="?apiKey=freekey"
        #api6="?apiKey=freekey"
        #api7="?apiKey=freekey"
        #api8="?apiKey=freekey"
        #api9="?apiKey=freekey"
        #api10="?apiKey=freekey"
        mylist = [str(api1), str(api2)]
        #mylist = [str(api1), str(api2), str(api3), str(api4), str(api5), str(api6), str(api7), str(api8), str(api9), str(api10)]
        apikeys=random.choice(mylist)
        ran= random.randint(x,y)
        seed=str(ran)
        myhex = "%064x" % ran
        private_key = myhex[:64]
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        ethadd = keys.PublicKey(public_key_bytes).to_address()			#Eth address
        blocs=requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd +apikeys)
        ress = blocs.json()
        TXS = dict(ress)["countTxs"]
        print ( 'Ethereum Address    :  '  + ethadd +  ' : TX = '  +  str(TXS), end='\r')
        if int(TXS) > 0:
            print("ETHAPI.py---Random Scan for ETH Addresses Transactions------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD---ETHAPI.py")
            print ( ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' '\n' )
            print ('Ethereum Address    : '  + ethadd) #Ethereum winner
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey HEX : " + myhex)
            print("Matching Key ==== Ethereum Address Found!!!\n PrivateKey DEC: " + seed)
            print ( ' <================================= WINNER Ethereum Address With Transactions WINNER =================================>' '\n' )
            f=open(u"winner.txt","a")
            f.write('\n=============Ethereum Address With Transactions=====================')
            f.write('\nPrivateKey (hex): ' + myhex)
            f.write('\nPrivateKey (dec): ' + seed)
            f.write('\n Eth Address: ' + ethadd)
            f.write('\n=============Ethereum Address With Transactions=====================')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' + '\n')
            f.close()
#CPU Control Command
if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()