import config, json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def json_loader():
    with open(config.filename, 'r') as f:
        data = json.load(f)

    message_list = data["messages"]

    list = []
    i = 0

    for messages in message_list:
        if(messages["type"] == "message"):
            line_list = messages["text"]
            s = ""
            for lines in line_list:
                if(type(lines) is dict):
                    s += str(lines["text"])
                else:
                    s += lines
            list.append(s)
            i += 1

    print(i, "messages loaded")

    return list


def create_lists(info):
    battery = []
    temp = []
    signal = []
    speed = []
    unix = []
    received = []

    for message in info:
        battery.append(message.split("\n")[4])
        temp.append(message.split("\n")[6])
        signal.append(message.split("\n")[10])
        speed.append(message.split("\n")[18])
        unix.append(message.split("\n")[20])
        received.append(message.split("\n")[22])
    
    return battery, temp, signal, speed, unix, received


def create_png(name, x, date, tag):
    plt.close("all")
    df = pd.DataFrame(x, index=date, columns=tag)
    df = df.cumsum()
    plt.figure();
    plot = df.plot();
    fig = plot.get_figure()
    fig.savefig("./img/" + name + ".png")


def create_battery_graph(battery, temp, unix):
    date = []
    x = []
    pb = 0
    pt = 0.0

    for i in range(0, len(unix)):
        s = temp[i].replace(",", ".")
        b = int(battery[i][:2])
        if(len(s) == 7):
            t = float(s[:4])
        else:
            t = float(s[:2])
        x.append([b-pb, t-pt])
        pb = b
        pt = t
        date.append(datetime.utcfromtimestamp(int(unix[i])).strftime('%Y-%m-%d %H:%M:%S'))
    
    create_png("battery_graph", x, unix, ["%", "°C"])


def create_wifi_graph(signal, unix):
    m = 0
    x = []
    
    for i in range(0, len(signal)):
        n, trash = signal[i].split("d")
        x.append([int(n) - m])
        m = int(n)

    create_png("wifi_graph", x, unix, ["dBm"])
    

def create_position_graph(speed, unix):
    x = []
    s = 0

    for i in range(0, len(speed)):
        km, trash = speed[i].split("k")
        x.append([int(km) - s])
        s = int(km)

    create_png("speed_graph", x, unix, ["km/h"])

    
def create_ping_graph(received, unix):
    import datetime
    import time

    x = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    p = 0
    
    for j in range(0, len(received)):
        month, d, y, trash, tm = received[j][9:].split(" ")
        m = 0

        for i in range(0, 12):
            if(months[i] == month):
                m = i + 1
        
        if(len(d) == 3):
            dd = d[:2]
        else:
            dd = d[:1]

        h, min = tm.split(":")
        mm = min[:2]
        date_time = datetime.datetime(int(y), int(m), int(dd), int(h), int(mm))
        rec = str(time.mktime(date_time.timetuple()))[:10]
        n = int(unix[j]) - int(rec)
        x.append([n-p])
        p = n
    
    create_png("ping_graph", x, unix, ["s"])


def main():
    info = json_loader()
    battery, temp, signal, speed, unix, received = create_lists(info)
    
    create_battery_graph(battery, temp, unix)
    create_wifi_graph(signal, unix)
    create_position_graph(speed, unix)
    create_ping_graph(received, unix)


if __name__ == "__main__":
    main()
