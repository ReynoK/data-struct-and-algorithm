/*
autohor:zhainakl
date:2015-1-7
*/
#include <map>
#include <list>
#include <iostream>
using namespace std;

typedef struct{
	int key;
	int data;
}Node;

class CLRUCache{
public:
	CLRUCache(int capacity);
	~CLRUCache();
	void  set(int key,int value);
	int get(int key);
	void print();
private:
	typedef  map<int,list<Node>::iterator>::iterator mapIter;	
	typedef list<Node>::iterator listIter;
	//C++ STL中的容器是以hash实现的，map中存放的是<关键字,关键字对应的迭代器>,
	//map的存在是为了能够在O(1)时间访问数据
	map<int,list<Node>::iterator> m_cacheMap;	
	list<Node> m_cacheList;						//C++ STL中的List是双向list
	int size;									//cache大小		
};





