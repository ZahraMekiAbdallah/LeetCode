class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        pointer = self.root
        for s in word:
            if s not in pointer.children:
                pointer.children[s] = Node()
            pointer = pointer.children[s]
        pointer.is_end = True

    def search(self, word: str) -> bool:
        pointer = self.root
        for s in word:
            if s in pointer.children:
                pointer = pointer.children[s]
            else:
                return False
        return pointer.is_end

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for s in prefix:
            if s in pointer.children:
                pointer = pointer.children[s]
            else:
                return False
        return pointer
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)