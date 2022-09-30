from datetime import datetime
from re import M
import time
import datetime as dt

def count_down(h, m, s):
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        timer = dt.timedelta(seconds = total_seconds)

        print(timer, end="\r")

        time.sleep(1)

        total_seconds -=1

    print("contagem finalizada!")

h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
count_down(int(h),int(m), int(s))