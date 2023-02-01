import pytest

# @pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
# def test_string_is_digit(item):
#         assert item.isdigit()
# @pytest.mark.parametrize("a")
def test_kullanici():
    a = "asdasdsad"

    assert not a.isdigit()
