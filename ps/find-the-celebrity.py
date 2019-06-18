# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        
        L = 0
        R = n - 1
        while L < R:
            if knows(L, R):
                L += 1
            else:
                R -= 1
        # L -> celebrity?
        for i in range(n):
            if i == L:
                continue
            if knows(L, i):
                return -1
            if not knows(i, L):
                return -1
        return L
    
def find_celebrity(candidates):
    if len(candidates) == 0:
        return -1
    """
    celeb_candidate = list()
    for i in candidates[1:]:
        if knows(candidates[0], i):
            celeb_candidate.append(i)
            
            
    if len(celeb_candidate) == 0:
        # candidates[0] is celeb or no one is celeb
        for i in candidates[1:]:
        	if not knows(i, candidates[0]):
                return -1
        return 0
    """
    
    i = 0
    j = len(candidates) - 1    #
    while i != j:
        if knows(candidates[i], candidates[j]):
			i += 1
        else:
            j -= 1
    
    # i -> celeb?
    for candid in candidates:
        if candidates[i] == candid:
            continue
        if not knows(candid, candidates[i]):
            return -1
    return candidates[i]
            
