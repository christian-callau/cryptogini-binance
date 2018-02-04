from binance.client import Client
import time
from datetime import datetime
import os
import linecache
import threading
import math
from decimal import *

from api import *

def main():
	
	client = Client(clients[0]['api_key'], clients[0]['api_secret'])

	
	# print solve_float_error(101.12, 1.0)
	# client.order_limit_buy(symbol='GTOBTC', quantity=152.0, price='0.00000623')

	# print time.localtime(time.time()).tm_year
	# print time.localtime(time.time()).tm_mon
	# print time.localtime(time.time()).tm_mday
	# print time.localtime(time.time()).tm_hour
	# print time.localtime(time.time()).tm_min
	# print time.localtime(time.time()).tm_sec

	# for client in clients:
	# 	t = threading.Thread(target=buy_pumped_coin, args=('RLCBTC', 8.34, a, Client(client['api_key'], client['api_secret'])))
	# 	t.start()


if __name__ == '__main__':	
  main()

