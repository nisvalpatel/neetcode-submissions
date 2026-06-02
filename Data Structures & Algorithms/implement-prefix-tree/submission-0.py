class TrieNode:
    def __init__(self):
        self.charList = [None] * 26
        self.isWord = False
    
# ord()   <- very important

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.charList[ord(char) - 97] == None:
                temp = TrieNode()
                curr.charList[ord(char) - 97] = temp

            curr = curr.charList[ord(char) - 97]
    
        curr.isWord = True
        




    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.charList[ord(char) - 97] == None:
                return False

            curr = curr.charList[ord(char) - 97]
    
        return curr.isWord


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if curr.charList[ord(char) - 97] == None:
                return False

            curr = curr.charList[ord(char) - 97]
    
        return True
        
        