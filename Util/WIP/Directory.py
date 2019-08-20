#
# from 
# https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
#

import os

#long way 

path = 'W:/GITHUB/NLP_SO/Data/'

print("******************************************")

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        #if '.txt' in file:
        files.append(os.path.join(r, file))

for f in files:
    print(f)


print("******************************************")
print("")
print("******************************************")


import glob

files = [f for f in glob.glob(path + "**/*.*", recursive=True)]

for f in files:
    print(f)