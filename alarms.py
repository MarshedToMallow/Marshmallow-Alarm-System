import datetime

NEVER = datetime.timedelta(weeks = 10 ** 8)

class Alarm:
    def __init__(self, time, repeat = NEVER, offset = datetime.timedelta()):
        self.time = time
        self.repeat = repeat
        self.offset = offset
    
    def check(self, early: datetime.datetime, late: datetime.datetime):
        trigger = early < self.time + self.offset and late > self.time + self.offset
        if trigger and self.repeat != NEVER:self.time += self.repeat
        return trigger

class AlarmHandler:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, time, repeat = datetime.timedelta(365 * 1000), offset = datetime.timedelta()):
        self.alarms.append(Alarm(time, repeat, offset))