/*
author:zhainakl
date:2015-01-04
refer to:剑指offer
目标：数值的整数次方，不考虑大数问题
注意点：
1. 判断各种异常输入
2. 判断指数是否小于0
3. 可以通过保存相同的计算值来加快计算速度
*/

#include <iostream>
using namespace std;

double power(double base,int exponent);
bool equal(double num1,double num2);
double powerWithExponent(double base,unsigned int exponent);
double powerWithExponent2(double base,unsigned int exponent);

int isInvalid=false;

double power(double base,int exponent){
	bool isNegative = false;
	if(equal(base,0.0)){
		if(exponent<0){
			isInvalid = true;
		}
		return 0;
	}
	unsigned int absExpenent = 0;	//处理指数小于0的情况
	if(exponent<0)
		isNegative = true;
	absExpenent = isNegative?(unsigned)(-exponent):(unsigned)(exponent);

	double result = powerWithExponent2(base,absExpenent);

	if(isNegative)
		result = 1.0/result;
	return result;
}

bool equal(double num1,double num2){
	//计算机在存储浮点数时有误差
	return ((num1-num2)<0.000001 && (num1-num2)>-0.000001);
}

//利用普通的循环来计算整数次方
double powerWithExponent(double base,unsigned int exponent){
	double result = 1;
	for(int i=1;i<=exponent;i++)
		result*=base;
	return result;
}

double powerWithExponent2(double base,unsigned exponent){
	if(exponent == 0)
		return 1;
	if(exponent == 1)
		return base;
	//通过a的n次方 ＝ a的n/2次方 * a的n/2次方来计算(n为偶数)
	double result = powerWithExponent2(base,exponent>>1);
	result*=result;
	if(exponent & 0x1)	//判断指数是否为奇数，利用&比取余运算快
		result*=base;
	return result;
}



int main(){
	double base;
	int exponent;
	double result;
	cout<<"请输入base和exponent:";
	while(cin>>base>>exponent){
		result = power(base,exponent);
		if(isInvalid){
			cout<<"底数为0，指数不能为0"<<endl;
			isInvalid = false;
		}else
			cout<<base<<"的"<<exponent<<"次方为:"<<result<<endl;
		cout<<"请输入base和exponent:";

		}
	return 0;
}