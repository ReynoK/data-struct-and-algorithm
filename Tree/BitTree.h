#ifndef BITTREE_H
#define BITTREE_H

typedef int EleType;

//二叉树节点定义
typedef struct _Node{
	EleType data;
	struct _Node *lchild;
	struct _Node *rchild;
}BitNode,*BitTree;

//tree的类定义
class BinaryTree{
public:
	BinaryTree();
	void createTree(BitTree & node);
	void preorderVisit();
	void inorderVisit();
	void postorderVisit();
	void NoRePreorderVisit();
	void NoRePreorderVisit2();
	void NoReInorderVisit();
	void NoReInorderVisit2();
	void NoRePostorderVisit();
private:
	void visit(EleType &data,int level);
	void preorderTraversal(BitTree & node,int level=0);
	void inorderTraversal(BitTree & node,int level=0);
	void postorderTraversal(BitTree & node,int level=0);
	BitTree root;
};
#endif