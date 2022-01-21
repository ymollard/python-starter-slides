#!/usr/bin/env python

from argparse import ArgumentParser
from subprocess import Popen, PIPE
from matplotlib import pyplot
import numpy

parser = ArgumentParser(description="Draw a plot of ping delays to a host")
parser.add_argument('--host', type=str, help='the host to ping', default="baidu.com")
parser.add_argument('--iterations', type=int, help='number of pings', default=50)
args = parser.parse_args()

durations = []

print("Ping measurement in progress, please wait while the {} pings are over...".format(args.iterations))
with Popen(["ping", args.host], stdout=PIPE) as ping:
    for i in range(args.iterations):
        line = ping.stdout.readline().decode("utf8")
        try:
            _, _, server, ip, icmp_seq, ttl, time = line.split(" ")
        except ValueError:
            # ValueError is raised if this ping lined is not formatted as expected, maybe the ping failed
            print("Ping failure :(")
            continue
        try:
            time_sec = float(time.split("=")[-1].split("\xa0")[0])
        except ValueError:
            # This line has not ping time in millisec, maybe this is a header/footer line, just ignore it
            continue
        durations.append(time_sec)

mean = numpy.mean(durations)
std = numpy.std(durations)

x_axis = range(len(durations))

# Plot all durations
pyplot.plot(x_axis, durations, color="red")

# Plot the mean (dashed --)
pyplot.plot([0, x_axis[-1]], [mean, mean], "--", color="red")

# Plot the stdev
pyplot.fill_between([0, x_axis[-1]], mean - std, mean + std,
                    color='red', alpha=0.1, label="std")

y_min = 0.95*min(durations)
y_max = 1.02*max(durations)

pyplot.xlabel("Iterations")
pyplot.xticks(x_axis)
pyplot.ylabel("Delay (ms)")
pyplot.yticks([y_min, y_max])
pyplot.ylim([y_min, y_max])
pyplot.title("Ping statistics for {}".format(args.host))
pyplot.show()

