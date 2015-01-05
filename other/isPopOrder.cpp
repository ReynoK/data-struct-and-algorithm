/*
author:zhainankl
date:2014-01-05
program：输入两个整数序列，第一个序列表示栈的压入顺序，判断第二个序列是否为该栈的弹出顺序
*/

#include <iostream>
#include <stack>
using namespace std;

bool isPopOrder(int *push,int *pop,int length){
	bool possible = false;
	stack<int> intStack;
	if(push!=NULL && pop!=NULL && length>0){
		const int * pushNext = push;
		const int * popNext = pop;
		while(pushNext-push<length){
			//先压入栈，然后比较栈顶和序列第一个元素是否相同
			intStack.push(*pushNext);
			//循环至栈顶和序列第一个数不一致
			while(!intStack.empty() && intStack.top() == *pop){
				pop++;
				intStack.pop();
			}
			pushNext++;
		}
		if(intStack.empty())
			possible = true;
	}
	return possible;
}

int main(int argc, char const *argv[])
{
	int push[] = {1};
	int pop[] = {1};
	cout<<isPopOrder(push,pop,1)<<endl;;
	return 0;
}
