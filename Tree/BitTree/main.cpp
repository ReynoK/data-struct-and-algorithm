#include "BitTree.h"
#include <iostream>
using namespace std;

#define SIZE 9

int main(){
	// int preorder[SIZE] = {1,2,4,5,6,3,7,8,9};
	// int inorder[SIZE] = {5,4,6,2,1,8,7,9,3};
	// BinaryTree tree(preorder,inorder,SIZE);
	int preorder1[]  = {1,2,4,5,8,3,6,7,9,10};
	int inorder1[] = {4,2,8,5,1,6,3,9,7,10};
	int preorder2[]  = {5,8};
	int inorder2[] = {8,5};
	BinaryTree tree(preorder1,inorder1,10);
	BinaryTree tree2(preorder2,inorder2,3);
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

	cout<<"广度优先遍历二叉树：";
	tree.breadthFirstVisit();
	cout<<endl;

	cout<<hasTree(tree,tree2)<<endl;
	return 0;
}