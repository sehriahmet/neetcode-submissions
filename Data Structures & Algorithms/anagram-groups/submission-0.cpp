#include <unordered_map>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> umap;
        for (int i = 0; i < strs.size(); i++) {
            string string_arr(26, 0);
            for (int j = 0; j < strs[i].size(); j++) {
                string_arr[strs[i][j] - 'a'] += 1;
            }
            
            umap[string_arr].push_back(strs[i]);
            
        }
        vector<vector<string>> result; 
        for ( auto entry : umap ) {
            result.push_back(entry.second);
        }
        return result;
    }
};
