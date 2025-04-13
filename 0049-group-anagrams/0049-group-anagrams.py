class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [word]
            else:
                hashmap[sorted_word].append(word)
        
        res = [value for key, value in hashmap.items()]

        return res  