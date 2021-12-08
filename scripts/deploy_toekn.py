from scripts.helpful_scripts import get_account
from brownie import OurToken
from web3 import Web3


def main():
    initial_value = Web3.toWei(1000, "ether")
    account = get_account()
    toekn = OurToken.deploy(initial_value, {"from": account})
    print(toekn.name())
