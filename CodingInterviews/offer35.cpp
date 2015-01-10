#include <iostream>
using namespace std;

/*要求：寻找第一个在字符串中不重复出现的字符
思路：可以遍历一遍，统计字符出现的次数，然后从头在遍历一次并访问统计的数量，直到
其出现次数为1，用哈希表将字符和次数映射，可以字符来实现访问次数。这里我们可以用
字符的ASCII码来当做关键字。时间效率为O(n)和空间效率为O(1)
*/
char findFirstNotReaptingChar(const char * pString){
	if(pString == NULL)
		return '\0';
	const int number = 256;
	int hashTable[number];
	for(int i=0;i<number;i++)
		hashTable[i] = 0;
	const char * temp = pString;
	while(*temp != '\0'){
		hashTable[*(temp++)]++;
	}
	temp = pString;	while(*temp != '\0'){
		if(hashTable[*temp] == 1)
			return *temp;
		temp++;
	}
	return '\0';
}

int main(){
	char * test = "abc";
	cout<<"first not reapeating char:"<<findFirstNotReaptingChar(test)<<endl;
	return 0;
}