# coding=utf-8
# python3 main.py
import json
import websocket

# 加入和发送函数
def join(username, password, ws_url, channel):
    import json
    import websocket
    global ws
    ws = websocket.WebSocket()
    ws.connect(ws_url)
    ws.send(json.dumps({'cmd': 'join', 'nick': username, 'pass': password, 'channel': channel }))

def send(message):
    import json
    import websocket
    ws.send(json.dumps({'cmd': 'chat', 'text': message}))

def receive():
    import json
    import websocket
    global msg
    global cmd
    global text
    global name
    global trip
    global userid
    global level
    global userhash
    msg = json.loads(ws.recv())
#    print(msg)
    if "cmd" in msg:
        cmd = msg["cmd"]
        if cmd == "chat":
            name = msg['nick']
            text = msg['text']
            trip = msg['trip']
            userid = msg['userid']
            level = msg['level']
        elif cmd == 'onlineAdd':
            userhash = msg['hash']
            name = msg['nick']
            trip = msg['trip']
            userid = msg['userid']
            level = msg['level']

# 功能列表

# join(username, password, ws_url, channel)
# send('(｡･∀･)ﾉﾞHi!')
# 循环判定
# while 1 == 1:
#     receive()
#     if cmd == 'chat':
#         if text == 'a':
#             send('aaa')
