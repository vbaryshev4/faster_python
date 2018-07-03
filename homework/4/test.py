from encode import *
from decode import *

def run_test(data, code_type, count_results):
    result = {'True':[], 'False':[]}

    if code_type == 'encode':
        for pair in data:
            res = encode(pair[0])
            if res == pair[1]:
                lst = result['True']
                lst.append(pair)
                result['True'] = lst
            else:
                lst = result['False']
                lst.append(pair)
                result['False'] = lst

    elif code_type == 'decode':
        for pair in data:
            res = decode(pair[1])
            if res == pair[0]:
                lst = result['True']
                lst.append(pair)
                result['True'] = lst
            else:
                lst = result['False']
                lst.append(pair)
                result['False'] = lst

    if count_results == True:
        count_true = result['True']
        count_true = len(count_true)
        result['True'] = count_true
        count_false = result['False']
        count_false = len(count_false)
        result['False'] = count_false

        return [code_type, result]

    return [code_type, result]


if __name__ == '__main__':

    test_data = [
                    ["AAAAAAAAAAAABBBCCDAA", "12A3B2C-1D2A"],
                    ["ABCABCABCABCDDDFFFFFF","-12ABCABCABCABC3D6F"],
                    ["WWWWWWWWWWWWB", "12W-1B"],
                    ["ABCD", "-4ABCD"],
                    ["DDDD", "4D"],
                    ["BAAAABBBCCDCAAM", "-1B4A3B2C-2DC2A-1M"],
                    ["ABCABCABCABC","-12ABCABCABCABC"],
                    ["FFFABCABCABCABC","3F-12ABCABCABCABC"]
                ]
                
    result = run_test(test_data, 'encode', count_results=True)
    print(result)

    result = run_test(test_data, 'decode', count_results=True)
    print(result)


