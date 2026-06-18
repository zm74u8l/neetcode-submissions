class Solution:
    def lengthOfLongestSubstring(self, s: str):
        d = {}
        count = 0
        left = 0 

        if len(s) == 1:
            return 1

        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

            while d[s[i]] > 1:
                
                d[s[left]] -= 1

                if d[s[left]] == 0:
                    del d[s[left]]

                left += 1
            
            count = max(count, i-left+1)



        return count



        