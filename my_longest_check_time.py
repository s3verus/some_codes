import timeit

testcode = '''
inpu = """
cate, cat, bat, bate, catayon
"""

lists = inpu.split(", ")[::-1]
maxim = max(lists, key=len)

lens = len(lists)
for j in range(lens):
    for i in maxim:
        if i not in "ertabdfyh":
            lists.remove(maxim)
            if len(lists) == 0:
                maxim = ""
                break
            maxim = max(lists, key=len) 
            break
# print(maxim)
'''

print(timeit.timeit(stmt=testcode))
