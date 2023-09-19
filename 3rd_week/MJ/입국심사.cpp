#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long left = 1;
    long long right = 1e18;
    long long mid;
    
    while (left <= right) {
        // mid는 시간. mid 시간 안에 심사를 마칠 수 있는 지 확인
        mid = (right + left) / 2;
        
        long long cnt = 0;
        for (int i = 0; i < times.size(); ++i) {    // 심사관의 수는 10^5 이라 반복문 사용 가능
            cnt += (mid / (long long) times[i]);
        }
        
        // Lower_bound, 처음으로 n 이상을 만족하는 값을 반환
        if (cnt >= n) {
            answer = mid;
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    
    return answer;
}
