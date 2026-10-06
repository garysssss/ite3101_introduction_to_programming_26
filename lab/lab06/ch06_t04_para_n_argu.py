def power(base: int, exponent: int) -> int:
    result = base ** exponent
    print("%d to the power of %d is %d." % (base, exponent, result))
    return result


power(37, 4)