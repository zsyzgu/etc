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
	price_XLF = -1
	first_XLF = 1
	po_XLF = 0
	#price_WFC = -1
	#first_WFC = 1
	#po_WFC = 0
	#price_GS = -1
	#first_GS = 1
	#po_GS = 0
	#price_MS = -1
	#first_MS = 1
	#po_MS = 0

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
				max_buy = 0
				max_buy_a = 0
				max_buy2 = 0
				for item in buy_mess:
					if (item[0] > max_buy2):
						max_buy2 = item[0]
						if max_buy2 > max_buy:
							tmp = max_buy2:
							max_buy2 = max_buy
							max_buy = tmp
							max_buy_a = item[1]
				max_buy_a = min(max_buy_a, amou)
				if max_buy - max_buy2 > 1:
					print(say_add(getid(), 'XLF', "BUY", max_buy2 + 1, max_buy_a), file=exchange)
					print(say_add(getid(), 'XLF', "SELL", max_buy, max_buy_a), file=exchange)
				
				sell_mess = data['sell']
				#min_sell = 1000000000
				#for item in sell_mess:
				#	min_sell = min(min_sell, item[0])
				#if max_buy != 0 and min_sell != 1000000000:
				#	price_XLF = (max_buy + min_sell) / 2
				#if first_XLF == 1:
				#	first_XLF = 0
				#	print(say_add(getid(), 'XLF', "SELL", price_XLF + diff, amou), file=exchange)
				#	print(say_add(getid(), 'XLF', "BUY", price_XLF - diff, amou), file=exchange)
			#if data['type'] == 'fill' and data['symbol'] == 'XLF':
			#	if data['dir'] == "BUY":
			#		id = getid()
			#		print(say_add(id, data['symbol'], "BUY", price_XLF - diff, data['size']), file=exchange)
			#	if data['dir'] == "SELL":
			#		id = getid()
			#		print(say_add(id, data['symbol'], "SELL", price_XLF + diff, data['size']), file=exchange)

		except:
			traceback.print_exc()

if __name__ == "__main__":
	main()
