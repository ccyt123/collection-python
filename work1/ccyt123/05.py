dict={1:"小明",2:"小红",3:"小华"}
for num in list(dict):
    if num % 2 == 0:
        del dict[num]
print(dict)
