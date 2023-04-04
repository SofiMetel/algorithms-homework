#1. returns the reverse of a given string.


#def reverse_str(str_before)

def reverse(forwards):
    if len(forwards)==0:
        return forwards
    else: 
        str_new=forwards[0]
        #reverse(forwards[1:])
        return reverse(forwards[1:]) + str_new
    
print(reverse("klara"))
