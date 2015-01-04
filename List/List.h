#ifndef LIST_H
#define LIST_H

typedef struct ListNode{
	int data;
	struct ListNode * next;
}ListNode,*List;

class CList{
public:
	CList();
	~CList();
	void travelList();
	ListNode* findKthToTail(unsigned int k);
	void reverseList();
private:
	void initList();
	void destroyList();
	List m_list;
};

#endif