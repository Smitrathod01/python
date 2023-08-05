dic={
    "a":"smit",
    "b":"rathod",
    "list":[12,34,23,45],
    "c":{'d':'Eng'},
    1:2
}

print(dic['list'])

dic['list']=[13,24,567,765]  #it is mutable means changable 
print(dic)

print(dic['c']['d']) #nested dictionary