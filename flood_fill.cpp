#include <bits/stdc++.h>
using namespace std;

// Time Complexity:O(M*N)
class Solution
{
public:
    void dfs(int sr, int sc, vector<vector<int>> &ans, int newColor, int iniCol, vector<vector<int>> &image)
    {
        int dx[] = {-1,
                    0,
                    1,
                    0};
        int dy[] = {0,
                    1,
                    0,
                    -1};

        ans[sr][sc] = newColor;

        int n = image.size();
        int m = image[0].size();

        for (int i = 0; i < 4; i++)
        {
            int sri = sr + dx[i];
            int sci = sc + dy[i];

            if (sri >= 0 && sci >= 0 && sri < n && sci < m && ans[sri][sci] != newColor && image[sri][sci] == iniCol)
            {
                dfs(sri, sci, ans, newColor, iniCol, image);
            }
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {

        int iniCol = image[sr][sc];

        vector<vector<int>> ans = image;

        dfs(sr, sc, ans, newColor, iniCol, image);

        return ans;
    }
};

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<int>> image{
        {1, 1, 1},
        {1, 1, 0},
        {1, 0, 1}};

    // sr = 1, sc = 1, newColor = 2
    Solution obj;
    vector<vector<int>> ans = obj.floodFill(image, 1, 1, 2);
    for (auto i : ans)
    {
        for (auto j : i)
            cout << j << " ";
        cout << "\n";
    }

    return 0;
}