from functions.level_1.two_date_parser import compose_datetime_from
import datetime, pytest
from freezegun import freeze_time


@freeze_time("2024-01-18 15:00:00")
def test_compose_datetime_from_today():
    assert compose_datetime_from('today', '14:40') == datetime.datetime(2024, 1, 18, 14, 40)


@freeze_time("2024-01-18 15:00:00")
def test_compose_datetime_from_tomorrow():
    assert compose_datetime_from('tomorrow', '14:40') == datetime.datetime(2024, 1, 19, 14, 40)

def test_compose_datetime_wrong_time_format():
    with pytest.raises(ValueError):
        compose_datetime_from('today', '14-40')

