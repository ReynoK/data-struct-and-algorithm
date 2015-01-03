#ifndef BITTREE_H
#define BITTREE_H

typedef int EleType;

//二叉树节点定义
typedef struct _Node{
	EleType data;
	struct _Node *lchild;
	struct _Node *rchild;
}BitNode,*BitTree;

/*
author:zhainankl
created on:2015年1月3号
reference：http://www.cnblogs.com/dolphin0520/archive/2011/08/25/2153720.html
		   http://www.cnblogs.com/lscheng/archive/2013/09/11/3313947.html
*/

//tree的类定义
class BinaryTree{
public:
	BinaryTree();
	BinaryTree(int*,int*,int);
	~BinaryTree();
	void createTree(BitTree & node);
	void preorderVisit();
	void inorderVisit();
	void postorderVisit();
	void NoRePreorderVisit();
	void NoRePreorderVisit2();
	void NoReInorderVisit();
	void NoReInorderVisit2();
	void NoRePostorderVisit();
	void breadthFirstVisit();
	void rebuildBitTree(int *,int *,int);
private:
	void visit(EleType &data,int level);
	void preorderTraversal(BitTree & node,int level=0);
	void inorderTraversal(BitTree & node,int level=0);
	void postorderTraversal(BitTree & node,int level=0);
	BitTree constructBitTree(int *,int *,int *, int *);
	void destroyTree(BitTree &tree);
	BitTree root;
};
#endif