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
	s.connect(("test-exch-westernjindynasty", 25000))
	return s.makefile('w+', 1)

def main():
	exchange = connect()
	print(say_hello("ZSYZGU"), file=exchange)

	diff = 5
	amou = 5
	dd = 5
	price_XLF = -1
	first_XLF = 1
	buy_XLF = 0
	sell_XLF = 0
	price_WFC = -1
	first_WFC = 1
	price_GS = -1
	first_GS = 1
	price_MS = -1
	first_MS = 1

	while True:
		data = exchange.readline().strip()
		data = json.loads(data)
		if not data.has_key('type'):
			continue
		try:
			if data['type'] == 'book' and data['symbol'] == 'XLF':
				buy_mess = data['buy']
				max_buy = 0
				max_buy_a = 0
				max_buy2 = 0
				for item in buy_mess:
					if (item[0] > max_buy2):
						max_buy2 = item[0]
						if max_buy2 > max_buy:
							tmp = max_buy2
							max_buy2 = max_buy
							max_buy = tmp
							max_buy_a = item[1]
				max_buy_a = min(max_buy_a, amou)
				if max_buy - max_buy2 > dd and max_buy != buy_XLF:
					buy_XLF = max_buy
					print(say_add(getid(), 'XLF', "BUY", max_buy2 + 1, max_buy_a), file=exchange)
					print(say_add(getid(), 'XLF', "SELL", max_buy, max_buy_a), file=exchange)
				
				sell_mess = data['sell']
				min_sell = 1000000000
				min_sell_a = 0
				min_sell2 = 1000000000
				for item in sell_mess:
					if (item[0] < min_sell2):
						min_sell2 = item[0]
						if min_sell2 < min_sell:
							tmp = min_sell2
							min_sell2 = min_sell
							min_sell = tmp
							min_sell_a = item[1]
				min_sell_a = min(min_sell_a, amou)
				if min_sell2 - min_sell > dd and min_sell != sell_XLF:
					sell_XLF = min_sell
					print(say_add(getid(), 'XLF', "BUY", min_sell, max_buy_a), file=exchange)
					print(say_add(getid(), 'XLF', "SELL", min_sell2 - 1, max_buy_a), file=exchange)
		except:
			traceback.print_exc()

if __name__ == "__main__":
	main()
