import timeit
testcode = '''
inpu = """
batbatbat, batebatebatebate, titititititititi, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut
"""
words = inpu.split(", ")[::-1]

is_feasible = lambda w : len([c for c in w if c not in "ertabdfyh"]) == 0
feasible_words = [w for w in words if is_feasible(w)]

result = max(feasible_words, key=len)

# print(result)
'''

print(timeit.timeit(stmt=testcode))
