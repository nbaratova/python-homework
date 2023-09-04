a = 'Oh, it is python'

a_dict = {}
count = 0
for i in a.lower():
    if i in a_dict:
        a_dict[i] = a_dict.get(i)+1
    else:
        a_dict[i] = count+1
print(a_dict)
