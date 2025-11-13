from sleep_tracker import *

def test_get_hour():
    assert get_hour("10:00 am") == 10
    assert get_hour("12:00 pm") == 12
    assert get_hour("3:00 pm") == 15

def test_hours_delta():
    assert get_hours_delta("10:00 am", "2:00 pm") == 4
    assert get_hours_delta("10:00 am", "11:00 am") == 1
    assert get_hours_delta("11:00 am", "10:00 am") == 23
    assert get_hours_delta("12:00 am", "2:00 pm") == 14
    assert get_hours_delta("2:00 pm", "12:00 am") == 10

def test_time_to_int():
    assert time_to_int(10, "am") == 10
    assert time_to_int(11, "am") == 11
    assert time_to_int(12, "am") == 0
    assert time_to_int(2, "am") == 2
    assert time_to_int(3, "pm") == 15
