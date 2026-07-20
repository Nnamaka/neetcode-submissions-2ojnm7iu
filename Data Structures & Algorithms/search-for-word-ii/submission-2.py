class TrieNode:
    def __init__(self):
        self.children = {}
        # the "word" will store the complete string at the leaf
        # node instead of a boolean
        self.word = None
    
    def remove_word(self, word: str) -> None:
        """This is a helper function to optimize algorithm by prunning
        words from the trie once found. """

        current = self
        nodes = []
        for char in word:
            if char not in current.children:
                return
            nodes.append((current, char))
            current = current.children[char]

        # Clean up nodes from bottom to top if they have no other children
        for parent, char in reversed(nodes):
            target_node = parent.children[char]
            if not target_node.children and target_node.word is None:
                del parent.children[char]
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        #Step 1: Build the Trie
        root = TrieNode()
        for w in words:
            current = root
            for char in w:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            # mark end of word by storing word string in 'word'
            current.word = w

        ROWS, COLS = len(board), len(board[0])
        result = []

        # step 2: Backtracking DFS function
        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            current_node = parent_node.children[char]

            # If we matched a complete word, save it
            if current_node.word:
                result.append(current_node.word)

                # set to None to prevent adding the same word multiple times
                current_node.word = None

                # Optimization: Prune the word out of the Trie to speed up remaining searches
                root.remove_word(result[-1])

            # mark the cell as visited
            board[r][c] = '#'

            # Explore 4 neighboring directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in current_node.children:
                    dfs(nr, nc, current_node)
            
            # Backtrack: restore the original character
            board[r][c] = char


        # step 3: scan the board to start matching prefixes
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return result
        