FROM python:3.11.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY mqtt_mirror.py .
CMD python3 mqtt_mirror.py --source-broker $SOURCE_BROKER --source-username $SOURCE_USERNAME --source-password $SOURCE_PASSWORD --source-topic $SOURCE_TOPIC --source-port $SOURCE_PORT --destination-broker $DESTINATION_BROKER --destination-username $DESTINATION_USERNAME --destination-password $DESTINATION_PASSWORD --destination-topic $DESTINATION_TOPIC --destination-port $DESTINATION_PORT
