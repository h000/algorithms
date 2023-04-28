class Solution(object):
    def numSimilarGroups(self, strs):
        answer = 0
        self.parents = [i for i in range(len(strs))]
        for x in range(len(strs)):
            for y in range(x + 1, len(strs)):
                if self.isSimilar(strs[x], strs[y]):
                    self.union(x, y)
        
        for x in range(len(self.parents)):
            self.parents[x] = self.getParent(x)
        return len(set((self.parents)))
    

    def getParent(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        y = self.getParent(y)
        x = self.getParent(x)
        self.parents[y] = x

    def isSimilar(self, x, y):
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        return diff <= 2
