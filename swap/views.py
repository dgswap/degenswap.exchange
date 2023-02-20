from flask import Flask, render_template, jsonify, request
from . import app



from swap.backend import swaptoken

@app.route("/",methods=['GET', 'POST'])
def home():

    return render_template("swap.html")

# What happens when our button is clicked
@app.route('/degenswap')
def degenswap():
    #Get the name we want to search for
    rpc = request.args.get('rpc').strip()
    exchange = request.args.get('exchange')
    gaslimit = int(request.args.get('gaslimit'))
    maxFeePerGas = int(request.args.get('maxFeePerGas'))
    maxPriorityFeePerGas = int(request.args.get('maxPriorityFeePerGas'))
    tokencontract = request.args.get('tokencontract').strip()
    publickey = request.args.get('publickey').strip()
    privatekey = request.args.get('privatekey').strip()
    numbereth = float(request.args.get('numbereth'))
    amountoutmin = int(request.args.get('amountoutmin'))
    
    # print(rpc)
    # print(exchange)
    # print(gaslimit)
    # print(maxFeePerGas)
    # print(maxPriorityFeePerGas)
    # print(weth)
    # print(tokencontract)
    # print(publickey)
    # print(privatekey)
    # print(numbereth)
    # print(amountoutmin)

    result = swaptoken.degenswap(rpc, exchange, gaslimit, maxFeePerGas, maxPriorityFeePerGas, tokencontract, publickey, privatekey, numbereth, amountoutmin)
    print (result)
    #Return the json format of the data we scraped
    return jsonify(result = result)