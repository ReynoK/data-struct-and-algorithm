#include <iostream>
#include "../Tree/BitTree/BitTree.h"
using namespace std;

/*要求：求树的深度，即根节点到叶子结点最长路径的长度
*/
int BitTreeDepth(BitTree& root){
	if(root==NULL)
		return 0;
	//本身一层
	int leftDepth = 1;
	int rightDepth = 1;
	if(root->lchild){
		//左子树的深度
		leftDepth+=BitTreeDepth(root->lchild);
	}
	if(root->rchild){
		//右子树的深度
		rightDepth+=BitTreeDepth(root->rchild);
	}
	//比较长度
	return (rightDepth>leftDepth)?rightDepth:leftDepth;
}

/*要求：判断二叉树是否时平衡的
思路：计算左右子树深度，看深度是否相差1以上
缺点：一个节点遍历两次，计算长度一次，判断子树是否平衡一次
*/
bool isBalanced1(BitTree& root){
	if(root==NULL)
		return true;
	//左子树的深度
	int leftDepth = BitTreeDepth(root->lchild);
	//右子树的深度
	int rightDepth = BitTreeDepth(root->rchild);
	int diff = leftDepth-rightDepth;
	if(diff>1 || diff<-1)
		return false;
	return isBalanced1(root->lchild)&&isBalanced1(root->rchild);
}
/*
思路：根据后序遍历，当根节点访问时，其两个子节点已经访问过，可以根据后序遍历的过程
先计算子节点平衡情况，并计算子节点的深度
root：根节点
depth：深度，自底向上计算
*/
bool isBalanced2(BitTree &root,int &depth){
	if(root==NULL){
		depth = 0;	//从叶子节点开始计算
		return true;
	}
	int left,right;//用来分别存储左右字节点的长度
	if(isBalanced2(root->lchild,left)&&
		isBalanced2(root->rchild,right)){
		//整个相当于一个后序遍历，先处理子节点，再处理本身节点
		int diff = left - right;
		if(diff<=1 && diff>=-1){
			//将左右子节点中最长加上1当作是当前节点的大小
			depth = (left>right)?left+1:right+1;
			return true;
		}
	}
	return false;
}

int getTreeDepth(BinaryTree &tree){
	return BitTreeDepth(tree.root);
}

bool IsBalanced(BinaryTree &tree){
	int depth = 0;
	return isBalanced2(tree.root,depth);
}
int main(){
	int preorder1[]  = {1};
	int inorder1[] = {1};
	BinaryTree tree(preorder1,inorder1,sizeof(preorder1)/sizeof(preorder1[0]));
	tree.preorderVisit();
	cout<<endl;
	tree.inorderVisit();
	cout<<endl;
	tree.postorderVisit();
	cout<<endl;
	cout<<"depth:"<<getTreeDepth(tree)<<endl;	
	cout<<"isBalanced:"<<IsBalanced(tree)<<endl;
	return 0;
}

