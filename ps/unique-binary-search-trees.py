class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_table = list()
        dp_table.append(1)
        dp_table.append(1)
    
        for i in range(2, n+1):
            sum = 0
            for j in range(i):
                sum += dp_table[j]*dp_table[i-j-1]
            dp_table.append(sum)

        return dp_table[n]
        
