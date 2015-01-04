#ifndef BITOPERATER_H
#define BITOPERATER_H
/*位运算
&：与
|：或
^：异或
<<：左移
>>：右移
注意点：
对与>>：无符号数值用0填补最高位，对于有符号数值，正整数用0填补，负整数用1填补
*/

class BitOperater{
public:
	static int numberOf1InBinary1(int);
	static int numberOf1InBinary2(int);
	static bool isPower(int);
	static int changeNumberofBinary(int,int);
};

//求一个数二进制中1的位数：不要用除法，除法的效率比移位低
//普通求法
/*
思路:判断n的最低位是不是1，可以通过先判断最低位是否为1，接着判断次地位是否为1，以此类推
*/
int BitOperater::numberOf1InBinary1(int num){
	int count = 0;
	int flag = 1;
	while(flag){
		if(num&flag)
			count++;
		flag = flag<<1;
	}
	return count;
}

//惊喜求法
/*
思路:当num减去1时，二进制最右边的1变为0，1左边若有0的话，全变成1，可动手算一下
1左边的高位保持不变
*/
int BitOperater::numberOf1InBinary2(int num){
	int count = 0;
	while(num){
		count++;
		num = num & (num-1);
	}
	return count;
}
//判断一个数是否是2的整数次幂
//思路:判断数的二进制数是否只包含一个1
bool BitOperater::isPower(int num){
	return numberOf1InBinary2(num)==1;
}

//求第二个数要变成第二个树所需要的改变二进制的位数
//思路：先求异或，然后求异或后1的位数
int BitOperater::changeNumberofBinary(int a,int b){
	return numberOf1InBinary2(a^b);
}

#endif