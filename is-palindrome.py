
def isPalindrome(str):
   index = 0
   n=len(str)
   smaller = str[1:n-1]
   if (n<=1 ):
      return True
   if((str[index] is str[n-index-1] and isPalindrome(smaller))):
      return True
   return False

str = 'yyyeb'
print(isPalindrome('madam'))