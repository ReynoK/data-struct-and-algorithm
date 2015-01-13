/*
author:zhainankl
created on:2015年1月3号
reference：http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html
		   http://www.blogjava.net/fancydeepin/archive/2013/02/03/395073.html
*/

#include "BitTree.h"
#include <stdio.h>
#include <stdlib.h>
#include <exception>
#include <iostream>
#include <stack>
#include <utility>
#include <queue>
#include "MyException.h"
using namespace std;

BinaryTree::BinaryTree():root(NULL){
	cout<<"开始创建二叉树，以0作为虚节点的值"<<endl;
	createTree(root);
}

BinaryTree::BinaryTree(int *preorder,int *inorder, int length):root(NULL){
	cout<<"根据前序遍历结果和中序遍历结果重建二叉树"<<endl;
	rebuildBitTree(preorder,inorder,length);
}

BinaryTree::~BinaryTree(){
	if(!root)
		return;
	cout<<"开始析构树"<<endl;
	destroyTree(root);
}
//析构过程和后序遍历类似，先析构左右子树，然后析构根节点
void BinaryTree::destroyTree(BitTree &tree){
	if(!tree)
		return;
	if(tree->lchild)
		destroyTree(tree->lchild);
	if(tree->rchild)
		destroyTree(tree->rchild);
	cout<<"析构当前元素为"<<tree->data<<"的节点"<<endl;
	free(tree);
	tree=NULL;
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
/*
思想：根据前序遍历访问的顺序，优先访问根结点，然后再分别访问左孩子和右孩子。即对于任一结点，其可看做是根结点，因此可以直接访问，访问完之后，若其左孩子不为空，按相同规则访问它的左子树；当访问其左子树时，再访问它的右子树。因此其处理过程如下：
对于任一结点P：
1) 访问结点P，并将结点P入栈;
2) 判断结点P的左孩子是否为空，若为空，则取栈顶结点并进行出栈操作，并将栈顶结点的右孩子置为当前的结点P（对p进行相同的操作），循环至1);若不为空，则将P的左孩子置为当前的结点P;
3) 直到P为NULL并且栈为空，则遍历结束。
*/
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
			//所需要的只是遍历其右子树，此节点已无需访问，因此在此处将其弹出栈
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
/*
思想：根据中序遍历的顺序，对于任一结点，优先访问其左孩子，而左孩子结点又可以看做一根结点，
然后继续访问其左孩子结点，直到遇到左孩子结点为空的结点才进行访问，然后按相同的规则访问其右子树。
因此其处理过程如下：
对于任一结点P，
1)若其左孩子不为空，则将P入栈并将P的左孩子置为当前的P，然后对当前结点P再进行相同的处理；
2)若其左孩子为空，则取栈顶元素并进行出栈操作，访问该栈顶结点，然后将当前的P置为栈顶结点的右孩子；
3)直到P为NULL并且栈为空则遍历结束
*/
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
在栈中的顺序是否正确（即是否已经被处理，也可以看作是其左节点是否被处理）。
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

//非递归后序遍历二叉树
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

//广度优先遍历
/*
思想：利用队列先进先出的特点，先让左子树入列，然后让右子树入列
*/
void BinaryTree::breadthFirstVisit(){
	if(!root)
		return;
	queue<BitNode*> bitNodeQueue;
	BitNode * q = root;
	bitNodeQueue.push(q);
	while(!bitNodeQueue.empty()){
		q = bitNodeQueue.front();
		cout<<q->data<<" ";
		bitNodeQueue.pop();
		if(q->lchild) 
			bitNodeQueue.push(q->lchild);
		if(q->rchild)
			bitNodeQueue.push(q->rchild);
	}
}

//根据前序遍历结果和中序遍历结果重建二叉树
/*
思想：前序遍历结果集中第一个元素为子树根节点，中序遍历结果中子树根节点左边为左
子树属于的节点，子树根节点右边的为右子树属于的节点，通过这种思想不断的递归创建
左右子树
*/
void BinaryTree::rebuildBitTree(int *preorder,int *inorder, int length){
	if(preorder==NULL || inorder==NULL || length<=0)	//数据右误
		return;
	if(root)
		throw new MyException("树非空!");
	root = constructBitTree(preorder,preorder+length-1,
							inorder,inorder+length-1);
}
//重建二叉树的子过程
BitTree BinaryTree::constructBitTree(
	int *startPreorder,int *endPreorder,
	int *startInorder, int *endInorder)
{
	EleType root = startPreorder[0];
	BitNode* node = (BitNode*)malloc(sizeof(BitNode));
	node->data = root;
	node->rchild = node->lchild = NULL;

	//当前节点为叶子节点
	if(startPreorder == endPreorder){
		if(startInorder == endInorder)
			return node;
		else
			throw new MyException("Invaild input!");
	}

	//在中序遍历结果中寻找根节点的值
	int *rootInorder = startInorder;
	while(rootInorder<endInorder && (*rootInorder)!=root)
		++rootInorder;
	//当根节点值不存在于中序遍历结果中
	if(rootInorder ==endInorder && (*rootInorder)!=root)
		throw new MyException("Invaild input!");

	//左子树节点数量
	int leftLength = rootInorder - startInorder;
	//前序遍历结果中左子树的右边界
	int *leftEndPreorder = startPreorder + leftLength;
	if(leftLength>0){//如果当前节点存在左子树
		node->lchild = constructBitTree(startPreorder+1,leftEndPreorder,
										startInorder,rootInorder-1);
	}
	//右子树节点数量
	int rightLength = endInorder - rootInorder;
	//前序遍历结果中右子树的左边界
	int *rightStartPreorder = leftEndPreorder + 1;
	if(rightLength>0){//如果当前节点存在右子树
		node->rchild = constructBitTree(rightStartPreorder,endPreorder,
										rootInorder+1,endInorder);
	}
	return node;
}

void BinaryTree::BinaryTree::visit(EleType &data,int level){
	//设置输出的宽度
	int blank = 3*level;
	while(blank--)
		cout<<" ";
	cout<<data<<endl;
}
//包装函数
bool hasTree(BinaryTree &t1,BinaryTree &t2){
	return hasSubTree(t1.root,t2.root);
}
//是否有子树
bool hasSubTree(BitTree t1,BitTree t2){
	bool result = false;
	if(NULL!=t1 && NULL !=t2){
		if(t1->data == t2->data)	//当前节点是否相同
			result = isTree1HasTree2(t1,t2);
		if(!result)
			//查看左子树是否右子树
			result = hasSubTree(t1->lchild,t2);
		if(!result)
			//查看右子树是否右子树
			result = hasSubTree(t1->rchild,t2);
	}
	return result;
}
//利用递归来判断节点时候相等
bool isTree1HasTree2(BitNode * n1,BitNode * n2){
	//递归终结：树2已遍历完毕或有节点不想等
	if(n2 == NULL)	//树t2已经到叶子节点
		return true;
	if(n1 == NULL)	//树1已到叶子结点
		return false;

	if(n1->data != n2->data)	//节点不等
		return false;
	else{						//比较左右子节点
		return isTree1HasTree2(n1->lchild,n2->lchild) &&
				isTree1HasTree2(n2->rchild,n2->rchild);
	}
}

void BinaryTree::mirrorBitTree(){
	mirrorRecursively(root);
}
//递归镜像二叉树
void BinaryTree::mirrorRecursively(BitNode * n1){
	if(!n1)
		return;
	BitNode * temp = n1->lchild;
	n1->lchild = n1->rchild;
	n1->rchild = temp;
	if(n1->lchild)
		mirrorRecursively(n1->lchild);
	if(n1->rchild)
		mirrorRecursively(n1->rchild);
}

//将二叉搜索树转化为双向链表
BitNode * BinaryTree::treeToList(){
	BitNode * lastNode = NULL;
	convertNode(root,lastNode);
	root = NULL;
	//此时lastNode指向尾部，通过循环让其指向头部
	while(lastNode->lchild)
		lastNode = lastNode->lchild;
	return lastNode;
}

//
/*
思想：由于二叉树是有序的，中序遍历可以从小到大访问链表，用lastNode表示前一个（访问的）节点，
在访问当前的同时，转换为链表。整个过程起来就是：将当前访问的节点加入链表，同时更新当前节点为
链表的最后一个，而访问采用中序遍历的形式。
lastNode：当前已经处理好链表的尾节点,即当前节点在双向链表的中的前继节点
*/
void BinaryTree::convertNode(BitNode * node,BitNode* &lastNode){
	if(node == NULL)
		return;
	//使左子树形成双向链表，lastNode指向双向链表的尾部
	if(node->lchild)
		convertNode(node->lchild,lastNode);
	//使当前节点与前继节点连接（相当于中序中的正在访问当前节点）
	//这里的前继节点表示上次访问的最近节点（左子树中的最大值）
	node->lchild = lastNode;
	if(lastNode)
		lastNode->rchild = node;
	//当前节点也与左边形成双向链表，更新当前根节点为链表的最后一个节点
	lastNode = node;
	//处理右子树（访问右子树）
	if(node->rchild)
		convertNode(node->rchild,lastNode);
}




