#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    for (int i = 0; i < progresses.size(); ++i) {
        if ((100 - progresses[i]) % speeds[i] != 0) {
            days.push_back((100 - progresses[i]) / speeds[i] + 1);
        }
        else days.push_back((100 - progresses[i]) / speeds[i]);
    }
    int count = 1;
    int pivot = days[0];
    for (int i = 1; i < progresses.size(); ++i) {
        if (days[i] <= pivot) {
            count++;
        }
        else {
            answer.push_back(count);
            count = 1;
            pivot = days[i];
        }
    }
    answer.push_back(count);
    return answer;
}
