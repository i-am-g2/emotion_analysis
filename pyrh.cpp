#include <iostream>
#include <stdlib.h>
using namespace std;
int main () {
	int x = system("python3 cmnd.py abdh");
	cout <<"Hello "<<x/256;
	return 0;
}