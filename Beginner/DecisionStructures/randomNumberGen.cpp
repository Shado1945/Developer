#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {

	//Variables
	int randNum;

	//Initialize random number
	srand(time(0));

	cout << "Random number generator" << endl;
	randNum = (rand() % 10) + 1;

	if (randNum < 5)
		cout << "The number " << randNum << " is lower than 5" << endl;
	else if (randNum == 5)
		cout << "The number " << randNum << " is equal to 5" << endl;
	else
		cout << "The number " << randNum << " is greater than 5" << endl;

	return 0;
}