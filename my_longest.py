inpu = input("input: ")

lists = inpu.split(", ")[::-1]
maxim = max(lists, key=len)

for item in lists:
    for i in maxim:
        if i not in "ertabdfyh":
            lists.remove(maxim)
            maxim = max(lists, key=len) 
            break
print(maxim)
