import pytest
from num2words import num2words

from number_to_phrase import translator

for num in range(1000):
    print(num2words(num))

num = -1
@pytest.mark.repeat(1000)
def test_num_to_phrase():
    global num
    num += 1
    assert translator(num) == num2words(num).replace('and ', '')