import pytest
import argparse
from main import validate_string, recursive_human_readable_convertor, convertor


@pytest.fixture(scope="module")
def test_short_string():
    return "SST"


@pytest.fixture(scope="module")
def test_long_string():
    return "STSTS"


def test_validate_valid_string():
    # Test case to validate a valid string
    data = "STSTS"
    result = validate_string(data)
    assert data == result


def test_validate_invalid_string():
    # Test case to validate an invalid string
    data = "STSTSVSDEETTT"
    with pytest.raises(argparse.ArgumentTypeError):
        validate_string(data)


def test_corner_cases_recursive_human_readable_convertor(test_short_string):
    # Test case to check recursion against corner cases 0, 1, negative number
    iter = 0
    expected = ""
    result = recursive_human_readable_convertor(test_short_string, iter)
    assert expected == result

    iter = -1
    expected = ""
    result = recursive_human_readable_convertor(test_short_string, iter)
    assert expected == result

    iter = 1
    expected = "Soft."
    result = recursive_human_readable_convertor(test_short_string, iter)
    assert expected == result


def test_short_recursive_human_readable_convertor(test_short_string):
    # Test cases to check recursion against a short string
    iter = 5
    expected = "Soft, Soft, Tough, Soft and Soft."
    result = recursive_human_readable_convertor(test_short_string, iter)
    assert expected == result

    iter = 2
    expected = "Soft and Soft."
    result = recursive_human_readable_convertor(test_short_string, iter)
    assert expected == result


def test_long_recursive_human_readable_convertor(test_long_string):
    # Test cases to check recursion against a long string
    iter = 8
    expected = "Soft, Tough, Soft, Tough, Soft, Soft, Tough and Soft."
    result = recursive_human_readable_convertor(test_long_string, iter)
    assert expected == result

    iter = 3
    expected = "Soft, Tough and Soft."
    result = recursive_human_readable_convertor(test_long_string, iter)
    assert expected == result


def test_convertor(test_short_string):
    # Test case to check returned strings are correct
    input = [test_short_string, "5", "2"]
    expected = ["Soft, Soft, Tough, Soft and Soft.", "Soft and Soft."]
    result = convertor(input)
    assert result == expected
