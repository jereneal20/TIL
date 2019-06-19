NOT_VISITED = 0
NOW_VISITING = 1
ALREADY_VISITED = 2

visited_dic = dict()

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        global visited_dic
        visited_dic = dict()
        graph_dic = dict()
        
        for idx, word in enumerate(words):
            for ch in word:
                visited_dic[ch] = NOT_VISITED
                graph_dic[ch] = list()

        for idx, word in enumerate(words[:-1]):
            i = 0
            while i < len(words[idx]) and i < len(words[idx+1]):
                if words[idx][i] != words[idx+1][i]:
                    graph_dic[words[idx][i]].append(words[idx+1][i])
                    break
                if words[idx][i] == words[idx+1][i]:
                    i += 1
        
        # print(visited_dic)
        # print(graph_dic)
        res = ""
        try:
            for key, vals in graph_dic.items():
                res += self.recurse(graph_dic, key)
        except Exception:
            # raise
            return ""
        return res[::-1]

    def recurse(self, graph_dic, key):
        global visited_dic
        res = ""
        
        if visited_dic[key] == NOW_VISITING:
            raise Exception    
        if visited_dic[key] == ALREADY_VISITED:
            return ""
        
        visited_dic[key] = NOW_VISITING
        
        vals = graph_dic[key]
        for val in vals:
            res += self.recurse(graph_dic, val[0])
        
        res += key
        visited_dic[key] = ALREADY_VISITED
        return res
# '''
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"

# '''


# r -> f -> g,
# r -> h -> g

# [
#     "r",
#     "fr",
#     "fh",
#     "fg",
#     "g"
# ]


# r : [t, l]

# r->t->f->g->l->m->h

# rtfg
# rtfglmhg

