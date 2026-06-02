class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        visited = []
        n = len(strs)
        for i in range(n):
            if i not in visited:
                temp = []
                temp.append(strs[i])
                for j in range(i+1, n):
                    if sorted(strs[i]) == sorted(strs[j]) and j not in visited:
                        temp.append(strs[j])
                        visited.append(j)
                ans.append(temp)
        return ans