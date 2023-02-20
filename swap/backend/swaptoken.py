import json
from web3 import Web3
import time
from swap.backend.route_config import ethereum_uniswap
from swap.backend.route_config import arbitrum_sushiswap
from swap.backend.route_config import ethereum_sushiswap

def degenswap(rpc, exchange, gaslimit, maxFeePerGas, maxPriorityFeePerGas, tokencontract, publickey, privatekey, numbereth, amountoutmin):

    w3 = Web3(Web3.HTTPProvider(rpc))
    token = w3.toChecksumAddress(tokencontract)
    nonce = w3.eth.get_transaction_count(publickey)

    if exchange == "Ethereum_Uniswapv2Route":
        weth = w3.toChecksumAddress(ethereum_uniswap.weth_contract)
        univ2route = w3.toChecksumAddress(ethereum_uniswap.univ2_route_contract)
        contract = w3.eth.contract(address=univ2route, abi=ethereum_uniswap.abi)
        uniswap_v2_tx = contract.functions.swapExactETHForTokens(
            amountoutmin,  # amountoutmin
            [weth, token],
            publickey,
            (int(time.time()) + 3600)
        ).buildTransaction({
            'from': publickey,
            'value': w3.toWei(numbereth, 'ether'),
            'gas': gaslimit,  # net current gas limit
            'maxFeePerGas': w3.toWei(maxFeePerGas, 'gwei'),
            'maxPriorityFeePerGas': w3.toWei(maxPriorityFeePerGas, 'gwei'),
            'nonce': nonce,
        })
    elif exchange == "Arbitrum_Sushiv2Route":
        weth = w3.toChecksumAddress(arbitrum_sushiswap.weth_contract)
        univ2route = w3.toChecksumAddress(arbitrum_sushiswap.sushiv2_route_contract)
        contract = w3.eth.contract(address=univ2route, abi=arbitrum_sushiswap.abi)
        uniswap_v2_tx = contract.functions.swapExactETHForTokens(
            amountoutmin,  # amountoutmin
            [weth, token],
            publickey,
            (int(time.time()) + 3600)
        ).buildTransaction({
            'from': publickey,
            'value': w3.toWei(numbereth, 'ether'),
            'gas': gaslimit,  # net current gas limit
            'gasPrice': w3.toWei(maxFeePerGas,'gwei'),
            'nonce': nonce,
        })
    elif exchange == "Ethereum_Sushiv2Route":
        weth = w3.toChecksumAddress(ethereum_sushiswap.weth_contract)
        univ2route = w3.toChecksumAddress(ethereum_sushiswap.sushi_v2_route_contract)
        contract = w3.eth.contract(address=univ2route, abi=ethereum_sushiswap.abi)
        uniswap_v2_tx = contract.functions.swapExactETHForTokens(
            amountoutmin,  # amountoutmin
            [weth, token],
            publickey,
            (int(time.time()) + 3600)
        ).buildTransaction({
            'from': publickey,
            'value': w3.toWei(numbereth, 'ether'),
            'gas': gaslimit,  # net current gas limit
            'maxFeePerGas': w3.toWei(maxFeePerGas, 'gwei'),
            'maxPriorityFeePerGas': w3.toWei(maxPriorityFeePerGas, 'gwei'),
            'nonce': nonce,
        })
    else:
        return "Swap False"

    signed_txn = w3.eth.account.sign_transaction(
    uniswap_v2_tx, private_key=privatekey)
    tx_token = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return str(w3.toHex(tx_token))


