import string

def print_rangoli(size):
    letters = string.ascii_lowercase[:size]
    pattern = []

    for i in range(size-1, -1, -1):
        left_part = letters[size-1:i:-1]
        middle = letters[i]
        right_part = letters[i+1:size]
        line = '-'.join(left_part + middle + right_part)
        pattern.append(line.center(4*size - 3, '-'))

    full_pattern = pattern + pattern[-2::-1]
    print('\n'.join(full_pattern))


if __name__ == '__main__':
