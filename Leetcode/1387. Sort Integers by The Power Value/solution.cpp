class Solution {
public:
    unordered_map<int, int> mem;

    int compute(int n) {
        if (mem[n] || n == 1) {
            return mem[n];
        }

        int count = 0;
        int power = n;

        while (power != 1) {
            if (power % 2) {
                power = power * 3 + 1;
            }
            else {
                power = power / 2;
            }
            count++;
        }

        mem[n] = count;

        return mem[n];
    }

    int getKth(int lo, int hi, int k) {
        vector<pair<int, int>> arr;

        for (int i = lo; i <= hi; i++) {
            arr.push_back({ compute(i), i });
        }

        sort(arr.begin(), arr.end());
        return arr[k-1].second;
    }
};