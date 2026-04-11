class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> umap;
        umap['('] = ')';
        umap['['] = ']';
        umap['{'] = '}';

        stack<char> st;

        for (int i = 0; i < s.size(); i++) {
            if (umap.count(s.at(i))) {
                st.push(umap[s[i]]);
            } else {
                if (st.size() == 0 || st.top() != s[i]) return false;
                st.pop();
            }
        } 
        if (st.empty()) return true;
        else return false;

    }
};
