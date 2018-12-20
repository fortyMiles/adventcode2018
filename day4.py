# Created by mqgao at 2018/12/13

import re

fall_asleep, wake_up = 'falls asleep', 'wakes up'


def get_sleep_points(sorted_events):
    sleep_points = [False]*60

    sleep_time = None

    for event in sorted_events:
        timestampe, action = event

        if action == fall_asleep: sleep_time = timestampe
        elif action == fall_asleep: continue

        if sleep_time:
            sleep_points[sleep_time:timestampe] = [True]*(timestampe - sleep_time)

    return sleep_points


def get_guards_sleep_time(guards_sleep_info): pass


guard_pat = re.compile('\[\d{4}-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] Guard #(\d+)\s+begins shift')
event_pat = re.compile('\[\d{4}-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (wakes up|falls asleep)')


def parse_events(events):



assert guard_pat.findall('[1518-03-13 23:46] Guard #2081 begins shift')[0] == ('03', '13', '23', '46', '2081')
assert event_pat.findall('[1518-06-08 00:49] wakes up')[0] == ('06', '08', '00', '49', 'wakes up')


events = [(5, fall_asleep), (25, wake_up), (30, fall_asleep), (55, wake_up)]

guard_10_sleep = get_sleep_points(events)

assert all([sleep for sleep in guard_10_sleep[5:25]])
assert not guard_10_sleep[25]
assert all([sleep for sleep in guard_10_sleep[30:55]])
assert not guard_10_sleep[55]

