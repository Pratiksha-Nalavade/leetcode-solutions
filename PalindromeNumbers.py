# LeetCode Problem: Palindrome Numbers 
# Difficulty: Easy 
class Solution(object):
    def isPalindrome(self, x):
        org=x
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(org==rev):
            return True
        else:
            return False
