#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#define MAX_N 50000

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end(), greater<>());
    
    for (int i = 0; i < people.size(); ++i) {
        if (people[i] + people[people.size() - 1] <= limit) {
            people.pop_back();
        }
        ++answer;
    }
    
    return answer;
}
