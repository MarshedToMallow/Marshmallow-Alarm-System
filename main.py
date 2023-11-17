import datetime
from alarms import Alarm

SECOND = datetime.timedelta(seconds = 1)

target = Alarm(datetime.datetime.now() + datetime.timedelta(seconds = 5), datetime.timedelta(seconds = 10))
early = target.time

while True:
    late = datetime.datetime.now()
    if target.check(early, late):print("BEEP BEEP BEEP")
    if early.microsecond > late.microsecond:print("A second has passed")
    early = late