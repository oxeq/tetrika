import pytest
from solution import appearance

@pytest.mark.parametrize("intervals, expected", [
    (
        {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        3117
    ),
    (
        {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                      1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                      1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                      1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                      1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        3577
    ),
    (
        {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        3565
    ),
])
def test_default_cases(intervals, expected):
    assert appearance(intervals) == expected


def test_no_overlap():
    """Тест без пересечений"""
    intervals = {
        'lesson': [100, 200],
        'pupil': [50, 90, 210, 220],
        'tutor': [80, 99, 201, 205]
    }
    assert appearance(intervals) == 0


def test_full_overlap():
    """Тест с полным пересечением"""
    intervals = {
        'lesson': [100, 200],
        'pupil': [100, 200],
        'tutor': [100, 200]
    }
    assert appearance(intervals) == 100


def test_partial_overlap():
    """Тест с частичным пересечением"""
    intervals = {
        'lesson': [100, 200],
        'pupil': [50, 150],
        'tutor': [120, 180]
    }
    assert appearance(intervals) == 30


def test_multiple_intervals():
    """Тест с несколькими интервалами"""
    intervals = {
        'lesson': [100, 200],
        'pupil': [50, 60, 70, 80, 90, 110, 150, 170],
        'tutor': [55, 65, 75, 85, 105, 115, 160, 180]
    }
    assert appearance(intervals) == 15


def test_empty_intervals():
    """Тест с пустыми интервалами"""
    intervals = {
        'lesson': [100, 200],
        'pupil': [],
        'tutor': []
    }
    assert appearance(intervals) == 0
