import time
import random


def read_data(filename):
    with open(filename) as data_file:
        return list(map(str.strip, data_file.readlines()))


def gen_lines(emails, names, length):
    current_time = time.time()
    for i in range(0, length):
        name = random.choice(names)
        email = random.choice(emails)
        datetime = time.strftime('%Y-%m-%d %H:%M', time.gmtime(random.uniform(1, current_time)))
        yield "%s\t%s\t%s\n" % (name, email, datetime)


def generate_test_file(length):
    emails = read_data("emails.txt")
    names = read_data("names.txt")
    lines_generator = gen_lines(emails, names, length)

    with open('logs.txt', 'w') as file:
        file.writelines(lines_generator)
    print("Generated %i lines of logs" % length)


if __name__ == "__main__":
    generate_test_file(100000000)
