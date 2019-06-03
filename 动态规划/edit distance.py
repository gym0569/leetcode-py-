class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance=[[i] for i in range(len(word1)+1)]
        distance[0]=[j for j in range(len(word2)+1)]
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                insert=distance[i][j-1]+1
                delete=distance[i-1][j]+1
                replace=distance[i-1][j-1]
                if word1[i-1]!=word2[j-1]:
                    replace+=1
                distance.append(min(insert,delete,replace))
        return distance[-1][-1]
