'''
11.10.15
Palindrome Permutation: 
	Given a string, write a function to check 
		if it is a permutation of a palindrome. 
	A Palindrome is a word or phrase that is the same forwards and backwards. 
	A Permutation is a rearrangement of letters. 
	The Palindrome does not need to be limited to just dictionary words.

EXAMPLE: 

Input: Tact Coa 
Output: True (permutations: "taco cat", "atco cta", etc.)

11.13.15
You need to add:  
Check if the Palindrome is even or odd - try to do this in one go

Remember to ask questions
'''
def PalindromePerm(str1):
	#if the string is a Palindrome 
	#Problem: Fix the space issue!  
	if str(str1)[::-1] == str1: return True
	#check if it is a Permutation of a Palendrome 

	else: return False

print PalindromePerm("taco cat") #check if Palindrome shoud be true; right now true
print PalindromePerm("tacocat") #prints true 


