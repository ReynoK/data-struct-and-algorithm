/*
autohor:zhainakl
date:2015-1-7
*/
#include <map>
#include <list>
#include "LRUCache.h"
#include <iostream>
using namespace std;

CLRUCache::CLRUCache(int capacity):size(capacity){}
CLRUCache::~CLRUCache(){}

/*
如果key不在cache中，则将(key,value)插入cache，
若cache已满，则把最近最久未用的链表从cache中删除(O(1));
若key存在，则重置value的值，并放到链表最前端(O(1))
*/
void CLRUCache::set(int key,int value){
	mapIter mapIt =  m_cacheMap.find(key);
	if(mapIt != m_cacheMap.end()){//命中
		listIter listIt = m_cacheMap[key];
		//设置新的节点
		Node newNode;
		newNode.key = key;
		newNode.data = value;
		//删除旧节点
		m_cacheList.erase(listIt);
		m_cacheList.push_front(newNode);
		//
		//更新map中存放的迭代器
		m_cacheMap[key] = m_cacheList.begin();
	}else{//没有命中
		if(m_cacheList.size() == size){//缓存区已满
			//删除尾部元素
			m_cacheMap.erase(m_cacheList.back().key);
			m_cacheList.pop_back();
		}
		Node newNode;
		newNode.key = key;
		newNode.data = value;
		m_cacheList.push_front(newNode);
		m_cacheMap[key]=m_cacheList.begin();
	}
}

int CLRUCache::get(int key){
	mapIter mapIt =  m_cacheMap.find(key);
	//关键字不存在于map中，即不存在关键为key的元素
	if(mapIt == m_cacheMap.end())
		return -1;
	listIter listIt = m_cacheMap[key];
	//设置新的节点
	Node newNode;
	newNode.key = listIt->key;
	newNode.data = listIt->data;
	//删除旧节点
	m_cacheList.erase(listIt);
	m_cacheList.push_front(newNode);
	//
	//更新map中存放的迭代器
	m_cacheMap[key] = m_cacheList.begin();
	return m_cacheMap[key]->data;
}

void CLRUCache::print(){
	listIter it = m_cacheList.begin();
	while(it!=m_cacheList.end()){
		cout<< it->key<<":"<<it->data;
		cout<<endl;
		it++;
	}
}

int main(){
	CLRUCache cache(3);
	cache.set(1,1);
	cache.set(2,2);
	cache.set(3,3);
	cache.get(2);
	cache.get(1);
	cache.set(4,4);
	cache.get(1);
	cout<<cache.get(3)<<endl;
	cache.print();
	return 0;
}
