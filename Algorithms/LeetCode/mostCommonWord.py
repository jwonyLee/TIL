class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w]', ' ', paragraph.lower()).split()
        print(words)
        dic = dict()
        
        for word in words:
            if word not in banned:
                dic[word] = dic.get(word, 0) + 1
        
        return max(dic.keys(), key=lambda x: dic[x])