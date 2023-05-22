#208 Leetcode Problem URL: https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self):
        self.dic = {}

    def insert(self, word):
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = {}

    def search(self, word):
        cur = self.dic
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False
        if 'end' in cur:
            return True
        return False
        

    def startsWith(self, prefix):
        cur = self.dic
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True

obj = Trie() # Creating object of Trie Class
obj.insert("hello") # Insert "hello" into Trie
obj.insert("hi") # Insert "hi" into Trie
obj.insert("hey") # Insert "hey" into Trie
print(obj.search("hi")) # return True
print(obj.startsWith("he")) # return True
print(obj.startsWith("heyy")) # return False