from app import app
from flask import render_template

import numpy as np
import matplotlib.pyplot as plt
import base64

plt.style.use('dark_background')
plt.rcParams['axes.facecolor'] = '#202125'
plt.rcParams['figure.facecolor'] = '#16171B'

from io import BytesIO

def plot():
    fig, axs = plt.subplots(2, 2, figsize=(9,6.3), dpi=70)

    x = np.linspace(0, 4, 300)
    axs[0, 0].plot(x, np.exp(x) + np.random.random(x.shape) * 5)
    # axs[1].plot(x, np.exp(-x) + np.random.random(x.shape) * 0.01)
    axs[1, 0].plot(x, 101 * np.exp(-x) + np.random.random(x.shape) * 11)
    axs[1, 1].plot(x, 10 * np.exp(-x) + np.random.random(x.shape) * 0.5)
    axs[0, 1].matshow(plt.imread("app/img.jpg", format='jpg'), aspect='auto')

    axs[0, 0].set_title('Altitude (m)')
    axs[1, 0].set_title('Speed (m/s)')
    axs[1, 1].set_title('Pressure (kPa)')
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

@app.route('/')
def index():
    plots = {
        'speed': plot()
    }

    return render_template('index.html', plots=plots)
