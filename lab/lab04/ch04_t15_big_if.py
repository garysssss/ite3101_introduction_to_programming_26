# Complete the if and elif statements!
def grade_converter(grade: int) -> str:
    if grade< 90-:
        return "A"
    elif grade>90 <80:
        return "B"
    elif grade>80 <70:
        return "C"
    elif grade>70 <60:
        return "D"
    else: grade <60
        return "F"


This should print an "A"
print(grade_converter(92))

This should print a "C"
print(grade_converter(70))

This should print an "F"
print(grade_converter(61))
