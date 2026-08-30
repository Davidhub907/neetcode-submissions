class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in my_map:
                my_map[sorted_string] = []
                my_map[sorted_string].append(string)
            else:
                my_map[sorted_string].append(string)
        
        sublists = []
        for lst in my_map.values():
            sublists.append(lst)
        
        return sublists

            