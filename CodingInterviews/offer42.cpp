#include <iostream>
#include <cstring>
using namespace std;

/*要求：反转单词顺序，输入一个英文句子，翻转句子中单词的顺序，但单词内字符串的顺序不变，标点符号
与普通字母一样处理。
思路：先将整个字符串反转，然后再饭庄各个单词，如'kang lei'->'iel gnak'->'lei kang's
*/
void ReverStr(char*start,char*end);
void ReverString(char*str){
	if(str==NULL)
		return;
	char * start = str;
	char * end = str;
	//寻找最后一个字符
	while(*(++end)!='\0')
		;
		end--;
	//反转整个字符串
	ReverStr(start,end);
	char *p = start;
	char *q = start;
	//反转各个单词
	while(*p!='\0'){
		//寻找单词左边界
		while((*p) == ' ')
			p++;
		q=p;
		//寻找单词右边界
		while((*q)!=' ' && (*q)!='\0')
			q++;
		q--;
		//反转单词
		ReverStr(p,q);
		//处理下一个单词
		p = q+1;
	}
}

void ReverStr(char*start,char*end){
	char temp;
	//从两端开始互换
	while(start<end){
		temp = *start;
		*start = *end;
		*end = temp;
		start++;
		end--;
	}
}

/*要求：左旋转，就是把字符串前面的若干字符转移到字符串的尾部。如'abcdef'->2->'cdefab'
思路：现将整个字符串旋转，然后在分别以旋转的个数为界分别反转两边字符串如'abcdef'->'fedcba'
->'cdefab'
*/
void LeftRotateString(char*str,int k){
	if(str == NULL || k < 0)
		return;
	int length = strlen(str);
	k = k%length;
	char * start = str;
	char * end = start+length-1;
	ReverStr(start,end);
	char *middle = end-k;
	ReverStr(start,middle);
	ReverStr(middle+1,end);
}

int main(){
	char name[] = "abcdefg";
	LeftRotateString(name,10);
	cout<<"reverse:"<<name<<endl;
}