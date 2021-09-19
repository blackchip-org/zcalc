import pytest

from zcalc.env import Env
from zcalc.stdlib import math

@pytest.mark.parametrize('line,expected', [
    ('1; 2; 3; clear', []),
    ('["*" 2; [put-stack double; 1; 2; 3; [each double', ['2', '4', '6']),
    ('42; [put answer; clear; [get answer', ['42']),
    ('3; 4; [put-stack other; 1; 2; [get-stack other', ['1', '2', '3', '4']),
    ('1; 2; 3; 4; rev', ['4', '3', '2', '1']),
    ('1; 2; 3; 4; down', ['4', '1', '2', '3']),
    ('1; 2; 3; 4; up', ['2', '3', '4', '1']),
    ('1; 2; swap', ['2', '1']),
    ('1; 2; 3; c', [])

])
def test_builtin(line, expected):
    z = Env(prelude=False)
    z.use('math')
    z.eval(line)
    assert z.stack == expected
