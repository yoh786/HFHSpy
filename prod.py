#init vars
desiredresult = []

def split_list(alist, size):
    list_of_lists = []
    while len(alist) > size:
        abit = alist[:size]
        list_of_lists.append(abit)
        alist = alist[size:]
    list_of_lists.append(alist)
    return list_of_lists

#open filepath
filepath = 'yoScripts/entriesshort.txt'
#push lines to an array
with open(filepath, encoding="utf-8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        popin = line.strip()
        desiredresult.append(popin)
        line = fp.readline()
        cnt += 1
    print("done with line loop")
    print(str(desiredresult))
#split said array
lines_per_object = 4
answer = split_list(desiredresult, lines_per_object)
print(str(answer))

#output a file
f = open("result.txt", "a", encoding="utf-8")
f.write(str(answer))
f.close()
#convert array of arrays to a array of objects?


#output another file
