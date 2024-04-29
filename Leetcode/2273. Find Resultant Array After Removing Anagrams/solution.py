class Solution:
    def check(self,word1: str,word2: str)->bool:
        word1=list(word1)
        word1.sort()
        word2=list(word2)
        word2.sort()
        if word1==word2:
            return 1
        return 0

    def removeAnagrams(self, words: List[str]) -> List[str]:
        lis=[]
        for i in range(len(words)):
            if len(lis)==0 or Solution.check(self,lis[len(lis)-1],words[i])==0:
                lis.append(words[i])
        return lis