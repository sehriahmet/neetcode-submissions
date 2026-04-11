class Solution {
public:
    bool isAnagram(string s, string t) {
        int length = s.size();
        if (length != t.size()) return false;
        unordered_map<char, int> umap;

        for (int i = 0; i < length; i++) {
            if (umap.count(s.at(i))) umap[s.at(i)] += 1;
            else umap[s.at(i)] = 1; 
        }
        for (int i = 0; i < length; i++) {
            if (!umap.count(t.at(i))) return false;
            else {
                if (umap[t.at(i)] < 1) return false;
                umap[t.at(i)] -= 1;
            }
        }
        return true;
    }
};
