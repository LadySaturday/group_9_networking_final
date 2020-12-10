'''
Group 9 - Lab 13
'''
import group_9_util as util#data sent from publisher
import paho.mqtt.client as mqtt
import json

import threading
import group_9_dynamic_displayog as graph #graph.changeList() needs to be called whenever publisher publishes data

HOST = 'localhost'
PORT = 8000
TOPIC = 'Group9/lab13'

display = graph.DynamicDisplayOG()

queue = []


def update_graph():
    print("received something")
    speed = queue.pop(0)
    # value = data['data']['speed']
    display.add_value(speed)

def on_message(c, usrdata, msg):
    print(f'\n[ Sub ]: Decoding message from publisher...')
    payload = msg.payload.decode('utf-8')
    data = json.loads(payload)
    util.print_data(data)
    queue.append(data['data']['speed'])
    display.set_list(queue)
    # Decode payload and print using print_data
    # t = threading.Thread(target=update_graph, daemon=True)
    # t.start()
    # update_graph(data)
   


def init_client():
    print(f'[ Sub ]: Initializing client...')
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(HOST, PORT)
    
    return client

def main():
    t = threading.Thread(target=listen, daemon=True)
    t.start()
    display.start()
    print('SUB >> after display start')

def listen():
    try:
        client = init_client()
        print(f'[ Sub ]: Subscribing to broker...')
        # connects/subs to Broker
        client.subscribe(TOPIC)
        print(f'[ Sub ]: Looping forever...')
        
        while True:
            client.loop_forever()
    except Exception as e:
        print(f'[ Sub ]: !!! Error !!! \n{e}')

    print(f'[ Sub ]: Finished.')


if __name__ == '__main__':
    main()
    
