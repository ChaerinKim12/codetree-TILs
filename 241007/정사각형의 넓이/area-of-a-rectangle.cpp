#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int square = n*n;
    cout << square << endl;
    if (n<5)
        cout << "tiny"; 
    return 0;
}