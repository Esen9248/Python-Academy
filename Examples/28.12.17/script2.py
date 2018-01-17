string1 = "Hey (injected  Yo Men"

array = string1.split()
dictionary = { x:x for x in array } #dic comprehantion
print(dictionary)
print(dictionary['(injected'])
