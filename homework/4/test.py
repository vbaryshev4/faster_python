from encode import *
from decode import *

def run_test(data, code_type):
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
            print(pair[1], decode(pair[1]))
            # res = decode(pair[1])
            # if res == pair[0]:
            #     lst = result['True']
            #     lst.append(pair)
            #     result['True'] = lst
            # else:
            #     lst = result['False']
            #     lst.append(pair)
            #     result['False'] = lst

    return result


if __name__ == '__main__':

    test_data = [
                    ["AAAAAAAAAAAABBBCCDAA", "12A3B2C-1D2A"],
                    ["ABCABCABCABCDDDFFFFFF","-12ABCABCABCABC3D6F"],
                    ["WWWWWWWWWWWWB", "12W-1B"],
                    ["ABCD", "-4ABCD"],
                    ["DDDD", "4D"],
                    ["BAAAABBBCCDCAAM", "-1B4A3B2C-2DC2A-1M"]
                ]
                
    result = run_test(test_data, 'encode')
    print(result)

    # result = run_test(test_data, 'decode')
    # print(result)

