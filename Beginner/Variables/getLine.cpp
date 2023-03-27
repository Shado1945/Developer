/* This is the getline function to read a sentence instead
*  of a one word string
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
	string name;
	string city;

	cout << "Please enter your name and surname:" << endl;
	getline(cin, name);

	cout << "Enter the city name:" << endl;
	getline(cin,city);

	cout << "Hello, " << name << endl;
	cout << "You live in " << city << endl;
	return 0;
}