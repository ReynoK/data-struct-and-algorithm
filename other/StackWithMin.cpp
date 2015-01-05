#include <iostream>
#include <stack>
#include <cstdlib>
using namespace std;

template<typename T>class StackWithMin{
public:
	// StackWithMin();
	// ~StackWithMin();
	void pop();
	const T& min();
	void push(const T&);
private:
	stack<T> m_data;
	stack<T> m_min;
};

template<typename T>
void StackWithMin<T>::push(const T& data){
	m_data.push(data);
	if(m_data.size()==0 || m_data.top()<data)
		m_min.push(m_data.top());
	else
		m_min.push(data);
}

template<typename T>
const T& StackWithMin<T>::min(){
	if(m_data.size()<=0 || m_min.size()<=0){
		cout<<"栈为空，出错"<<endl;
		exit(-1);
	}	return m_min.top();
}

template<typename T>
void StackWithMin<T>::pop(){
	if(m_data.size()<=0 || m_min.size()<=0){
		cout<<"栈为空，出错"<<endl;
		exit(-1);
	}
	m_min.pop();
	m_data.pop();
}

int main(int argc, char const *argv[])
{
	StackWithMin<int> stack;
	stack.push(1);
	stack.push(2);
	cout<<stack.min()<<endl;
	stack.pop();
	stack.pop();
	stack.pop();
	stack.pop();
	return 0;
}