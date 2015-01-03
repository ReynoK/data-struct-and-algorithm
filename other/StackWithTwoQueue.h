#ifndef STACKWITHTWOQUEUE_H
#define STACKWITHTWOQUEUE_H
#include <queue>
#include "MyException.h"
using namespace std;

template<typename T> class CStack{
public:
	CStack(){};
	~CStack(){};
	T pop();
	void push(const T& node);
private:
	queue<T> m_queue1;
	queue<T> m_queue2;
};

template<typename T>
T CStack<T>::pop(){
	queue<T> *tempQueue=NULL,*popQueue = NULL;
	if(m_queue1.empty()){
		tempQueue = &m_queue1;
		popQueue = &m_queue2;
	}else{
		tempQueue = &m_queue2;
		popQueue = &m_queue1;
	}
	if(popQueue->empty())
		throw new MyException("empty stack!");
	else{
		while(popQueue->size()!=1){
			T& temp = popQueue->front();
			tempQueue->push(temp);
			popQueue->pop();
		}
		T& temp = popQueue->front();
		popQueue->pop();
		return temp;
	}
}

//压入栈
/*
当有一个队列为非空时，向非空队列压入元素，若两者都为空，则向m_queue2中压入元素
*/
template<typename T>
void CStack<T>::push(const T& node){
	if(m_queue1.empty()){
		m_queue2.push(node);
	}else{
		m_queue1.push(node);
	}
}


#endif 