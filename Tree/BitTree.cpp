/*
author:zhainankl
created on:2015年1月3号
reference：http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html
*/

#include "BitTree.h"
#include <stdio.h>
#include <stdlib.h>
#include <exception>
#include <iostream>
#include <stack>
#include <utility>
#include "MyException.h"
using namespace std;

BinaryTree::BinaryTree():root(NULL){
	cout<<"开始创建二叉树，以0作为虚节点的值"<<endl;
	createTree(root);
}

//先序创建二叉树
void BinaryTree::createTree(BitTree & node){
	int data;
	scanf("%d",&data);
	if(data == 0)
		node=NULL;
	else{
		node = (BitNode*)malloc(sizeof(BitNode));
		if(!node)
			throw new MyException("create node error!");
		node->data = data;
		createTree(node->lchild);
		createTree(node->rchild);
	}
}
//递归先序遍历二叉树
void BinaryTree::preorderTraversal(BitTree & node,int level){
	if(!node)
		return;
	// visit(node->data,level);
	cout<<node->data<<" ";
	preorderTraversal(node->lchild,level+1);
	preorderTraversal(node->rchild,level+1);
}

//先序递归遍历二叉树的包装
void BinaryTree::preorderVisit(){
	preorderTraversal(root);
}

//中序递归遍历二叉树
void BinaryTree::inorderTraversal(BitTree & node,int level){
	if(!node)
		return;
	inorderTraversal(node->lchild,level+1);
	// visit(node->data,level);
	cout<<node->data<<" ";
	inorderTraversal(node->rchild,level+1);
}
//中序递归遍历二叉树的包装
void BinaryTree::inorderVisit(){
	inorderTraversal(root);
}
//后序递归遍历二叉树
void BinaryTree::postorderTraversal(BitTree & node,int level){
	if(!node)
		return;
	postorderTraversal(node->lchild,level+1);
	postorderTraversal(node->rchild,level+1);
	cout<<node->data<<" ";
	// visit(node->data,level);
}

//中序递归遍历二叉树的包装
void BinaryTree::postorderVisit(){
	postorderTraversal(root);
}

//非递归前序遍历二叉树
void BinaryTree::NoRePreorderVisit(){
	stack<BitNode*> bitNodeStack;
	BitNode *p = root;
	while(p!=NULL || !bitNodeStack.empty()){
		while(p!=NULL){
			cout<<p->data<<" ";
			bitNodeStack.push(p);
			p = p->lchild;
		}
		if(!bitNodeStack.empty()){
			p = bitNodeStack.top();
			//当前栈顶节点已经打印过（访问过了，此处只是为了得到其右子树），
			//所需要的只是遍历其右子树，此节点已无需再用，因此在此处将其弹出栈
			bitNodeStack.pop();
			p = p->rchild;	//相当于每次循环都是遍历一次子树
		}
	}
}
//非递归前序遍历版本2 
void BinaryTree::NoRePreorderVisit2(){
	if(!root)
		return ;
	stack<BitNode*> bitNodeStack;
	BitNode *p = root,*q = NULL;
	bitNodeStack.push(p);
	//思路：前序遍历是先遍历访问根节点，然后在访问左子节点，然后访问右子节点
	//此处栈定总是子树的跟节点，先访问并弹出根节点，由于栈是后进先出的特点，
	//因此先将右节点压入栈中，然后将左节点压入栈中，然后每次循环都先取出栈顶元素，
	//以相同方法处理。
	while(!bitNodeStack.empty()){
		q = bitNodeStack.top();
		cout<<q->data<<" ";
		bitNodeStack.pop();
		if(q->rchild) bitNodeStack.push(q->rchild);
		if(q->lchild) bitNodeStack.push(q->lchild);
	}
}

//非递归中序遍历二叉树
void BinaryTree::NoReInorderVisit(){
	stack<BitNode*> bitNodeStack;
	BitNode * p = root;
	while(p!=NULL || !bitNodeStack.empty()){
		while(p!=NULL){
			bitNodeStack.push(p);
			p = p->lchild;
		}
		if(!bitNodeStack.empty()){
			p = bitNodeStack.top();
			//得到当前栈顶节点，打印当前栈顶节点的值，因为要访问其右子树，此节点已
			//无需在用（已经访问过了），因此将其弹出
			cout<<p->data<<" ";
			bitNodeStack.pop();
			p = p->rchild;
		}
	}
}

//非递归中序遍历二叉树版本2
/*
思想：中序遍历的特点：先访问其左子节点，然后访问根节点，接着访问其右节点。
根据栈的性质（后近先出），中序遍历在栈的顺序应该是从栈底至栈顶依次是右节点，
根节点，左节点，为了得到这样的顺序，设置一个标志位用来标志此节点的左右子节点
在栈中的顺序是否正确（即是否已经被处理，也可以看作是其左节点未处理）。
在程序中，当得到一个节点时，先将其右节点压入栈中，然后压入根节点，最后压入左节点
*/
void BinaryTree::NoReInorderVisit2(){
	if (!root)	//当树为空时退出
		return ;
	//栈存入的类型为pair<节点指针,是否已处理>
	stack< pair<BitNode*,bool> > bitNodeStack;
	BitNode * p = root,*q = NULL;
	bool used;
	bitNodeStack.push( make_pair(p,false));
	while(!bitNodeStack.empty()){
		q = bitNodeStack.top().first;
		used = bitNodeStack.top().second;
		bitNodeStack.pop();
		if(!used){	//判断该节点是否已经被处理
			//未处理，将该节点及其子节点已正确的方式压入栈中
			if(q->rchild) bitNodeStack.push( make_pair(q->rchild,false));
			bitNodeStack.push( make_pair(q,true));
			if(q->lchild) bitNodeStack.push(make_pair(q->lchild,false));
		}
		else{
			cout<<q->data<<" ";
		}
	}
}

//非递归遍历二叉树
/*
思路：类似'非递归中序遍历二叉树'，设置一个表示为用来表示其左右子节点是否已经访问，
（即表示当前与其左右子节点在栈中的顺序是否正确）
*/
void BinaryTree::NoRePostorderVisit(){
	if(!root)	//当树为空时退出
		return;
	//栈存入的类型为pair<节点指针,是否已处理>
	stack< pair<BitNode*,bool> > bitNodeStack; 
	BitNode * p = root;
	bool used;
	bitNodeStack.push( make_pair(p,false));
	while(!bitNodeStack.empty()){	//当栈非空时
		p = bitNodeStack.top().first;
		used = bitNodeStack.top().second;
		bitNodeStack.pop();
		if(!used){//当前节点的数序是否处理
			//将当前跟节点压入栈中，其顺序已正确处理
			bitNodeStack.push( make_pair(p,true));
			if(p->rchild) //左子节点非空时
				bitNodeStack.push( make_pair(p->rchild,false));
			if(p->lchild)	//右子节点非空时
				bitNodeStack.push( make_pair(p->lchild,false));
		}
		else
			cout<<p->data<<" ";
	}
}

void BinaryTree::BinaryTree::visit(EleType &data,int level){
	//设置输出的宽度
	int blank = 3*level;
	while(blank--)
		cout<<" ";
	cout<<data<<endl;
}

