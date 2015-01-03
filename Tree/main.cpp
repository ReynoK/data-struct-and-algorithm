#include "BitTree.h"
#include <iostream>
using namespace std;

int main(){
	BinaryTree tree;
	cout<<"前序递归遍历：";
	tree.preorderVisit();
	cout<<endl;
	cout<<"前序非递归遍历：";
	tree.NoRePreorderVisit2();
	cout<<endl;
}