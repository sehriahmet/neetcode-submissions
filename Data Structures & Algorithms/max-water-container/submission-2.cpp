class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max = 0;
        int l = 0;
        int r = heights.size() - 1;
        while (l < r) {
            int h;
            if (heights[l] < heights[r]) h = heights[l];
            else h = heights[r];
            int a = (r-l) * h;
            if (a > max) max = a;
            if (heights[l] < heights[r]) {
                l++;
            } else r--;
        }
        return max;
    }
};
