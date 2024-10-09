#include <iostream>

using namespace std;

int main() {
    // 변수 선언
    int gender,age;

    // 입력
    cin >> gender;
    cin >> age;

    // gender가 1인지 2인지 판단하기
    if(gender == 0) {
        // gender가 1일 때, age가 19보다 크다면 MAN이, 크지 않다면 BOY가 됩니다.
        if(age >= 19)
            cout << "MAN";
        else
            cout << "BOY";
    }
    else {
        // gender가 2일 때, age가 19보다 크다면 WOMAN이, 크지 않다면 GIRL이 됩니다.
        if(age >= 19)
            cout << "WOMAN";
        else
            cout << "GIRL";
    }
    return 0;
}