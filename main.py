#!/usr/bin/python
from __future__ import print_function

import traceback
import sys
import socket
from utility import *
import json

id = 0
def getid():
	global id
	id += 1
	return id

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s.connect(("test-exch-westernjindynasty", 25000))
	s.connect(("production", 25000))
	return s.makefile('w+', 1)

def main():
	exchange = connect()
	#print(say_hello("ZSYZGU"), file=exchange)
	print(say_hello("WESTERNJINDYNASTY"), file=exchange)

	last_buy = 0
	last_sell = 0
	last_diff = 0

	while True:
		data = exchange.readline().strip()
		data = json.loads(data)
		if not data.has_key('type'):
			continue
		try:
			if data['type'] == 'reject':
				print(data['error'])

			if data['type'] == 'book' and data['symbol'] == 'XLF':
				buy_mess = data['buy']
				max_buy = 0
				for item in buy_mess:
					if (item[0] > max_buy):
						max_buy = item[0]
				
				sell_mess = data['sell']
				min_sell = 1000000000
				for item in sell_mess:
					if (item[0] < min_sell):
						min_sell = item[0]
				
				if min_sell - max_buy > 10 and max_buy != 0 and min_sell != 1000000000:
					this_buy = max_buy + 1
					if this_buy != last_buy and this_buy != last_buy + 1:
						print('BUY')
						last_buy = max_buy + 1
						print(say_add(getid(), 'XLF', "BUY", this_buy, 1), file=exchange)
					this_sell = min_sell - 1
					if this_sell != last_sell and this_sell != last_sell - 1:
						print('SELL')
						last_sell = this_sell
						print(say_add(getid(), 'XLF', "SELL", this_sell, 1), file=exchange)

		except:
			traceback.print_exc()

if __name__ == "__main__":
	main()
