from app import app
from flask import render_template, request, Response

import atexit
import numpy as np
import matplotlib.pyplot as plt
import base64

from digi.xbee.devices import XBeeDevice
from io import BytesIO

plt.style.use('dark_background')
plt.rcParams['axes.facecolor'] = '#202125'
plt.rcParams['figure.facecolor'] = '#16171B'

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
REMOTE_NODE_ID = "ROUTER"

device = None
remote_device = None

from collections import namedtuple

Telemetry = namedtuple('Telemetry', ['team_id', 'time', 'packet',
                                     'voltage',
                                     'altitude',
                                     'velocity',
                                     'lat',
                                     'lon',
                                     'took_photo',
                                     'rpm_a',
                                     'rpm_b',
                                     'rpm_c',
                                     'rpm_d',
                                     'stage',
                                     'took_photos',
                                     'send_photos'])

xbee_data = []

import csv

csv_fp = None
csv_writer = None

import time

@app.before_first_request
def setup_xbee():
    global device
    global remote_device

    device = XBeeDevice(PORT, BAUD_RATE)
    device.open()
    xbee_network = device.get_network()
    remote_device = xbee_network.discover_device(REMOTE_NODE_ID)

    while not remote_device:
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)

    device.add_data_received_callback(xbee_callback)

    global csv_fp
    global csv_writer

    csv_fp = open('6165_TLM_2020_' + str(time.time()) + '.csv', 'w')
    csv_writer = csv.writer(csv_fp)


def xbee_callback(xbee_message):
    data = xbee_message.data.decode()

    print(eval(data))
    csv_writer.writerow(eval(data))
    csv_fp.flush()

    tele = Telemetry(*eval(data))
    xbee_data.append(tele)


def plot():
    fig, axs = plt.subplots(2, 1, figsize=(9, 6.3), dpi=70)

    time = list(map(lambda row: float(row.time), xbee_data))
    alt = list(map(lambda row: float(row.altitude), xbee_data))
    velocity = list(map(lambda row: float(row.velocity), xbee_data))

    x = np.linspace(0, 4, 300)
    axs[0].plot(time, alt)
    axs[1].plot(time, velocity)
    # axs[1, 1].plot(x, 10 * np.exp(-x) + np.random.random(x.shape) * 0.5)
    # axs[0, 1].matshow(plt.imread("app/img.jpg", format='jpg'), aspect='auto')

    axs[0].set_title('Altitude (m)')
    axs[1].set_title('Velocity (m/s)')
    # axs[1, 1].set_title('Pressure (kPa)')
    # axs[3].set_title('Speed (m/s)')

    for ax in axs.flatten():
        ax.grid(True, linestyle='--', linewidth=0.5, color='#938572')
        ax.grid(False, axis='x')

    plt.tight_layout()

    figbin = BytesIO()
    plt.savefig(figbin, format='png', facecolor=fig.get_facecolor())
    figbin.seek(0)

    figdata_png = base64.b64encode(figbin.getvalue())

    return figdata_png.decode('utf8')


@app.route('/api/serial', methods=['POST'])
def serial():
    print(xbee_data)
    # xbee_data.append(Telemetry(*([0] * 16)))
    command = request.json['command']

    if command == 'reset':
        xbee_data.clear()

    device.send_data_async(remote_device, command)

    return Response(status=200)


@app.route('/')
def index():
    plots = {
        'speed': plot()
    }

    return render_template('index.html', plots=plots, data=xbee_data[::-1])


def close_serial():
    if csv_fp:
        csv_fp.close()

    if device:
        device.close()


atexit.register(close_serial)
