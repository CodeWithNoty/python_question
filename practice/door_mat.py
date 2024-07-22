def create_door_mat(m, n):
    # Top part of the mat
    for i in range(m // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(n, '-'))

    # Welcome message
    print('WELCOME'.center(n, '-'))

    # Bottom part of the mat
    for i in range(m // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(n, '-'))

# Example usage:
m = 9  # Height of the mat
n = 27  # Width of the mat

create_door_mat(m, n)
