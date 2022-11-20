import time
import ttn


app_id = 'hackbackend'
access_key = 'ahosetuhacoreuh943hpb3h'


class TTNHandler:
    def __init__(self):
        self.handler = ttn.HandlerClient(app_id, access_key)

    def mqqt_client(self):
        def uplink_callback(msg, client):
            print("Received uplink from ", msg.dev_id)
            print(msg)

        mqtt_client = self.handler.data()
        mqtt_client.set_uplink_callback(uplink_callback)
        mqtt_client.connect()
        time.sleep(60)
        mqtt_client.close()

    def get_info(self):
        info = {}
        app_client = self.handler.application()
        my_app = app_client.get()
        info['app'] = my_app
        my_devices = app_client.devices()
        info['devices'] = my_devices
        return my_devices

