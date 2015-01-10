#include "../List/List.h"
#include <iostream>
#include <stack>
using namespace std;

/*要求：寻找链表中公共部分第一个点的值，使其接下去的都是相等的
思路：让长链表先前进N步，让两个链表剩余的长度相等
时间复杂度为O(m+n),m，n分别为两个链表的长度，不需要其他空间
*/
int findFirstCommandNode(CList &list1,CList &list2){
	unsigned int listLength1 = list1.getLen();
	unsigned int listLength2 = list2.getLen();
	unsigned diff = 0;
	int commondNodeData = 0;
	List longList = NULL;
	List shortList = NULL;
	//寻找需要先前进的链表
	if(listLength1>listLength2){
		diff = listLength1 - listLength2;
		longList = list1.m_list;
		shortList = list2.m_list;
	}else{
		diff = listLength2 - listLength1;
		longList = list2.m_list;
		shortList = list1.m_list;
	}
	//让长链表先前进
	while(diff!=0){
		longList = longList->next;
		diff--;
	}
	while(longList!=NULL && shortList!=NULL){
		if(longList->data != shortList->data)//只要不等
			//则前面都不是相等部分的开始
			commondNodeData = 0;
		else if(commondNodeData==0){//如果相等且前面没有相等部分，
			//则假设该点为公共部分开始部分
			commondNodeData = longList->data;
		}
		longList = longList->next;
		shortList = shortList->next;
	}
	return commondNodeData;
}

/*思路：既然链表时从头开始遍历的，我们所有寻找的是从尾部开始知道不想等的地方
因此可以先将链表压入栈中，然后弹出，知道弹出的点不一样，此时就是我们说要寻找的
位置，但是要花费两个栈的空间，时间复杂度为也为O(m+n)
*/
int findFirstCommandNode2(CList &list1,CList &list2){
	stack<int> stack1;
	stack<int> stack2;
}


int main(){
	int times = 4;
	while(times--){
		CList list1;
		CList list2;
		list1.travelList();
		list2.travelList();
		cout<<"first commond node:"<<findFirstCommandNode(list1,list2)<<endl;
	}
	return 0;
}