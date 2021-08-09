# Find-That-ETH-Wallet
Random Scan for ETH Addresses and Transactions

get a free key or 2 from https://ethplorer.io/ , After creating key you have to wait 10mins till active. Upto 2 API keys per account.
35,000 Request Hourly(Per API KEY)
756,000 Request Daily(Per API KEY)
![image](https://user-images.githubusercontent.com/88630056/128769247-14e9ba19-ed36-4a74-b3a1-129c858fbe70.png)


### ethapi.py

1. Number of CPU for multi proccessing
2. Insert API Key you can create 2 per account. Multi Accounts= Multiple API keys.
Remove # to make lines work insert your API key
3. pick or edit this line # if needed and use line below for 10.
4. Range for scanning
I think best 1 api = 1 cpu for my laptop I have 6 API's and run 6CPU
![image](https://user-images.githubusercontent.com/88630056/128767412-710c3f89-ca99-4488-b0a9-d735c0846763.png)


### ethweb3bal.py

![image](https://user-images.githubusercontent.com/88630056/128767587-0c1dbd88-a700-462e-8c45-c9eb9a2cb165.png)

pip3 install colorama
pip3 install web3
pip3 install requests

online Scan looks for ETH
Need to PUT API KEY INTO LINE 17 Replace freekey

### ethweb3.py

![image](https://user-images.githubusercontent.com/88630056/128767691-a58d845a-f5fe-4e3a-9512-9ee570ddf019.png)

pip3 install colorama
pip3 install web3

Offline Scan looks for ETH need to make a ethlist.txt database.

