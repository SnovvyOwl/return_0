#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int n = citations.size();
    sort(citations.begin(), citations.end(), greater<int>());
    
    int i, j;
    for (int i = 0; i < n; ++i) {
        int cnt = i; // cnt = citations[i] 보다 큰 인용수를 가지는 논문 수
        // citations[i]와 같은 인용수를 가지는 논문의 수를 세기
        for (j = i; j < n; ++j) {
            if (citations[j] == citations[i]) {
                    cnt++;
            }
            else break;
        }
        
        if (cnt <= citations[i]) {
            // cout << "cnt= " << cnt << " citations[i]= " << citations[i];
            answer = cnt;
        }
        else {
            i = j - 1;
        }
    }
    return answer;
}
