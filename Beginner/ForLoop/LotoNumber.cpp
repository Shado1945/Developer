#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {
	srand(time(0));
	cout << "The Lotto numbers are:" << endl;
	for(int i = 0;i <= 5;i++) {
		if(i == 5) {
			cout << "The bonus is: " << (rand() % 60) + 1 << endl;
		}
		else {
			cout << (rand() % 60) + 1 << endl;
		}
	}
}