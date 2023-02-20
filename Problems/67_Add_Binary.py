
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = len(a) - 1 
        j = len(b) - 1
        extra = 0

        while i >= 0 and j >= 0:
            if extra == 0:
                if a[i] == '0':
                    res = b[j] + res
                elif b[j] == '0':
                    res = a[i] + res
                else:
                    extra = 1
                    res = "0" + res
            else:
                if a[i] == '0':
                    if b[j] == '0':
                        res = "1" + res
                        extra = 0
                    else:
                        res = "0" + res
                        extra = 1
                else:
                    if b[j] == '0':
                        res = "0" + res
                        extra = 1
                    else:
                        res = "1" + res
                        extra = 1
            i -= 1
            j -= 1
        
        if extra == 0:
            if i < 0: 
                res = b[0:(j+1)] + res
            else:
                res = a[0:(i+1)] + res
        else:
            if i < 0 and j < 0:
                return "1" + res
            if i < 0: 
                res = Solution.addBinary(self, a=b[0:(j+1)], b="1") + res 
            else:
                res = Solution.addBinary(self, a=a[0:(i+1)], b="1") + res 
                
        return res

    def addBinaryV2(self, a: str, b: str) -> str:
        return bin(eval(f'0b{a}') + eval(f'0b{b}'))[2:]

a = "100"
b = "110010"
s = Solution()
print("result", s.addBinaryV2(a, b))