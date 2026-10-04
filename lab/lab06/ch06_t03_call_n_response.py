def square(10: float) -> float:
    """Returns the square of a number."""
    squared = 10 ** 2
    print("%d squared is %d." % (10, squared))
    return squared

# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses
def square(10):
    print(10**2)