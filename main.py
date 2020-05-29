import time as t
from win10toast import ToastNotifier
from datetime import datetime

h = str(input("Start hour: "))
m = str(input("Start minute: "))

hora = datetime.strptime(f"{h}:{m}:00", "%X").time()
hora_act = datetime.now().time()

activities = int(input("How many tasks: "))
title = []
note = []
seconds = []
toast = ToastNotifier()

for i in range(activities):
    title.append(str(input("Title of task: ")))
    note.append(str(input("Note of task: ")))
    hours = int(input("How many hours to wait: "))
    minutes = int(input("How many minutes to wait: "))
    s = int(input("How many seconds to wait: "))
    seconds.append((hours * 3600) + (minutes * 60)+s)

while (hora > hora_act):
    t.sleep(1)
    hora_act = datetime.now().time()

for j in range(activities):
    for i in range(seconds.pop(0)):
        t.sleep(1)
    toast.show_toast(f"{title.pop(0)}", f"{note.pop(0)}", duration=20)