def cal_y(l):
    for each in l:
        y= 45*each+0.5
        print('The value of y is {0:.2f} when x is {1}'.format(y,each))

x=[1,2.3,5.6,7,78]
print("Given the condition m=45 and c=0.5")
cal_y(x)