//Sale price calculator

#include <iostream>
using namespace std;

int main() {
	double originalPrice, discount, salePrice;
	cout << "Enter the items original price: ";
	cin >> originalPrice;
	discount = originalPrice * 0.2;
	salePrice = originalPrice - discount;

	cout << "The sale price is $" << salePrice << endl;
	return 0;
}