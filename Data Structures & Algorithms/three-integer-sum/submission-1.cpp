class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result; 
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i>0 && nums[i] == nums[i-1]) continue;
            int l = i+1;
            int r = nums.size() - 1;
            int target = -nums[i];
            while (l < r) {
                int curr = nums[l] + nums[r];
                if (target < curr) {
                    r--;
                } else if (curr < target) {
                    l++;
                } else {
                    vector<int> add_result = { nums[i], nums[l], nums[r] };
                    int found = 0; 
                    for(int j=0;j<result.size();j++) 
                        if (result[j] == add_result) found = 1;
                    if (!found) result.push_back(add_result);
                    l++;
                    r--;
                }
            }
        }
        return result;
    }
};
