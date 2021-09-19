import pytest

from zcalc.env import Env
from zcalc.stdlib import math

@pytest.mark.parametrize('line', [
    '6 ; 2 ; + ; 8',
    '6 ; 2 ; - ; 4',
    '6 ; 2 ; * ; 12',
    '6 ; 2 ; / ; 3',
    '3 ; 2 ; % ; 1',

    '6 ; 2 ; a ; 8',
    '6 ; 2 ; s ; 4',
    '6 ; 2 ; m ; 12',
    '6 ; 2 ; d ; 3',

    '6 ; 2 ; add ; 8',
    '6 ; 2 ; sub ; 4',
    '6 ; 2 ; mul ; 12',
    '6 ; 2 ; div ; 3',
    '3 ; 2 ; mod ; 1',

    '1.1; 2.2; add; 3.3',  # ensure it is a decimal, not float
    '0.5; frac; 1/2',
    '2.99; int; 2',
    '-5; neg; 5',
    '1.40500e2; norm; 140.5',
    '1; 2; 3; 4; sum; 10',

])
def test_math(line):
    z = Env(prelude=False)
    z.use('math')
    z.eval(line)
    assert z.pop() == z.pop()

