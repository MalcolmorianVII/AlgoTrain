
class TrieNode:
    def __init__(self) -> None:
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self,word):
        currentNode = self.root

        for xter in word:
            if not currentNode.children.get(xter):
                return None
            currentNode = currentNode.children[xter]
        return currentNode
    
    def insert(self,word):
        currentNode = self.root

        for xter in word:
            if not currentNode.children.get(xter):
                new_node = TrieNode()
                currentNode.children[xter] = new_node
                currentNode = new_node
            else:
                currentNode = currentNode.children[xter]
        currentNode.children['*'] = None

    def collectWords(self,node=None,word="",words=[]):
        currentNode = node or self.root

        # Iterate through all current child nodes

        for key,childNode in currentNode.children.items():

            if key == "*":
                words.append(word)
            else:
                self.collectWords(childNode,word+key,words)
        return words
    def autocomplete(self,prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectWords(currentNode)

rootNode = TrieNode()
rootNode.children = {'a':TrieNode(),'b':TrieNode(),'c':TrieNode()}
print(rootNode)