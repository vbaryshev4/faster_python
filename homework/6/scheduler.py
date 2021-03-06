import time
from random import randint
import asyncio

class Scheduler:
    """docstring for Scheduler"""
    def __init__(self):
        pass

    async def delay(self, func, args, seconds):
        await asyncio.sleep(seconds)
        print(func(*args))
        
if __name__ == '__main__':

    def sum_(a, b):
        return a + b

    def minus_(a, b):
        return a - b

    def mul_(a, b):
        return a * b

    def dev_(a, b):
        return a / b

a = Scheduler()
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(a.delay(sum_,[2,2], 4)), ioloop.create_task(a.delay(sum_, [10,10], 10))]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()


    # funcs = [sum_, minus_, mul_, dev_]

    # result = [{'counts':{'True':0, 'False':0}}]

    # for i in range(100):
    #     case_template = {
    #         'object':None, 
    #         'function':None, 
    #         'args':None,
    #         'excpected_result':None,
    #         'test_result':None,
    #         'std_out':None
    #                     }

    #     case_template['function'] = funcs[randint(0, len(funcs)-1)]
    #     case_template['object'] = Scheduler()
    #     arg_a, arg_b = randint(1, 256), randint(1, 256)
    #     case_template['args'] = [arg_a, arg_b]
    #     case_template['expected_result'] = case_template['function'](arg_a, arg_b)
    #     delay = 0
    #     case_template['test_result'] = case_template['object'].delay(case_template['function'], [arg_a, arg_b], delay)
    #     if case_template['expected_result'] == case_template['test_result']:
    #         case_template['std_out'] = True
    #         result[0]['counts']['True'] += 1
    #     else:
    #         case_template['std_out'] = False
    #         result[0]['counts']['False'] += 1

    #     result.append(case_template)

    # print(result)
    # print('TESTS: Trues = {0} and Falses = {1}'.format(result[0]['counts']['True'], result[0]['counts']['False']))