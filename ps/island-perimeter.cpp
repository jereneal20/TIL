class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int i,j, perimeter=0;
        for (i=0;i<grid.size();i++){
            for(j=0;j<grid[0].size();j++){
                if (grid[i][j] == 0) continue;
                if (i == grid.size() -1 || grid[i+1][j] == 0) perimeter++;
                if (i == 0 || grid[i-1][j] == 0) perimeter++;
                if (j == grid[0].size() -1 || grid[i][j+1] == 0) perimeter++;
                if (j == 0 || grid[i][j-1] == 0) perimeter++;
            }
        }
        return perimeter;
    }
};
