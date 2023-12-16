#include <iostream>

using namespace std;

int main()
{
    long num1, num2;

    cout << "\n\nThis program adds two integers."
            "\n\nEnter your first integer: ";
    cin >> num1;

    cout << "\nEnter your second integer: ";
    cin >> num2;

    cout << "\nThe sum is " << num1 + num2 << "!\n\n";

    return 0;
}