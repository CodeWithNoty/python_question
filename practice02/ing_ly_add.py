def num(n):
    print(str(n))
    if len(n) < 3:
        n += 'ing'  # Correcting this line to concatenate strings
    elif n.endswith('ing'):  # Correcting condition to check if n ends with 'ing'
        n += 'ly'  # Correcting this line to concatenate strings
    elif len(n) > 3:
        return n
    return n  # Adding a return statement if none of the conditions are met

print(num("abc"))
