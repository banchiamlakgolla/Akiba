class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = str(x)
        if number == number[::-1]:
            return True
        else:
            return False


        