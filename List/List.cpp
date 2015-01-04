#include "MyException.h"
#include "List.h"
#include <iostream>
#include <cstdlib>
using namespace std;

CList::CList():m_list(NULL){
	initList();
}

CList::~CList(){
	destroyList();
}

void CList::initList(){
	cout<<"输入数字初始化链表，以0作为结束"<<endl;
	int item;
	ListNode * p = NULL;
	while(cin>>item && item != 0){
		ListNode *node = (ListNode*)malloc(sizeof(ListNode));
		node->data = item;
		node->next = NULL;
		if(!m_list){
			 p = m_list = node;
			 continue;	//	防止当节点只有一个的时候，造成环形
			}
		p->next = node;
		p = p->next;
	}
}

void CList::travelList(){
	ListNode * q = m_list;
	while(q){
		cout<<q->data<<" ";
		q = q->next;
	}
	cout<<endl;
}

void CList::destroyList(){
	if(!m_list)
		return;
	ListNode * q = m_list;
	while(m_list){
		q = m_list;
		m_list = m_list->next;
		free(q);
	}
}
//寻找倒数第k个节点
/*思路：（1）普通思路，得到链表数量（通过访问所有节点），然后找到地n-k+1个节点，花费时间较长
(2)利用两个指针遍历，使第2个指针指向链表的第k个，然后同时增加知道第2指针指针尾节点，然后第1个指针
所指向的就是所要的位置。->提醒：当一个指针不能解决问题时，可以使用两个指针来遍历链表，可以让其中一个
指针走得快一些，或先在链表中走上若干步
*/
ListNode* CList::findKthToTail(unsigned int k){
	if(!m_list ){
		cout<<"链表为空"<<endl;
		return NULL;
	}
	if(k==0)		//避免下面循环-1造成错误
		return m_list;
	ListNode *p=m_list,*q=m_list;
	while(--k){
		q = q->next;
		if(NULL == q){	//链表节点的数量不足k个
			cout<<"节点数量不足"<<endl;
			return NULL;
		}
	}
	while(NULL != q->next){
		q = q->next;
		p = p->next;
	}
	return p;
}
//反转链表
/*
注意点：
1.旧链表中头指针在新链表中的下一个节点为空
*/
void CList::reverseList(){
	if(!m_list)
		return ;
	ListNode * p=NULL,*q = NULL,*r = NULL;
	p = NULL; 	//从NULL开始，可以直接使旧链表第一个指针在新链表中的下一个元素为NULL
	q = m_list;
	while(q){
		r = q->next;
		if(r == NULL)
			m_list = q;
		q->next = p;
		p = q;
		q = r;		
	} 
}


int main(int argc, char const *argv[])
{
	CList list;
	list.travelList();
	list.reverseList();
	list.travelList();
	// int k;
	// ListNode *temp=NULL;
	// cout<<"所寻找的节点的倒数位置：";
	// cin>>k;
	// if((temp = list.findKthToTail(k))!=NULL)
	// 	cout<<temp->data<<endl;
	return 0;
}

