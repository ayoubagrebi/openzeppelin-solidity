from web3 import web3
import json


def loadAbi (abi) :
    return json.load(open("./abis/%s"%(abi)))

def getContractInstance(adress,abiFile):
    return w3.eth.contract(adress, abi=loadAbi(abiFile))

   def liquidate(user, liquidator, amount):

  allowance = dai.functions.allowance(user, lendingPool.address).call()


  if allowance <= 0:
    tx = dai.functions.approve(lendingPool.address, amount).transact({
      "from": liquidator,
    })    
      lendingPool.functions.liquidationCall(
    weth.address,
    dai.address,
    user,
    amount,
    True
  ).transact({"from": liquidator})
  