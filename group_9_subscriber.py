'''
Group 9 - Lab 13
'''
import group_9_util as util#data sent from publisher
import paho.mqtt.client as mqtt
import json

import threading
import group_9_dynamic_display as graph #graph.changeList() needs to be called whenever publisher publishes data

HOST = 'localhost'
PORT = 8000
TOPIC = 'Group9/lab13'


def on_message(c, usrdata, msg):
    print(f'\n[ Sub ]: Decoding message from publisher...')

    # Decode payload and print using print_data
    payload = msg.payload.decode('utf-8')
    data = json.loads(payload)
    util.print_data(data)
    graph.changeList()
   


def init_client():
    print(f'[ Sub ]: Initializing client...')
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(HOST, PORT)
    
    return client

def main():
    try:
        client = init_client()
        print(f'[ Sub ]: Subscribing to broker...')
        # connects/subs to Broker
        client.subscribe(TOPIC)
        print(f'[ Sub ]: Looping forever...')
        
        while True:
            client.loop_forever()
    except Exception:
        print('[ Sub ]: Error occured.')

    print(f'[ Sub ]: Finished.')


if __name__ == '__main__':
    main()
    
