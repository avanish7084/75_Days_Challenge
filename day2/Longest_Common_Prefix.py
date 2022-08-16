class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcs(s1,s2,n):
            res=""
            i=0
            while n>0:
                if s1[i]==s2[i]:
                    res+=s1[i]
                    i+=1
                else:
                    break
                n-=1
            
            return res
            
        res=strs[0]
        for i in range(1,len(strs)):
            res=lcs(res,strs[i],min(len(res),len(strs[i])))
        return res
        
        
        
