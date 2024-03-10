import time
import speedtest

speed = speedtest.Speedtest()
print(round(speed.download()))