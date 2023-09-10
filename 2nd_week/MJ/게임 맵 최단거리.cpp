#include<vector>
#include<queue>
#include<iostream>
#define MAX_N 100
#define MAX_M 100

using namespace std;

int n, m, visited[MAX_N][MAX_M];
int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, -1, 1};

bool InRange(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int bfs(vector<vector<int> > maps) {
    queue<pair<int, int>> q;
    visited[0][0] = 1;
    q.push({0, 0});
    
    int x, y, nx, ny;
    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        
        // 상대방 진영 (n, m)에 도착했는지 확인
        if (x == n - 1 && y == m - 1) {
            return visited[x][y];
        }
        
        for (int i = 0; i < 4; ++i) {
            nx = x + dx[i];
            ny = y + dy[i];
            // 게임 맵 안에 있고, 벽이 없는 자리, 방문한 적 없는 칸
            if (InRange(nx, ny) && maps[nx][ny] && !visited[nx][ny]) {  
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << visited[i][j] << " ";
        }
        cout << endl;
    }
    // 너비우선탐색이 끝나도 상대방 진영에 도착하지 못했을 때 -1 return
    return -1;
}

int solution(vector<vector<int> > maps)
{
    int answer = 0; 
    n = maps.size();
    m = maps[0].size();
    answer = bfs(maps);
        
    return answer;
}
