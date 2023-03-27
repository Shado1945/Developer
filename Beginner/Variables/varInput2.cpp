#include <iostream>
#include <string>
using namespace std;

int main() {
	string name;
	double payRate;
	int hours;

	cout << "Enter your first name" << endl;
	cin >> name;
	cout << "Enter your hourly pay rate." << endl;
	cin >> payRate;
	cout << "Enter the number of hours worked." << endl;
	cin >> hours;

	cout << "Here are the values that you entered."<<endl;
	cout << name << endl;
	cout << payRate << endl;
	cout << hours << endl;
	return 0;
}