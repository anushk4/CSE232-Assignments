# Reference: https://github.com/aflah02/CN_Assignments/blob/main/Assignment%203/Q1/queue_plotter.py

import matplotlib.pyplot as plt
import re

def read_file(filename):
    f = open(filename, "r")
    content = f.readlines()
    f.close()
    return content
    
def process_delay():
    content = read_file("tcp-example.tr")
    enqueue = {}
    x = []
    y = []
    for i in content:
        match = re.search(r"Seq=(\d+)", i)
        packet_id = -1
        if match:
            packet_id = match.group(1)
        i = i.split()
        if packet_id == -1:
            continue
        if i[0] == '+':
            enqueue[packet_id] = float(i[1])
        elif i[0] == '-':
            delay = float(i[1]) - enqueue[packet_id]
            x.append(float(i[1]))
            y.append(delay)
    return x, y

def plot_graph():
    x, y = process_delay()
    plt.plot(x, y)
    plt.xlabel("Time in seconds")
    plt.ylabel("Queuing delay in seconds")
    plt.savefig('queueing_delay.eps', format='eps')
        
plot_graph()
