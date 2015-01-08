#ifndef LIST_H
#define LIST_H

typedef struct ListNode{
	int data;
	struct ListNode * next;
}ListNode,*List;

class CList{
public:
	CList();
	CList(const CList&);//拷贝构造函数
	CList& operator=(const CList& list);
	~CList();
	void travelList();
	ListNode* findKthToTail(unsigned int k);
	void copyList(const CList& list);
	void reverseList();
	int findFirstCommondNode(const CList&);
	unsigned int getLen();
private:
	void initList();
	void destroyList();
	unsigned int getLength(const List&);
	List m_list;
};


#endif