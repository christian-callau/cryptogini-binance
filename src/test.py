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

test_array = [0, 0, 0]
def main():
	
	client = Client(clients[0]['api_key'], clients[0]['api_secret'])

	symb = 'TRXBTC'
	minQty = 0.01
	
	# print solve_float_error(101.12, 1.0)
	# client.order_limit_buy(symbol='GTOBTC', quantity=152.0, price='0.00000623')

	# print time.localtime(time.time()).tm_year
	# print time.localtime(time.time()).tm_mon
	# print time.localtime(time.time()).tm_mday
	# print time.localtime(time.time()).tm_hour
	# print time.localtime(time.time()).tm_min
	# print time.localtime(time.time()).tm_sec

	for a in range(3):
		t = threading.Thread(target=test1, args=(a,))
		t.start()
	print test_array
	# for client in clients:
	# 	t = threading.Thread(target=buy_pumped_coin, args=('RLCBTC', 8.34, a, Client(client['api_key'], client['api_secret'])))
	# 	t.start()

def test1(position):
	global test_array
	if posit	ion == 1:
		print "hey"
		test_array[position] = 1


if __name__ == '__main__':	
  main()

