import datetime

NEVER = datetime.timedelta(weeks = 10 ** 8)

class Alarm:
    def __init__(self, time: datetime.datetime, name: str = "Alarm", repeat: datetime.timedelta = NEVER, offset: datetime.timedelta = datetime.timedelta()):
        self.time = time
        self.name = name
        self.repeat = repeat
        self.offset = offset
    
    def check(self, early: datetime.datetime, late: datetime.datetime):
        trigger = early < self.time + self.offset and late > self.time + self.offset
        if trigger and self.repeat != NEVER:self.time += self.repeat
        return trigger

class RelativeAlarm:
    def __init__(self, parent_offset: datetime.timedelta, offset: datetime.timedelta = datetime.timedelta()):
        self.parent_offset = parent_offset
        self.offset = offset
    
    def parent_triggered(self, parent_time):
        self.time = parent_time + self.parent_offset + self.offset

class AlarmHandler:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, time: datetime.date, name: str = "Alarm", repeat = datetime.timedelta(365 * 1000), offset = datetime.timedelta()):
        self.alarms.append(Alarm(time, name, repeat, offset))
    
    def check_alarms(self, early: datetime.datetime, late: datetime.datetime):
        for alarm in self.alarms:
            if alarm.check(early, late):print(alarm.name)