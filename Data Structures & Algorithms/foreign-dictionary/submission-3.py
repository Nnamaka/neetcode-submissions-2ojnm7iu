class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        # Build graph edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # False = visited, True = visiting
        result = []


        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char] # True indicates a cycle

            visited[char] = True # Mark as visiting
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True #

            visited[char] = False
            result.append(char)
            return False

        for char in adj:
            if dfs(char):
                return "" # Return empty string if cycle detected

        # DFS appends nodes post-order, so reverse to get topological order
        result.reverse()
        return "".join(result)