'''
11.8.15
Check Permutation: 
	Given two strings, 
	write a method to decide if one is a permutation of the other? 


Time Complexity: 
Space Complexity: 


Permutation: rearrangement of elements in a set 
	ex. dog, god, odg

We need to compare the strings 

Ask about: casing 
'''
def checkPermutation(str1, str2):
	if len(str1) != len(str2): return False
	else: return ''.join(sorted(str1)) == ''.join(sorted(str2))

#sorted - sorts alphabetacally & numerically
#join - join the array into a string 

print checkPermutation("abcq", "bcaa") 




