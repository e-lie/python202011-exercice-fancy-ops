from computation_libs.fancy_int_operations import fancy_add

def test_fancy_add():
    assert fancy_add(3,8) == 11
    assert fancy_add(0,0) == 0


def test_fancy_add_float():
    try:
        fancy_add(1.0, 2)
        fancy_add(2, 3.0)
    except AssertionError:
        return
    raise Exception("Should fail with float with AssertionError")