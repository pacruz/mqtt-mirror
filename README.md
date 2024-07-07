mqtt-mirror
====

Rough one-way mqtt mirror.  Subscribes to message on source broker and sends them to destination broker.

Dependencies
------------
 - paho-mqtt 2.1.0: https://pypi.org/project/paho-mqtt/2.1.0/
 - Python 3.11.9: https://python.org/

Run flags
---------
```
Usage: python ./mqtt-mirror.py [options]

--source-broker <source-broker>
--source-username <source-username>
--source-password <source-password>
--source-topic <source-topic>
--destination-broker <destination-broker>
--destination-username <destination-username>
--destination-password <destination-password>
--destination-topic <destination-topic>
--destination-port <destination-port>
```

Docker configuration
--------------------

To build the mqtt-mirror app into a docker image:

```
docker build -t pacruz-mqtt-mirror .
```

To (optionally) export the image as a tar:

```
docker save pacruz-mqtt-mirror > pacruz-mqtt-mirror.tar
```

To run the container with docker compose, the following compose file should work

```
services:
  mqtt-mirror:
    image: pacruz-mqtt-mirror
    container_name: pacruz-mqtt-mirror
    environment:
      SOURCE_BROKER: "<ip_address>"
      SOURCE_USERNAME: "<username>"
      SOURCE_PASSWORD: "<password>"
      SOURCE_TOPIC: "<some_topic>"
      SOURCE_PORT: 1883
      DESTINATION_BROKER: "<ip_address>"
      DESTINATION_USERNAME: "<username>"
      DESTINATION_PASSWORD: "<password>"
      DESTINATION_TOPIC: "<some_topic>"
      DESTINATION_PORT: 1883
    restart: unless-stopped
```

Then run 
```
docker compose up -d
```

Copyright
---------

2024 <pacruz@pacruz.com>
