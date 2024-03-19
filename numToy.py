if __name__ == '__main__':
    s = "Aa .1"
    print(s[0].isupper())
    print(s[2].isspace())
    print(s[3].upper()) # no op, still .
    print(s[4].upper())  # no op, still 1
    print(s[4].isalnum())  # true, is num or alpha
    print(s[4].isdigit())  # true, is digit
    print(s[0].isalnum())  # true, is num or alpha
    print(s[1].isalnum())  # true, is num or alpha
    print(s[2].isalnum())  # false, is num or alpha
