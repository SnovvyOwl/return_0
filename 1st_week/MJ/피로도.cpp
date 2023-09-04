#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n, answer = -1;
int visited[8];

void recursive(vector<vector<int>> dungeons, int k, int cnt) {
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0) {
            // 종료 조건
            if (k < dungeons[i][0]) {
                answer = max(answer, cnt);
                continue;  // return; 안되는 이유..
            }
            
            visited[i] = 1;
            recursive(dungeons, k - dungeons[i][1], cnt + 1);
            visited[i] = 0;
            
        }
    }
    
    // 분기가 종료되었을 때 최대값 갱신
    answer = max(answer, cnt);
    return;
}

int solution(int k, vector<vector<int>> dungeons) {
    n = dungeons.size();
    recursive(dungeons, k, 0);
    return answer;
}
