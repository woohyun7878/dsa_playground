class TrieNode:
    def __init__(self, is_word = False):
        self.children = dict()
        self.is_word = is_word
            
class Trie:      
    def __init__(self):
        self.root = TrieNode(False)
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True 

    def find_pre(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur
    
    def has_word(self, word):
        node = self.find_pre(word)
        return node and node.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Naive DFS: T(n) = 3T(n-1) + 1 --> O(N * 3^N) * len(words); This is not going to fly 
        
        Optimization:
        We can halt recursion if current prefix does not exist in any of the words in the list.
        We can do this in constant time using a trie data structure. 
    
        """
        # Add all words into a trie 
        trie = Trie()
        for word in words:
            trie.add_word(word)
            
        # dfs function to check if prefix exists:
        ret = set()
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(r, c, letters = []):
            if (r, c) in visited:
                return 
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            
            # Prologue            
            visited.add((r, c))
            letters.append(board[r][c])
            
            # Early Stop
            word = ''.join(letters)
            if not trie.find_pre(word):
                visited.remove((r, c))
                letters.pop()
                return 
            
            # Target word found
            if trie.has_word(word):
                ret.add(word)
            
            # Recurse through next choices
            dfs(r+1, c), dfs(r-1, c)
            dfs(r, c+1), dfs(r, c-1)
            
            # Epilogue
            visited.remove((r, c))
            letters.pop()
            
            
        # recurse beginning at each block:
        for r in range(m):
            for c in range(n):
                
                # dfs or bfs to see if we need to halt 
                dfs(r, c)
        
        
        return list(ret) 
        
        
        
        
        
        
    