sumlist = []

for x in range (10):
    sumlist.append(str(x))

print(str(sumlist))

def split_list(alist, size):
    list_of_lists = []
    while len(alist) > size:
        abit = alist[:size]
        list_of_lists.append(abit)
        alist = alist[size:]
    list_of_lists.append(alist)
    return list_of_lists

def a_new_dict(alist):
    new_object = {}
    new_object["first"] = alist[0]
    new_object["second"] = alist[1]
    new_object["third"] = alist[2]
    new_object["fourth"] = alist[3]
    new_object["fifth"] = alist[4]
    print(str(new_object))
    return new_object

answer = split_list(sumlist, 5)
print(str(answer))

endArray = []

for v in answer:
    print("mark")
    one_obj = a_new_dict(v)
    endArray.append(one_obj)

print(str(endArray))
