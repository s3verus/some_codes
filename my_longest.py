import timeit

testcode = '''
inpu = """
batbatbat, batebatebatebate, titititititititi, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut, cat, bat, bate, clean, toss, a, coin, to, your, witcher, can, can, can, cant, not, title, url, text, ghost, dog, lost, in, translate, cat, cut
"""

lists = inpu.split(", ")[::-1]
maxim = max(lists, key=len)

for item in lists:
    for i in maxim:
        if i not in "ertabdfyh":
            lists.remove(maxim)
            maxim = max(lists, key=len) 
            break
# print(maxim)
'''
print(timeit.timeit(stmt=testcode))
