#include <iostream>
using namespace std;

int main() {
    double ft;
    cin >> ft;
    cout << fixed;
    cout.precision(1);
    ft *= 30.48;
    cout << ft;
    return 0;
}