class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> umap;
        int l = 0;
        int r = 0;
        int max = 0; 
        for (int i = 0; i < s.size(); i++) {
            umap[s[i]] = 0;
        }
        for (r = 0; r < s.size(); r++) {
            umap[s[r]] += 1; 
            while (l < r && umap[s[r]] > 1) {
                umap[s[l]] -= 1;
                l++;
            }
            if (r-l+1 > max) max = r-l+1;

        }
        return max;
    }
};
