import timeit

testcode = '''
inpu = """
cate, cat, bat, bate, catayon
"""
words = inpu.split(", ")[::-1]

is_feasible = lambda w : len([c for c in w if c not in "ertabdfyh"]) == 0
feasible_words = [w for w in words if is_feasible(w)]

result = max(feasible_words, key=len)

# print(result)
'''

print(timeit.timeit(stmt=testcode))
