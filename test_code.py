from code import get_Cp_parameter
from pytest import raises


def test_function():
    with raises(ValueError) as exception:
        get_Cp_parameter(4,0.5,0.5,4,0)
    with raises(ValueError) as exceptiion:
        get_Cp_parameter(3,0.5,0.5,2,0)
    with raises(TypeError) as exception:
        get_Cp_parameter('4',0.5,0.5,2,0)
