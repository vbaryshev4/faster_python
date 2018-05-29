from collections import Counter

def split_mails(arg):
    # Firstway
    for mail in arg:
       domain = mail.split('@')[1].strip()
       yield domain
    # Second way
    # return (mail.split('@')[1].strip() for mail in arg)
 
def get_top10(file):
    with open(file) as f:
        result = split_mails(f)
        return Counter(result).most_common(10)

def start():
    return get_top10('task_1_test.txt')

if __name__ == '__main__':
    result = start()
    for i, j in result:
        print(i, j) 