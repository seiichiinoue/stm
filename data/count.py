from collections import Counter
from itertools import chain

def countInFile(filename):
    with open(filename) as f:
        return Counter(chain.from_iterable(map(str.split, f)))

import os
def count_in_file(path):
    d = dict()
    l = os.listdir("./sample")
    for author in l:
        for fn in os.listdir("./sample/"+author):
            with open("./sample/"+author+"/"+fn) as f:
                tmp = f.readlines()
                for sentence in tmp:
                    for word in sentence:
                        if word not in d.keys():
                            d[word] = 0
                        d[word] += 1
    return d

# import os
# l = os.listdir("./sample")
# for author in l:
#     for fn in os.listdir("./sample/"+author):
#         with open("./sample/"+author+"/"+fn) as f:
#             with open("./sample.txt", mode="a") as wf:
#                 wf.writelines(f.readlines())

count = countInFile("./all.txt")
# count = count_in_file("./sample.txt")
print(len(count.keys()))
s = 0
for k, v in count.items():
    if v < 5: s += 1
print(s)

