#include <iostream>
using namespace std;


/*思路：不用四则运算实现两个整数之和
思路：不能用四则运算，就只能用二进制来实现了，根据二进制运算，我们可以将二进制分为两个过程，
求得不许进位的和的二进制(即1+1=0，1+0=1，0+0=＝,想当于异或)，如6(110)+10(1010),
110^1010 = 1100,在求需进位的位置(即两个都为1的位置，相当于&)，将其求和，(110&1010)<<1=100，
此时又回到相加，相当于递归直到不许进位
*/
int add(int num1,int num2){
	if(num2==0)
		return num1;
	int temp = num1^num2;
	int carry = (num1&num2)<<1;
	// cout<<temp<<endl;
	// cout<<carry<<endl;
	return add(temp,carry);
}

int main(){
	int num1 = -100,num2 = 6;
	cout<<add(num1,num2)<<endl;
	return 0;
}