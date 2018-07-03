def merge_(lists):
    result = []

    for lst in lists:
        if lst[0] == '-':
            result.append(''.join(lst[2:]))
        elif lst[0] != '-':
            result.append(lst[1]*lst[0])

    return ''.join(result)


def decode(string):
    result = []
    part = []
    
    for letter in string:

        try:
           letter = int(letter)
           part.append(letter)
        except ValueError:
            part.append(letter)
            if letter != '-':
                if len(part) > 1:
                    result.append(part)
                elif len(part) == 1:
                    result[-1].append(letter)
                part = []
    print(string, result)
    return merge_(result)
