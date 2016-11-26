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

	price_XLF = -1
	po_XLF = 0
	price_WFC = -1
	po_WFC = 0

	while True:
		data = exchange.readline().strip()
		data = json.loads(data)
		if not data.has_key('type'):
			continue
		try:
			if data['type'] == 'hello':
				sym = data['symbols']
				for item in sym:
					if item["symbol"] == "XLF":
						po_XLF = int(item["position"])
			if data['type'] == 'book' and data['symbol'] == 'XLF':
				buy_mess = data['buy']
				sell_mess = data['sell']
				max_buy = 0
				for item in buy_mess:
					max_buy = max(max_buy, item[0])
				min_sell = 1000000000
				for item in sell_mess:
					min_sell = min(min_sell, item[0])
				if price_XLF == -1:
					price_XLF = (max_buy + min_sell) / 2
					sell_num = 50
					buy_num = 50
					if po_XLF > 0:
						buy_num = 50 - po_XLF
					else:
						sell_num = 50 + po_XLF
					print(say_add(getid(), 'XLF', "SELL", price_XLF + 10, sell_num), file=exchange)
					print(say_add(getid(), 'XLF', "BUY", price_XLF - 10, buy_num), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'XLF':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price_XLF - 10, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price_XLF + 10, data['size']), file=exchange)
		except:
			traceback.print_exc()

if __name__ == "__main__":
	main()
