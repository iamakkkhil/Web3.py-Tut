import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Connect to infura.io project
infura_url = os.getenv("INFURA_URL")
w3 = Web3(Web3.HTTPProvider(infura_url))

if w3.isConnected():
    print("Connected successfully to Infura.io")
    blockNumber = w3.eth.block_number
    print("Current block number: ", blockNumber)

    balance = w3.eth.getBalance("0xFfdc2bb0106Cb487ac8937ec68b875d087aD631F")
    print("Current Balance: ", balance)
else:
    print("Not connected to Infura.io")
