def countSubstring(str, sub):
    len1 = len(str)
    len2 = len(sub)

    if (len1==0 or len1<len2):
        return 0;
    if (str[0 : len2] == sub):
        return countSubstring(str[1:],sub) + 1;
 
    # Otherwise, return the count
    # from the remaining index
    return countSubstring(str[1:],sub);



print(countSubstring("he and herself", "he"))
