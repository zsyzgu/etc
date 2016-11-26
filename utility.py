import json

def say_hello(team):
    return json.dumps({"type": "hello", "team": team})

def say_add(order_id, symbol, dir, price, size):
    return json.dumps({"type": "add", "order_id": order_id, "symbol": symbol, "dir": dir, "price": price, "size": size})

def say_convert(order_id, symbol, dir, size):
    return json.dumps({"type": "convert", "order_id": order_id, "symbol": symbol, "dir": dir, "size": size})

def say_cancel(order_id):
    return json.dumps({"type": "cancel", "order_id": order_id})
