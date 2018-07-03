def merge_(lists):
    result = ''
    uniq = []

    for lst in lists:
        if len(lst) > 1 and uniq == []:
            result += str(len(lst)) + lst[-1]
        elif len(lst) > 1 and uniq != []:
            result += '-' + str(len(uniq)) + ''.join(uniq)
            result += str(len(lst)) + lst[-1]
            uniq = []
        elif len(lst) == 1:
            uniq.append(lst[-1])
    if uniq != []:
        result += '-' + str(len(uniq)) + ''.join(uniq)

    return result


def encode(string):  
    result = []
    part_result = [string[0]]

    for letter in string[1:]:
        if part_result[-1] == letter:
            part_result.append(letter)
        elif part_result[-1] != letter:
            result.append(part_result)
            part_result = [letter]
    result.append(part_result)
    
    return merge_(result)
