import asyncio
from asyncua import Client, ua
import datetime as dt
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.animation as animation


url = "opc.tcp://localhost:4840"
namespace = "CODESYSSPV3/3S/IecVarAccess"

#Parameters
global u 
global ykm1
u = 1
ykm1 = 0
rng = np.random.default_rng()


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = tankFunction(1,5,3)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')


def tankFunction(l,w,h):
    global u
    global ykm1
    y = 0.05*u+ykm1+np.random.normal(0,0.01)
    if y < 0:
        y = 0
        u=1
    elif y > 4:
        y = 4
        u = -1
    ykm1 = y
    yword = round(1029.6576*y)
    if yword > 4096:
        yword = 4096
    elif yword < 1:
        yword = 1
    print(yword)
    return yword


async def main_client():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        #EXAMPLE OF READING VALUE
        #node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL_Modbus.Mb_Tank01_ManualDensity")
        #var = await node.get_value()
        #print(var)
        
        node2 = client.get_node("ns=4;s=|var|Tanksounding_PLC.GVL_Simulation.A02_CH0")
        await node2.write_value(tankFunction(1,1,1), ua.UInt16)

        now = dt.datetime.now()

        



while True:
    asyncio.run(main_client())

    #remove if you want to show live plot. If you plot the values the program does not go out of the plot function again, and does not send values to OPC server..... need to fix this bug.
    #ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000,cache_frame_data=False)
    #plt.show()

    

    