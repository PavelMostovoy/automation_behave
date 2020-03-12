from pprint import pprint

data = [1,2,3,4,3,3,3]

data1 = set(data)

data2 = (1,2,3,4,5,678,66,55)

data3 = {"key1": 23,
         "key2": 34,
         5: "true",
         '5':"false"}
print(data3)

data3[5] = data1

pprint(data3.get(6))

print(data3)

print(data2[1])
