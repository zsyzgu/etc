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

    price = -1
    has_stock = False

    while True:
        data = exchange.readline().strip()
        data = json.loads(data)
        if not data.has_key('type'):
            continue
        try:
			if data['type'] == 'book' and data['symbol'] == 'XLF':
				buy_mess = data['buy']
				sell_mess = data['sell']
				max_buy = 0
				for item in buy_mess:
					max_buy = max(max_buy, item[0])
				min_sell = 1000000000
				for item in sell_mess:
					min_sell = min(min_sell, item[0])
				if price == -1:
					price = (max_buy + min_sell) / 2
					print(say_add(getid(), 'XLF', "SELL", price + 10, 100), file=exchange)
					print(say_add(getid(), 'XLF', "BUY", price - 10, 100), file=exchange)
			if data['type'] == 'fill' and data['symbol'] == 'XLF':
				if data['dir'] == "BUY":
					id = getid()
					print(say_add(id, data['symbol'], "BUY", price + 10, data['size']), file=exchange)
				if data['dir'] == "SELL":
					id = getid()
					print(say_add(id, data['symbol'], "SELL", price - 10, data['size']), file=exchange)
        except:
            traceback.print_exc()

if __name__ == "__main__":
    main()
