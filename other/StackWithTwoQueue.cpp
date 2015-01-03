#include "StackWithTwoQueue.h"
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	CStack<int> stack;
	stack.push(1);
	stack.push(2);
	stack.push(3);
	cout<<stack.pop()<<endl;
	stack.push(4);
	for(int i=0;i<3;i++)
		cout<<stack.pop();
	cout<<endl;
	return 0;
}