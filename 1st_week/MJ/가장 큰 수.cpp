#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(const int &x, const int &y) {
    return to_string(x) + to_string(y) > to_string(y) + to_string(x);    
}

string solution(vector<int> numbers) {
    string answer = "";
    sort(numbers.begin(), numbers.end(), cmp);
    
    // "0000" = 0
    if (numbers[0] == 0) return "0";
    
    for (int i = 0; i < numbers.size(); ++i) {
        answer += to_string(numbers[i]);
    }
    
    return answer;
}
