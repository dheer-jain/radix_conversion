def any_to_decimal(number: str, radix: int) -> float:
    '''
    Convert given number of radix into equivalent decimal number.
    
    >>> convert.any_to_decimal("2baD", 16)
    11181
    >>> convert.any_to_decimal("101.101", 2)
    5.625
    >>> convert.any_to_decimal("-212", 3)
    -23
    '''
    import string

    valid_radix = type(radix) is int and radix >= 2 and radix <= 36
    assert valid_radix, "radix must be passed as int in [2, 36]"

    valid_number = (type(number) is str
                    and (not not number)  # number != ""
                    and (number.count(".") < 2)
                    )
    assert valid_number, "non string or invalid number passed to program."

    number = number.strip().upper()

    is_negative = number[0] == '-'
    if is_negative:
        number = number[1:]  # remove -ve sign

    # create tuple of allowed character and tally the nubmer.
    allowed_characters = tuple("." + string.digits + string.ascii_uppercase)
    for ch in number:
        if ch not in allowed_characters[:radix + 1]:
            raise ValueError("either number not in radix or invalid.")

    # create list of corresponding values of characters in number.
    values = []
    for ch in number:
        if ch.isdigit():    # int as str to int
            values.append(int(ch))
        elif ch.isalpha():   # alphabet to int.
            values.append(ord(ch) - ord('A') + 10)
        elif ch == ".":  # leaving "." as it is.
            values.append(ch)

    # generating power(index) to use with radix upon number from right to left
    # Say for "302.1" power as -1, for "1.1001" power = -4
    if '.' in values:   # get power as -ve number of digit after radix point.
        power = -(len(values) - values.index(".")) + 1
        values.remove('.')
    else:   # if no fraction part no negative power
        power = 0

    values.reverse()
    decimal = 0

    # appling power from right to left on radix while multiplying it with ...
    # ... corresponding  digit(value) of number and adding.
    for element in values:
        decimal += element * pow(radix, power)
        power += 1

    return - decimal if is_negative else decimal


def main():
    number = input("Please enter number: ")
    radix = int(input('Please enter radix: '))
    print(f"Equivalent Decimal: {any_to_decimal(number, radix)}")


if __name__ == "__main__":
    main()
