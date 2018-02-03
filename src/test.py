from binance.client import Client
import time
from datetime import datetime
import os
import linecache
import threading
import math
from decimal import *

from api import *

def type_something():
	s = raw_input('> ')

def test():
	print time.time()

def unicode_to_float(string):
	if '.' in string:
		aux = string.split('.')
		decimals = len(aux[1])
		return float(aux[0]) + float(aux[1])/pow(10,len(aux[1]))
	else:
		return float(string)

def solve_float_error(amount, minQty):
	if minQty % 1 < 0:
		getcontext().prec = 28
		number = Decimal(str(amount)).quantize(Decimal(str(minQty)), rounding=ROUND_DOWN)
		return float(number)
	else:
		return amount - amount % minQty

def get_decimals(Qty):
	string = str(Qty)
	return str(Qty)[::-1].find('.')
		

def correct_sell_percentage(sell_amount, minQty):
	count = 0
	len_arr = len(sell_amount)
	for i in range(len_arr-1):
		count += sell_amount[i]
	a = solve_float_error((1 - count), minQty)
	if a != sell_amount[len_arr-1]:
		print "sell percentages were not correctly distributed, new distribution is:"
		sell_amount[len_arr-1] = solve_float_error(a, minQty)
		print sell_amount

def main():
	
	client = Client(clients[0]['api_key'], clients[0]['api_secret'])

	symb = 'TRXBTC'
	minQty = 0.01
	
	print solve_float_error(101.12, 1.0)

	client.order_limit_buy(symbol='GTOBTC', quantity=152.0, price='0.00000623')
	# client.order_market_buy(symbol='TNTBTC', quantity=123.0)
	# client.order_market_sell(symbol='TNTBTC', quantity=123.0)
	# sell_amount = [0.4, 0.4, 0.2] #Max 4 decimals
	# actual_price = 0.00001
	# price_amounts = [1.2, 1.3, 1.4]
	# amount = 2477.12

	# if len(sell_amount) != len(price_amounts):
	# 	price_amounts = price_amounts[0]*len(sell_amount)
		
	# correct_sell_percentage(sell_amount, 0.0001)

	# num_of_orders = len(sell_amount)
	# order_amounts = [0.0]*num_of_orders
	# amount_left = amount

	# for order in range(num_of_orders-1, -1, -1):
	# 	if order != 0:
	# 		amount_to_add = solve_float_error(amount * sell_amount[order], minQty)
	# 		order_amounts[order] = amount_to_add
	# 		amount_left -= amount_to_add
	# 	else:
	# 		order_amounts[0] = solve_float_error(amount_left, minQty)

	# print order_amounts

	# count = 0
	# for i in range(num_of_orders):
	# 	count += order_amounts[i]
	# if solve_float_error(count, minQty) !=  amount:
	# 	print "amount was not correctly distributed"
	# 	print count, amount




	# print time.localtime(time.time()).tm_year
	# print time.localtime(time.time()).tm_mon
	# print time.localtime(time.time()).tm_mday
	# print time.localtime(time.time()).tm_hour
	# print time.localtime(time.time()).tm_min
	# print time.localtime(time.time()).tm_sec


	# for client in clients:
	# 	t = threading.Thread(target=buy_pumped_coin, args=('RLCBTC', 8.34, a, Client(client['api_key'], client['api_secret'])))
	# 	t.start()

	# ids = []
	# for order in range(num_of_orders):
	# 	id_num = client.order_limit_sell(symbol=symb, quantity=order_amounts[order], price=price_amounts[order])['orderId']
	# 	ids.append(id_num)
	# # cancel_limit(client, symb, ids[1])
	# raw_input('> Press enter to cancell orders and market sell')
	# all_t = []

	# for order in range(num_of_orders):
	# 	t = threading.Thread(target=cancel_limit, args=(client, symb, ids[order]))
	# 	t.start()
	# 	all_t.append(t)

	# for thr in all_t:
	# 	thr.join()
	# print time.time()

def cancel_limit(client, symb, id_num):
	try:
		client.cancel_order(symbol=symb, orderId=id_num)
	except:
		print "sell Limit was already canceled"
if __name__ == '__main__':	
  main()

