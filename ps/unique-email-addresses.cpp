class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        int i, res = 1;
        if (emails.size() == 0) return 0;
        
        for (i=0;i<emails.size();i++) {
            emails[i] = convert(emails[i]);
        }
        sort(emails.begin(),emails.end());
        for (i=0;i<emails.size()-1;i++) {
            if (emails[i].compare(emails[i+1]) != 0) {
                res += 1;
            }
        }
        return res;
    }
    
    string convert(string a) {
        int i = 0,j = 0;
        string res = "";
        for (i=0;i<a.size();i++) {
            if (a[i] == '@') break;
            if (a[i] == '.') continue;
            if (a[i] == '+') {
                while (a[i] != '@') i++;
                break;
            }
            res += a[i];
        }
        for (;i<a.size();i++) {
            res += a[i];
        }
        return res;
        
    }
};
