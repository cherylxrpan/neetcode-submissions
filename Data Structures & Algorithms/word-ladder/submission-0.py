class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        q = deque([beginWord])
        steps = 1
        while q:
            for i in range(len(q)):                    # one level = one more word in the chain
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + c + word[i+1:]
                        if nxt in words:
                            words.remove(nxt)          # mark visited by removing it
                            q.append(nxt)
            steps += 1
        return 0                

        