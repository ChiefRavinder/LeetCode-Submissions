class Solution:
    def ladderLength(self, startWord: str, targetWord: str, wordList: List[str]) -> int:
        words=set(wordList)
        q=deque()
        q.append((startWord,1))
        if startWord in words:
            words.remove(startWord)
        while q:
            curr_word,count=q.popleft()
            if curr_word==targetWord:
                return count
            for i in range(len(curr_word)):
                temp=curr_word[i]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    curr_word=curr_word[:i]+j+curr_word[i+1:]
                    if curr_word in words:
                        q.append((curr_word,count+1))
                        words.remove(curr_word)
                        
                curr_word=curr_word[:i]+temp+curr_word[i+1:]
            # count+=1
        return 0