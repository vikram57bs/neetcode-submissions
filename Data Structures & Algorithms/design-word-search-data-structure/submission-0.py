class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    def addWord(self, word: str) -> None:
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.is_end=True
    def search(self, word: str) -> bool:
        def dfs(curr,ind) -> bool:
            if ind==len(word):
                return curr.is_end
            char=word[ind]
            if char==".":
                for i in curr.children:
                    if(dfs(curr.children[i],ind+1)):
                        return True
                return False
            else:
                if char in curr.children:
                    return dfs(curr.children[char],ind+1)
                else:
                    return False
        return dfs(self.root,0)
