class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if (r<0 or c<0 or r == len(board) or c == len(board[0]) or (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]     # move down the trie
            word += board[r][c]                   # extend the word
            if node.end:
                res.add(word)   

            dfs(r + 1, c, node, word)             # down
            dfs(r - 1, c, node, word)             # up
            dfs(r, c + 1, node, word)             # right
            dfs(r, c - 1, node, word)             # left

            visit.remove((r, c))                  # undo, so other paths can use this cell

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")               # 2. start from every cell

        return list(res)

