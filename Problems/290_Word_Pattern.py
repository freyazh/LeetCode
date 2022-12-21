class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s: return False
        patternMap = {}
        s1 = s.split(' ')
        if len(pattern) != len(s1): return False
        for i in range(0, len(pattern)):
            if pattern[i] in patternMap: 
                if patternMap[pattern[i]] != s1[i]:
                    return False 
            else:
                if s1[i] in patternMap.values():
                        return False
                    
                patternMap[pattern[i]] = s1[i]  

        return True
