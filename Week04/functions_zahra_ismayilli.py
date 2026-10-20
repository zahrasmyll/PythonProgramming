# custom_power
custom_power = lambda x=0, e=1, /: x ** e


# custom_equation
def custom_equation(
    x: int,
    y: int,
    /,
    a: int = 1,
    b: int = 1,
    c: int = 1
) -> float:
    """
    Calculates the equation using five integers.

    :param x: First integer.
    :param y: Second integer.
    :param a: Exponent of x.
    :param b: Exponent of y.
    :param c: Divisor.
    :return: Result of the equation as a float.
    """
    return (x ** a + y ** b) / c


# fn_w_counter
def fn_w_counter():
    if not hasattr(fn_w_counter, "counts"):
        fn_w_counter.counts = {}

    import inspect

    caller = inspect.currentframe().f_back
    caller_name = caller.f_code.co_name

    counts = fn_w_counter.counts
    counts[caller_name] = counts.get(caller_name, 0) + 1

    return sum(counts.values()), counts.copy()
