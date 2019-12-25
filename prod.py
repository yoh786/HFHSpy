#INIT VARS
desiredresult = []
listresult = []

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
    new_object["Article Name"] = alist[0]
    kbcut = alist[1]
    kb = kbcut[:7]
    new_object["KB Number"] = kb
    new_object["Description"] = alist[2]
    print(str(new_object))
    return new_object
#END VARS
#set filepath
filepath = 'entriesshort.txt'
#Open file, push lines to an array
with open(filepath, encoding="utf-8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        popin = line.strip()
        listresult.append(popin)
        print(".")
        line = fp.readline()
        cnt += 1
    print("done with line loop")
#split said array
lines_per_object = 4
answer = split_list(listresult, lines_per_object)
#convert Lists to Dictionaries
count = 0
for e in answer:
    print("{} made".format(str(count)))
    one_entry = a_new_dict(e)
    desiredresult.append(one_entry)
    count += 1
#output a file
f = open("result.txt", "a", encoding="utf-8")
f.write(str(desiredresult))
f.close()
#el fin
