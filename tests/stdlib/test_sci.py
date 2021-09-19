import pytest

from zcalc.env import Env
from zcalc.stdlib import math

@pytest.mark.parametrize("line", [
    '-12.34; abs; 12.34',
    '1; exp; 2.718281828459045235360287471',
    '2; ln; 0.6931471805599453094172321215',
    '2; log10; 0.3010299956639811952137388947',
    '6; 2; pow; 36',
    '256; sqrt; 16',
])
def test_sci(line):
    z = Env(prelude=False)
    z.use('sci')
    z.eval(line)
    assert z.pop() == z.pop()


