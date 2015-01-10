#include "MyException.h"
#include "List.h"
#include <iostream>
#include <cstdlib>
using namespace std;

CList::CList():m_list(NULL){
	initList();
}
//拷贝构造函数
CList::CList(const CList& list):m_list(NULL){
	//当被复制的链表为空
	if(!list.m_list)
		return;
	copyList(list);
}
//拷贝赋值函数
CList& CList::operator=(const CList& list){
	if(list.m_list == m_list)
		return *this;
	destroyList();
	copyList(list);
	return *this;
}
/*复制链表
*/
void CList::copyList(const CList& list){
	ListNode * pre = NULL;
	ListNode * temp = list.m_list;
	while(temp){
		ListNode * node = (ListNode*)malloc(sizeof(ListNode));
		node->data = temp->data;
		node->next = NULL;
		if(m_list==NULL){
			m_list = node;
			pre = m_list;
			temp = temp->next;
			continue;
		}
		pre->next = node;
		pre = pre->next;
		temp = temp->next;
	}
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
	m_list = NULL;	//将头指针置空
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
// /*要求：获得两个链表第一个相同的位置的值
// */
// int CList::findFirstCommondNode(const CList& list){
// 	int listLength1 = getLength(m_list);
// 	int listLength2 = getLength(list.m_list);
// 	int diff = 0;
// 	List listLong = m_list;
// 	List listShort = list.m_list;
// 	if(listLength1>listLength2){
// 		diff = listLength1 - listLength2;
// 	}else{
// 		listLong = list.m_list;
// 		listShort = m_list;
// 		diff = listLength2 - listLength1;
// 	}
// 	cout<<"diff:"<<diff<<endl;
// 	while(diff--){
// 		listLong = listLong->next;
// 	}
// 	while(listLong!=NULL && listShort!=NULL && listShort!=listLong){
// 		listLong = listLong->next;
// 		listShort = listShort->next;
// 	}
// 	if(listLong)
// 		return listLong->data;
// 	else
// 		return 0;
// }

unsigned int CList::getLen(){
	return getLength(m_list);
}


unsigned int CList::getLength(const List& listHead){
	unsigned int len = 0;
	List temp = listHead;
	while(temp){
		len++;
		temp=temp->next;
	}
	return len;
}





// int main(int argc, char const *argv[])
// {
// 	CList list;
// 	cout<<"list:";
// 	list.travelList();
// 	CList list2(list);
// 	cout<<"list2:";
// 	list2.travelList();
// 	// cout<<"commonNodeValue:"<<list.findFirstCommondNode(list2)<<endl;;
// 	// list.travelList();
// 	// cout<<"list2:";
// 	// list2.travelList();
// 	// list2 = list;
// 	// list.reverseList();
// 	// cout<<"list2:";
// 	// list2.travelList();
// 	// cout<<"list lenght:"<<list2.getLen()<<endl;

// 	// int k;
// 	// ListNode *temp=NULL;
// 	// cout<<"所寻找的节点的倒数位置：";
// 	// cin>>k;
// 	// if((temp = list.findKthToTail(k))!=NULL)
// 	// 	cout<<temp->data<<endl;
// 	return 0;
// }

