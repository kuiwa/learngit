# -*- coding: utf-8 -*-

file = open("pickle.txt", "w")
import pickle
dict = {"name": "BeginMan", "age": "22"}
pickle.dump(dict, file)
file.close()

test = open("pickle.txt", "r")
print pickle.load(test)
test.close()