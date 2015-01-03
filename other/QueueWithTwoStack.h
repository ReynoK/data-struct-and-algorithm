#ifndef QUEUEWITHTWOSTACK_H
#define QUEUEWITHTWOSTACK_H
#include "MyException.h"
#include <stack>
using namespace std;

template<typename T> class CQueue{
public:
	CQueue();
	~CQueue();
	void appendTail(const T& node);
	T deleteHead();
private:
	stack<T> m_s1;
	stack<T> m_s2;
};

template<typename T>
CQueue<T>::CQueue(){

}
template<typename T>
CQueue<T>::~CQueue(){

}

template<typename T>
void CQueue<T>::appendTail(const T& node){
	m_s1.push(node);
}

//向队列中添加元素
/*
思路：由于栈是后进先出，所以在得到队列元素时，可以将栈s1的元素弹出并压入s2，此时
s2的栈顶，相当于队列头。增加元素时，都添加到到s1中，因为无论s2是否为空,s1的元素
都在s2元素的后面，当s2为空时，在进行同样的弹出压入操作即可。
*/
template<typename T>
T CQueue<T>::deleteHead(){
	if(m_s1.empty() && m_s2.empty())
		throw new MyException("empty queue!");
	T temp;
	if(m_s2.empty()){
		while(!m_s1.empty()){
			T &data = m_s1.top();
			m_s2.push(data);
			m_s1.pop();
		}
	}
	temp = m_s2.top();
	m_s2.pop();
	return temp;

}

#endif