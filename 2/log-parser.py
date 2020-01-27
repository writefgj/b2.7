import collections
import json

FILE_NAME1 = 'data_500.json'
FILE_NAME2 = 'data_3000.json'
fp= open(FILE_NAME2)
strings = fp.readlines()
fp.close
logs=[]
browse = collections.Counter()
itemId = collections.Counter()
sumprice=0
for i in strings:
	logs.append(json.loads(i))
for i in logs:
	for key,value in i.items():
		if key == 'userAgentName':
			browse[value] += 1
for i in logs:
	if i['eventType']=='itemBuyEvent' and i['detectedDuplicate'] == False and i['detectedCorruption'] == False:
		for key,value in i.items():
			if key == 'item_price':
				sumprice += value
for i in logs:
	if i['eventType']=='itemFavEvent' and i['detectedDuplicate'] == False and i['detectedCorruption'] == False:
		for key,value in i.items():
			if key == 'item_id':
				itemId[value] +=1
# print(len(browse))
# print(sumprice)
print(itemId)