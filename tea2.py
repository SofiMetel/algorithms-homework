
'''We are having a party where there will be tea and biscuits. 
Return the string outcome of the party from the following options: bad, good, great.

A party is good if both tea and biscuits are at least 5. However, if either tea or biscuits is 
at least double the amount of the other one, the party 
is great. However, in all cases, if either tea or biscuits are less than 5, the party is always bad.'''

def party(tea, candy):
    if (tea>=5 and candy>=5):
        if(tea>=2*candy or candy>=2*tea):
            ans ='great'
        else:
            ans = 'good'
    else:
        ans='bad'
    return ans


print(party(6,8))
print(party(3,8))
print(party(20,6))
print(party(10, 4))