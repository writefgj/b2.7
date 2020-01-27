import collections
FILE_NAME = "dummy-access.log"
fp= open(FILE_NAME)
fp_lines = fp.readlines()
fp.close()
counter = collections.Counter()
for lines in fp_lines:
    words = lines.split()
    counter[words[0]] += 1
summary=0
for key,value in counter.items():
    summary = summary + value
summary = summary/len(counter)
print(summary)