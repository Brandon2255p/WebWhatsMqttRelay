import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message, MediaMessage, NotificationMessage
from message_distributor import MessageDistributor
import json
import os
MQTT_SERVER = os.environ["MQTT_SERVER"]
MQTT_PORT = os.environ["MQTT_PORT"]
MQTT_USER = os.environ["MQTT_USER"]
MQTT_PASS = os.environ["MQTT_PASS"]

distributor = MessageDistributor()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(self, client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    self.subscribe("outgoing/")
    self.subscribe("assign/")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
    if(msg.topic == "assign/"):
        print("Assigning user")
        parsed_json = json.loads(msg.payload)
        agent_id = parsed_json["agent_id"].encode("utf-8")
        chat_id = parsed_json["chat_id"].encode("utf-8")
        assigner.assign_chat(agent_id, chat_id);
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("rbpzxiof", "mY5QlIiDUZQD")
client.connect("m11.cloudmqtt.com", 18211, 60)

driver = WhatsAPIDriver(profile = "/home/user/.mozilla/firefox/mwad0hks.default")
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

chat = driver.get_chat_from_phone_number("27837548664")
print(chat.name)
print(chat.id)
#chat.load_earlier_messages()

    

print(assigner.get_agent_id("hello"))
print(assigner.get_agent_id(chat.id))

for message in chat.get_messages(include_notifications=True, include_me=True):
    topic = "brandon/{}".format(chat.id)
    print(topic)
    if not isinstance(message, MediaMessage):
        payload = "{}: {}".format(message.sender.get_safe_name(), message.content.encode('utf-8').strip())
        client.publish(topic, payload)
    else:
        distributor.

print("Looping")
client.loop_start();

assigner.close();
#status = driver.get_status();
#print(status)
#
#for chat in driver.get_all_chats():
#    for message in chat.get_messages():
#        topic = "brandon/{}".format(chat.id)
#        payload = "MSG: {}".format(message)
#        print(topic)
#        print(payload)
#        client.publish(topic, payload)
while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        for message in contact.messages:
            print(message)




