
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
    def trie_traverse(self,node=None):
        current_node = node or self.root
        for key,childNode in current_node.children.items():
            print(key)
            if key != "*":
                self.trie_traverse(childNode)

    def autocorrect(self,str,node=None,word=""):
        current_node = node or self.root
        if current_node == "*":
            return word
        for key,childNode in current_node.children.items():
            if key == "*":
                return word
            else:
                if str[0] in current_node.children.items():
                    continue
                else:
                    return self.autocorrect(str[1:],childNode,word + key)
        
    

rootNode = TrieNode()
node1 = TrieNode()
node1.children = {'d':"*"}
node2 = TrieNode()
node2.children = {'a':"*"}
node3 = TrieNode()
node3.children = {'o':"*"}
rootNode.children = {'a':node1,'b':node2,'c':node3}

trie = Trie()
trie.root = rootNode

# trie.trie_traverse()
print(trie.autocorrect('ct'))