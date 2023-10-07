a=["banana","apple",1,33,22]
def is_number(item):
    return isinstance(item,(int))
def extract_numbers_from_list(item):
    return list(filter(is_number,item))
b=extract_numbers_from_list(a)
c=sorted(b)
print(c)
