def palli(string):
    lf=0
    rf=len(string)-1
    while rf>=lf:
        if not string[lf]==string[rf]:
            return False
        lf+=1
        rf-=1
    return True
print(palli('nono'))

# def isPalindrome(string):
# 	left_pos = 0
# 	right_pos = len(string) - 1
	
# 	while right_pos >= left_pos:
# 		if not string[left_pos] == string[right_pos]:
# 			return False
# 		left_pos += 1
# 		right_pos -= 1
# 	return True
# print(isPalindrome('aza')) 
