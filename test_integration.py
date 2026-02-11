from basic_operations import add
from advanced_operations import sin
import math

def test_add_and_sin():
    result = sin(add(0, math.pi/2))
    assert round(result,2) == 1.00
