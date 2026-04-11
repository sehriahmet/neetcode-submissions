class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> umap;
        int max = 0;
        int l = 0;
        int result = 0;
        for (int i = 0; i < s.size(); i++) {
            umap[s[i]] = 0;
        }
        for (int r = 0; r < s.size(); r++) {
            umap[s[r]] += 1;
            if (max < umap[s[r]]) {
                max = umap[s[r]];
            }
            while (k + max < (r-l+1) && l < r) {
                umap[s[l]] -= 1;
                l++;
            }
            if (result < r-l+1) result = r-l+1;
        }
        return result;
    }
};
