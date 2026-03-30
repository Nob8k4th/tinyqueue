import pytest

from tinyqueue.scheduler import Scheduler


def test_parse_cron_valid():
    assert Scheduler().parse_cron("*/5 * * * *") == 5


def test_parse_cron_valid_one():
    assert Scheduler().parse_cron("*/1 * * * *") == 1


def test_parse_cron_invalid_parts():
    with pytest.raises(ValueError):
        Scheduler().parse_cron("* * *")


def test_parse_cron_invalid_head():
    with pytest.raises(ValueError):
        Scheduler().parse_cron("5 * * * *")


def test_parse_cron_returns_interval():
    assert Scheduler().parse_cron("*/10 * * * *") == 10
