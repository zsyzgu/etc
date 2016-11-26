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
	price_GS = -1
	po_GS = 0
	price_MS = -1
	po_MS = 0

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
					print(say_add(getid(), 'XLF', "SELL", price_XLF + 20, sell_num), file=exchange)
					print(say_add(getid(), 'XLF', "BUY", price_XLF - 20, buy_num), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'XLF':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price_XLF - 20, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price_XLF + 20, data['size']), file=exchange)

			if data['type'] == 'hello':
				sym = data['symbols']
				for item in sym:
					if item["symbol"] == "WFC":
						po_WFC = int(item["position"])
			if data['type'] == 'book' and data['symbol'] == 'WFC':
				buy_mess = data['buy']
				sell_mess = data['sell']
				max_buy = 0
				for item in buy_mess:
					max_buy = max(max_buy, item[0])
				min_sell = 1000000000
				for item in sell_mess:
					min_sell = min(min_sell, item[0])
				if price_WFC == -1:
					price_WFC = (max_buy + min_sell) / 2
					sell_num = 50
					buy_num = 50
					if po_WFC > 0:
						buy_num = 50 - po_WFC
					else:
						sell_num = 50 + po_WFC
					print(say_add(getid(), 'WFC', "SELL", price_WFC + 20, sell_num), file=exchange)
					print(say_add(getid(), 'WFC', "BUY", price_WFC - 20, buy_num), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'WFC':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price_WFC - 20, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price_WFC + 20, data['size']), file=exchange)

			if data['type'] == 'hello':
				sym = data['symbols']
				for item in sym:
					if item["symbol"] == "GS":
						po_GS = int(item["position"])
			if data['type'] == 'book' and data['symbol'] == 'GS':
				buy_mess = data['buy']
				sell_mess = data['sell']
				max_buy = 0
				for item in buy_mess:
					max_buy = max(max_buy, item[0])
				min_sell = 1000000000
				for item in sell_mess:
					min_sell = min(min_sell, item[0])
				if price_GS == -1:
					price_GS = (max_buy + min_sell) / 2
					sell_num = 50
					buy_num = 50
					if po_GS > 0:
						buy_num = 50 - po_GS
					else:
						sell_num = 50 + po_GS
					print(say_add(getid(), 'GS', "SELL", price_GS + 20, sell_num), file=exchange)
					print(say_add(getid(), 'GS', "BUY", price_GS - 20, buy_num), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'GS':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price_GS - 20, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price_GS + 20, data['size']), file=exchange)

			if data['type'] == 'hello':
				sym = data['symbols']
				for item in sym:
					if item["symbol"] == "MS":
						po_MS = int(item["position"])
			if data['type'] == 'book' and data['symbol'] == 'MS':
				buy_mess = data['buy']
				sell_mess = data['sell']
				max_buy = 0
				for item in buy_mess:
					max_buy = max(max_buy, item[0])
				min_sell = 1000000000
				for item in sell_mess:
					min_sell = min(min_sell, item[0])
				if price_MS == -1:
					price_MS = (max_buy + min_sell) / 2
					sell_num = 50
					buy_num = 50
					if po_MS > 0:
						buy_num = 50 - po_MS
					else:
						sell_num = 50 + po_MS
					print(say_add(getid(), 'MS', "SELL", price_MS + 20, sell_num), file=exchange)
					print(say_add(getid(), 'MS', "BUY", price_MS - 20, buy_num), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'MS':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price_MS - 20, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price_MS + 20, data['size']), file=exchange)
		except:
			traceback.print_exc()

if __name__ == "__main__":
	main()
