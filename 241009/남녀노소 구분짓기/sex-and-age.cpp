#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int age, gen;
    cin >> age;
    cin >> gen;
    if ((age<=19) && (gen==0))
    cout << "BOY";
    else if ((age<=19) && (gen==1))
    cout << "GIRL";
    else if ((age>=19) && (gen==0))
    cout << "MAN";
    else
    cout << "WOMAN";
    return 0;
}