class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        vector<bool> visited(N, false);
        function<void(int)> Dfs = [&] (int node) {
            if (!visited[node]) {
                visited[node] = true;
                for (auto neigh: rooms[node]) {
                    Dfs(neigh);
                }
            }
        };
        Dfs(0);
        // have we visited all the rooms:
        for (int i = 0; i < N; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }

};