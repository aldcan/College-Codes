class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original == reversed_num

# Sample Cases
solution = Solution()

# Test case 1: Palindrome number
x = 121
print(solution.isPalindrome(x))  # Output: True
        
        
