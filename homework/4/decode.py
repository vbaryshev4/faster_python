def merge_(lists):
    result = []

    for lst in lists:
        if lst[0].count('-') > 0:
            result.append(''.join(lst[1:]))
        elif lst[0].count('-') == 0:
            result.append(lst[1]*int(lst[0]))

    result = ''.join(result)
    
    return result


def decode(string):
    result = []
    part = []
    
    for letter in string:

        try:
            int(letter)
            if part == []:
                part.append(letter)
            elif part != []:
                part[-1] +=  str(letter)

        except ValueError:
            part.append(letter)
            if letter != '-':
                if len(part) > 1:
                    result.append(part)
                elif len(part) == 1:
                    result[-1].append(letter)
                part = []
 
    return merge_(result)
