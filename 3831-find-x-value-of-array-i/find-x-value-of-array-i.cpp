class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> dp(k, 0);

        for (int num : nums) {
            int a = num % k;

            vector<long long> ndp(k, 0);

            // start a new subarray
            ndp[a]++;

            // extend previous subarrays
            for (int r = 0; r < k; r++) {
                if (dp[r] == 0) continue;
                ndp[(1LL * r * a) % k] += dp[r];
            }

            for (int r = 0; r < k; r++) {
                ans[r] += ndp[r];
            }

            dp = std::move(ndp);
        }

        return ans;
    }
};