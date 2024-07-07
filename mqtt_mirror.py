import argparse, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    print(args.source_topic)
    client.subscribe(args.source_topic)

def on_message(client, userdata, msg):
    base_topic = args.source_topic
    if base_topic.endswith("#"):
        base_topic = base_topic[:-1]
    
    dest_topic = msg.topic.replace(base_topic,args.destination_topic)
    mqtt_internal.publish(dest_topic,msg.payload)

parser = argparse.ArgumentParser()
parser.add_argument("--source-broker", help = "Source broker IP/Hostname")
parser.add_argument("--source-username", help="Source broker username")
parser.add_argument("--source-password", help="Source broker password")
parser.add_argument("--source-port", help="Source broker port", default=1883)
parser.add_argument("--source-topic",help="Topic to listen to on source broker")

parser.add_argument("--destination-broker", help = "Destination broker IP/Hostname")
parser.add_argument("--destination-username", help="Destination broker username")
parser.add_argument("--destination-password", help="Destination broker password")
parser.add_argument("--destination-port", help="Destination broker port", default=1883)
parser.add_argument("--destination-topic", help="Topic to publish to on destination broker")

args = parser.parse_args()

if (args.destination_broker is None):
    sys.exit("--destination--broker is required")
if (args.destination_username is None):
    sys.exit("--destination-username is required")
if (args.destination_password is None):
    sys.exit("--destination-password is required")
if (args.destination_topic is None):
    sys.exit("--destination-topic is required")
if (args.source_broker is None):
    sys.exit("--source--broker is required")
if (args.source_username is None):
    sys.exit("--source-username is required")
if (args.source_password is None):
    sys.exit("--destination-password is required")
if (args.source_topic is None):
    sys.exit("--source-topic is required")

mqtt_internal = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_internal.username_pw_set(username=args.destination_username, password=args.destination_password)
mqtt_internal.connect(args.destination_broker,args.destination_port,60)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.username_pw_set(username=args.source_username, password=args.source_password)
mqttc.connect(args.source_broker, args.source_port, 60)

mqttc.loop_forever()
