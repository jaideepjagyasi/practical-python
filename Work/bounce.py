# bounce.py
#
# Exercise 1.5
init_height=100 #meters

for i in range(1,11):
    init_height=init_height * (3/5)
    # print(i,init_height)
    # rounding upto4 digits
    # okay
    print(i,round(init_height,4))
