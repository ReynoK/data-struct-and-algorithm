#include "BitTree.h"
#include <iostream>
using namespace std;

int main(){
	BinaryTree tree;
	cout<<"前序递归遍历：   ";
	tree.preorderVisit();
	cout<<endl;
	cout<<"前序非递归遍历1：";
	tree.NoRePreorderVisit();
	cout<<endl;
	cout<<"前序非递归遍历2：";
	tree.NoRePreorderVisit2();
	cout<<endl;

	cout<<"中序递归遍历：     ";
	tree.inorderVisit();
	cout<<endl;
	cout<<"非递归遍历二叉树1：";
	tree.NoReInorderVisit();
	cout<<endl;
	cout<<"非递归遍历二叉树2：";
	tree.NoReInorderVisit2();
	cout<<endl;
 
	cout<<"后序递归遍历：  ";
	tree.postorderVisit();
	cout<<endl;
	cout<<"后序非递归遍历：";
	tree.NoRePostorderVisit();
	cout<<endl;
	return 0;
}