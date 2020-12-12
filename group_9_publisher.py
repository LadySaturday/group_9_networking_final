'''
Group 9 - Lab 13
'''
import group_9_util as util
import paho.mqtt.client as mqtt
import json, time
import group_9_data_generator as generator

HOST = 'localhost'
PORT = 8000
TOPIC = 'Group9/lab13'

sampleSize=300
speedometer = generator.Speedometer(500, 50)
speedometer.generate_data()


def init_client():
    # create client and connects to broker
    print(f'[ Pub ]: Initializing client...')
    client = mqtt.Client()
    client.connect(HOST, PORT)
    client.loop_start()
    return client



def main():
    try:
        client = init_client()
        time.sleep(1)
        # Not sure if we have to do more data than just 10 sets
        for i in range(10):
            print(f'\n[ Pub ]: Creating & publishing data... ({i})')
            data = speedometer.create_data() # Creating new data
            client.publish(TOPIC, json.dumps(data)) # Publishing data 
            print(f'[ Pub ]: Sleeping for 3 seconds...')
            time.sleep(3)

        client.loop_stop()
    except Exception:
        print('[ Pub ]: Error occured.')

    print(f'[ Pub ]: Finished.')


if __name__ == '__main__':
    main()
