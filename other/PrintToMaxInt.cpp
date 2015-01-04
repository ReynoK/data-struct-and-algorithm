/*
author:zhainakl
date:2015-01-04
refer to:剑指offer
目标：输入数字n，按顺序打印出从1到最大的n为的十进制树
解决：
1. 利用字符串，防止数过大，数字类型无法处理
注意点：
1.数字前置0不用输出
2.如何快速的判断是否溢出
*/
#include <cstring>
#include <iostream>
using namespace std;

void printToMaxInt(int n);
void printToMaxInt2(int n);
void recursively(char*result,int length,int index);
bool increment(char * result,int length);
void print(char *result,int length);


void printToMaxInt(int n){
	if(n<0)	//位数应大于等于0
		return;
	char * result = new char[n+1];
	memset(result,'0',n+1);
	result[n] = '\0';
	while(increment(result,n))
		print(result,n);
		// cout<<result<<endl;

}

//利用排列组合和递归
void printToMaxInt2(int n){
	if(n<0)	//位数应大于等于0
		return;
	char * result = new char[n+1];
	memset(result,'0',n+1);
	result[n] = '\0';
	recursively(result,n,0);
}
//递归排列，每一位都遍历0-9
void recursively(char*result,int length,int index){
	if(index==length){
		print(result,length);
		return;
	}
	for(int i=0;i<10;i++){
		result[index] = '0'+i;
		recursively(result,length,index+1);//不是index++
	}
}

bool increment(char * result,int length){
	//当最大位数加1时，数的最高位由9->0，可通过判断最高位是否变化来看是否溢出，不需要
	//判断其他位
	bool isOverFlow = false;
	bool isTakeOver = false;//判断是否需要进位
	int bitValue=0;
	for(int i=length-1;i>=0;i--){
		bitValue = (result[i]-'0');
		if(i==length-1)//个位数+1
			bitValue++;

		if(isTakeOver){//判断是否需要进位
			bitValue++;
			isTakeOver=false;
		}

		if(bitValue>=10){
			result[i] = '0'+(bitValue-10);
			isTakeOver = true;
			if(0 == i)
				return false;
		}else{
			result[i] = '0' + bitValue;
			break;
		}
	}
	return true;
}

//用来规范输出
void print(char * result,int length){
	bool isBegin = false;
	for(int i=0; i<length;i++){
		if(!isBegin && result[i]!='0')
			isBegin=true;
		if(isBegin)
			cout<<result[i];
	}
	cout<<endl;
}

int main(int argc, char const *argv[])
{
	printToMaxInt2(3);
	return 0;
}