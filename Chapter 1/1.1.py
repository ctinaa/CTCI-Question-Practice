''' 
11.8.15
Is Unique: Implement an algorithm to determine 
	if a string has all unique characters. 
	What if you cannot use additional data structures? 


Ask whether ASCII or Unicode Strings 
Assume there are 128 max unique Characters 
are all the characters in the string unique 

Time Complexity: O(N) 
Space Complexity: O(1)
'''

testString = "abcdefd"

def isUniqueChar(str):
	if len(str) > 128: return False 


	arr = [False] * 128 

	for char in str: 
		if arr[ord(char)] is False: #returns ASCII 
			arr[ord(char)] = True
		else : return False 
	return True 

print isUniqueChar(testString)


