#include <iostream>
#include <string>
using namespace std;

int main() {
	int age;
	string name,surname;

	cout << "Enter your name." << endl;
	cin >> name;
	cout << "Enter your surname." << endl;
	cin >> surname;
	cout << "Enter your age." << endl;
	cin >> age;

	cout << "Hello " << name << " " << surname << endl;
	cout << "May I presume you " << name << " " << surname << "," << endl;
	cout << "is "<< age << " years old?"<<endl;
	return 0;

}