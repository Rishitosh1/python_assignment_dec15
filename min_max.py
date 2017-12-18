my_list=[4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
max_value=my_list[0]
min_value=my_list[0]
for each in my_list:
    if(min_value > each):
        min_value=each
    else:
        continue
for each in my_list:
    if(max_value < each):
        max_value=each
    else:
        continue


print('The minimum number in the list is {}'.format(min_value))
print('The maximum number in the list is {}'.format(max_value))