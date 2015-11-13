'''
11.12.15
URLify: 
Write a method to replace all spaces in a string with '%20.' 
You may assume that the string has sufficient space 
	at the end to hold the additional characters, 
	and that you are given the "true" length of the string. 
EXAMPLE: "Mr John Smith"
Output: "Mr%20John%20Smith"

Time:  O(n)
Space: O(n)
'''

def word(str):
	str = str.strip()
	str = str.replace('', '%20')
	return str

def main():
	if True: 
		print str("Mr John Smith")

if __name__ == "__main__": 
	main() 
