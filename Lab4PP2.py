import math
import datetime

def squares_up_to(n):
    result = []
    for i in range(n + 1):
        result.append(i * i)
    return result

def even_numbers_list(n):
    result = []
    for x in range(0, n + 1, 2):
        result.append(x)
    return result
    
def divisible_by_3_and_4(n):
    result = []
    for x in range(0, n + 1):
        if x % 3 == 0 and x % 4 == 0:
            result.append(x)
    return result

def squares_range(a, b):
    result = []
    for x in range(a, b + 1):
        result.append(x * x)
    return result

def countdown(n):
    result = []
    for x in range(n, -1, -1):
        result.append(x)
    return result


today = datetime.datetime.now().date()
five_days_ago = today - datetime.timedelta(days=5)
print("Today:", today)
print("Five days ago:", five_days_ago)

today = datetime.datetime.now().date()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

now = datetime.datetime.now()
no_microseconds = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", no_microseconds)

date1 = datetime.datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime.datetime(2025, 1, 2, 13, 30, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", int(seconds))

def degrees_to_radians(deg):
    return math.radians(deg)

def area_trapezoid(h, base1, base2):
    return ((base1 + base2) / 2.0) * h

def area_regular_polygon(n_sides, side_length):
    n = n_sides
    s = side_length
    return (n * s * s) / (4.0 * math.tan(math.pi / n))

def area_parallelogram(base, height):
    return float(base) * float(height)

#IDK 


import json


f = open("data.json", "r", encoding="utf-8")
data = json.load(f)
f.close()


rows = []
for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu = attrs["mtu"]
    rows.append((dn, descr, speed, mtu))


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:>6}  {:>6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for dn, descr, speed, mtu in rows:
    print("{:<50} {:<20} {:>6}  {:>6}".format(dn, descr, speed, mtu))
