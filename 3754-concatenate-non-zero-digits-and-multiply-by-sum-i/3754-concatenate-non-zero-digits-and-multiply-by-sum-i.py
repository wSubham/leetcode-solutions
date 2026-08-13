class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        total=0

        for digit in str(n):
            if digit!='0':
                x+=digit
                total+=int(digit)
        if x=="":
            return 0
        return int(x)*total