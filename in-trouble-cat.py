#We have a loud meowing cat. The "hour" parameter is the current hour time in the range 1..24. 
#We are in trouble if the cat is meowing before 6 or after 21, if we are in trouble then return true, otherwise false.

def in_trouble(cat_talking, time):
    if(time<6 or time>21) and cat_talking==True:
        return True
    else: 
        return False
    

print(in_trouble(True, 6))
#False
print(in_trouble(True, 11))
#False
print(in_trouble(True, 24))
#True
print(in_trouble(True, 16))
#False
print(in_trouble(False, 4))
#False