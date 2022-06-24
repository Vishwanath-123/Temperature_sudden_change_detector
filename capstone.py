import email_conf1
import math
import statistics
from boltiot import Email, Bolt
import json
import time



minimum_limit = 6.64  # the minimum threshold of light value
maximum_limit = 11.1  # the maximum threshold of light value


def compute_bounds(history_data, frame_size, factor):
    if len(history_data) < frame_size:
        return None

    if len(history_data) > frame_size:
        del history_data[0:len(history_data) - frame_size]

        mn = statistics.mean(history_data)
        variance = 0

        for data in history_data:
            variance += math.pow(data - mn, 2)

        z = factor * math.sqrt(variance / frame_size)
        high_bound = history_data[frame_size - 1] + z
        low_bound = history_data[frame_size - 1] - z
        return [high_bound, low_bound]


mybolt = Bolt(email_conf1.API_KEY, email_conf1.DEVICE_ID)
mailer = Email(email_conf1.MAILGUN_API_KEY, email_conf1.SANDBOX_URL,
                email_conf1.SENDER_EMAIL, email_conf1.RECIPIENT_EMAIL)
history_data = []

while True:
    print('Reading sensor value')
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print('Sensor value is: ' + str(data['value']))
    bound = compute_bounds(history_data, email_conf1.FRAME_SIZE,
                           email_conf1.MUL_FACTOR)
    if not bound:
        required_data_count = email_conf1.FRAME_SIZE - len(history_data)
        print ('Not enough data to compute Z-score. Need ',
               required_data_count, ' more data points')
        history_data.append(int(data['value']))
        time.sleep(10)
        continue

    try:
        sensor_value = int(data['value'])
        if sensor_value > bound[0]:
            print('Somebody opened the door.')
            response = mailer.send_email('Alert!','Somebody opened the door.')
            print ('THis is the response', response)
        history_data.append(sensor_value)
    except Exception as e:
        print ('Error', e)
    time.sleep(10)
