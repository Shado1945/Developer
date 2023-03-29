#include <iostream>
using namespace std;

int main() {
	//Declare Variables
	double test1,test2,test3,average;
	
	//Get test1
	cout << "Enter the score for test1:" << endl;
	cin >> test1;

	//Get test2
	cout << "Enter the score for test2:" << endl;
	cin >> test2;

	//Get test3
	cout << "Enter the score for test3:" << endl;
	cin >> test3;

	//Calculate the average score
	average = (test1 + test2 + test3) / 3;

	//Display average
	cout << "The average is " << average << endl;

	/*
	* If the average is greater than 95
	* congratulate the user
	*/
	if (average > 95)
		cout << "Way to go! Great average!" << endl;

	return 0;
}