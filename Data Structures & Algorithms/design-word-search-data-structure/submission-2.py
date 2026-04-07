class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        return self.searchsub(0, self.root, word)

    def searchsub(self, idx: int, node: TrieNode, word: str) -> bool:
        n = len(word)
        if idx == n: return node.end
        ch = word[idx]
        if ch == ".":
            for child in node.children:
                if self.searchsub(idx + 1, node.children[child], word):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.searchsub(idx + 1, node.children[ch], word)
