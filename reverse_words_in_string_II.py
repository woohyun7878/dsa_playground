class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Idea: Reverse the array, then perform sliding window on the next pass
        n = len(s) 
            
        # Reverse array
        for i in range(n // 2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        
        l, r = 0, 0
        while r <= n:
            # time to reverse!
            if r == n or s[r] == ' ':
                for i in range((r - l) // 2):
                    s[l + i], s[r - 1- i] = s[r - 1- i],  s[l + i]
                
                r += 1
                l = r
            else:
                r += 1
        
        return s
                