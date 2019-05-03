class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        int i,j,k;
        vector<string> res(queries.size(), "");
        vector<int> priority(queries.size(), 5);
        for (i=0;i<queries.size();i++) {
            for(j=0;j<wordlist.size();j++) {
                if (queries[i].size() != wordlist[j].size()) {
                    continue;
                }
                int prior = 1;
                for(k=0;k<queries[i].size(); k++) {
                    if (queries[i][k] == wordlist[j][k]) {
                        // exact match
                        prior = max(1, prior);
                    } else {
                        char q1, w1, q2, w2;
                        q1 = queries[i][k] <= 'Z' ? queries[i][k] - 'A': queries[i][k] - 'a';
                        q2 = (q1 == 0 || q1 == 4 || q1 == 8 || q1 == 'o'-'a' || q1=='u'-'a') ? '*' : q1;
                            
                        w1 = wordlist[j][k] <= 'Z' ? wordlist[j][k] - 'A': wordlist[j][k] - 'a';
                        w2 = (w1 == 0 || w1 == 4 || w1 == 8 || w1 == 'o'-'a' || w1=='u'-'a') ? '*' : w1;
                        if (q2 != w2) {
                            prior = 5;
                            break;
                        }
                        if (q1 == w1) {
                            prior = max(2, prior);
                        } else {
                            prior = max(3, prior);
                        }
                        
                    }
                }
                if (k != queries[i].size()) continue;
                if (prior < priority[i]) {
                    priority[i] = prior;
                    res[i] = wordlist[j];
                }
                if (prior == 1) break;
            }
        }
        return res;
    }
};
