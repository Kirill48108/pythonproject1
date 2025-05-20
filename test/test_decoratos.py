from src.decorators import log


def test_log():

    @log()
    def add_numbers(a, b):
        return a + b

    result1 = add_numbers(3, 5)
    assert result1 == 8

    @log("log.txt")
    def sub_numbers(a, b):
        return a - b

    result2 = sub_numbers(21, 4)
    assert result2 == 17

    @log(filename="mylog.txt")
    def test_function_error(x, y):
        raise ValueError("Test error")
