#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int score;
    cin >> score;
    int n;
    n = 80 - score;
    if (score >= 80)
        cout << "pass" << endl;
    else
        cout << n << "more score" << endl;
    return 0;
}