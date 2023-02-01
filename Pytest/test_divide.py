def divide(a,b):
    return a/b


def test_divide_integers():
    assert divide(2,2) == 1
    assert divide(5,2) == 2.5


def test_divide_zero():
    try:
        divide(5,0)
        assert False, "Expected an exception"

    except ZeroDivisionError as e:
        assert str(e) == "division by zero"

