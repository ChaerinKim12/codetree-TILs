#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int score;
    cin >> score;
    if (score >= 80)
        cout << "pass" << endl;
    else
        cout << 80-score << "more score" << endl;
    return 0;
}