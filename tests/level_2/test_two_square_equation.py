from functions.level_2.two_square_equation import solve_square_equation
import pytest



def test__solve_square_equation__if_discriminant_is_negative():
    assert solve_square_equation(1.0, 2.0, 3.0) == (None, None)


def test__solve_square_equation__if_not_square_coefficient():
    assert solve_square_equation(0, 4.0, 8.0) == (-2, None)


def test__solve_square_equation__if_not_square_coefficient_and_not_linear_coefficient():
    assert solve_square_equation(0, 0, 8.0) == (None, None)

def test__solve_square_equation__if_all_input_and_discriminant_is_positive():
    assert solve_square_equation(1, 3.0, 1.0) == (-2.618033988749895, -0.3819660112501051)

def test__solve_square_equation__if_not_input():
    with pytest.raises(TypeError):
        solve_square_equation()

def test__solve_square_equation__if_wrong_input():
    with pytest.raises(TypeError):
        solve_square_equation('1.0', '2.0', '3.0')




