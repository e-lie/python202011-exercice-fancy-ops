
def fancy_add(n: int, m: int) -> int:
    assert isinstance(n, int)
    assert isinstance(m, int)
    return n + m

def fancy_product(n: int, m: int) -> int:
    assert isinstance(n, int)
    assert isinstance(m, int)
    return n * m

from .more_fancy_operations import fancy_substract

fancy_operations = {
    "add" : {
        "function": fancy_add,
        "symbol": '+'
    },
    "product" : {
        "function": fancy_product,
        "symbol": '*'
    },
    "substract" : {
        "function": fancy_substract,
        "symbol": '-'
    }
}