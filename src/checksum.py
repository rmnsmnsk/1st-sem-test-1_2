def modulo11_checksum(isbn_number: str):

    if not isinstance(isbn_number, str):
        return False

    digits = [int(char) for char in isbn_number if char.isdigit()]

    if len(digits) != 10:
        return False

    check_digit = digits[-1]
    total = 0

    for i in range(len(digits) - 1):
        weight = 10 - i
        digit = digits[i]
        total += digit * weight

    total += check_digit
    return total % 11 == 0


