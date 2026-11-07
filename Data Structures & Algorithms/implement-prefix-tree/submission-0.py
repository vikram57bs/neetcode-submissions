class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class PrefixTree:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.is_end=True

    def search(self, word: str) -> bool:
        current=self.root
        for i in word:
            if i in current.children:
                current=current.children[i]
            else:
                return False
        if(current.is_end):
            return True
        else:
            return False
    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for i in prefix:
            if i in current.children:
                current=current.children[i]
            else:
                return False
        return True