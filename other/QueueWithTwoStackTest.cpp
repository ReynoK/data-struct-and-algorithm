#include "QueueWithTwoStack.h"

int main(){
	CQueue<char> queue;

	queue.appendTail('a');
	queue.appendTail('b');
	queue.appendTail('c');

	cout<<queue.deleteHead()<<queue.deleteHead()<<queue.deleteHead()<<endl;
	return 0;
}