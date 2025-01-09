import pytest
from src.mainn import assembly, check_age, only_str
from src.mainn import divide



def test_assembly():
    "Tests the multi-valued addition function."
    assert assembly(2,3) == 5
    assert assembly(-1,1) == 0
    assert assembly(0,0) == 0


def test_divide():
    assert divide(10,2) == 5
    assert divide(9,3) == 3

    #We test if it raises the correct exception
    with pytest.raises(ValueError, match="Zero division is not allowed."):
        divide(10,0)


def test_check_age():
    assert check_age(15) == "Age is valid"
    with pytest.raises(ValueError, match="Age cannot be negative."):
        check_age(-1)

def test_only_str():
    assert only_str("test") == "TEST"
    with pytest.raises(TypeError, match="Only strings are supported."):
        only_str(123)
    with pytest.raises(TypeError, match="Only strings are supported."):
        only_str(["no" "string"])
