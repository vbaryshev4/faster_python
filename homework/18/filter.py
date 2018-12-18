def sort_odds(itterable_obj):
    return [i for i in itterable_obj if i % 2 == 0]

a = [1, 2, 3, 4]
result = sort_odds(a)
print(result)

a = [1, 2, 3, 4]
print([i for i in a if i % 2 == 0])
