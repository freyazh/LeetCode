class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = 0
        resl = []
        l = len(num)

        for i in range(0, l):
            res += num[i] * pow(10, l - i - 1)

        res = res + k
        j = res % 10
        while res > 0:
            resl.insert(0, j)
            res = res // 10
            j = res % 10
        
        return resl