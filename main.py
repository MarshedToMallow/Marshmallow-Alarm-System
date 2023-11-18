import datetime
from alarms import AlarmHandler

SECOND = datetime.timedelta(seconds = 1)

handler = AlarmHandler()
handler.add_alarm(time = datetime.datetime.now() + datetime.timedelta(seconds = 5), name = "BEEP BEEP BEEP", repeat = datetime.timedelta(seconds = 10))
early = handler.alarms[0].time

while True:
    late = datetime.datetime.now()
    handler.check_alarms(early, late)
    if early.microsecond > late.microsecond:print(".")
    early = late