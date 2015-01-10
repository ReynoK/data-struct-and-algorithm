#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int countOne(char *number);
/*要求：计算1到N中，十进制中1的数量
思路：如21424，可以分别计算万位，千位....，然后加起来即可得到
一个数字n有Olog(n)位，因此这种算法的时间复杂度为Olog(n)
*/
int NumberOf1Between1AndN(unsigned int num){
	char number[50];
	sprintf(number,"%d",num);//将数字转换成字符串，可以方便的分别提取位数
	return countOne(number);
}

int countOne(char *number){
	//判断非法输入
	if(number==NULL || *number<'0' || *number>'9' || *number=='\0')
		return 0;

	int first = *number - '0';//得到最高位
	int length = strlen(number);
	int sum = 0;
	//将数字分开，如21424分为0-20000和200001-21424
	//计算0-20000中10000到19999中1的万的个数为10的（余下的位数的个数）次方，即1Xpower(10,3)
	if(first>1)
		sum += pow(10,length-1);
	//若最高位为1，则最高为出现1的次数就为去掉最高位后，所表示的数的个数
	else if(first==1)
		sum += atoi(number+1)+1;
	//计算初去最高位后，每个位上出现的次数，如00001-20000，为最高位有3中选取方式
	//其余位有10中选择方式，当除最高位每一位固定为1时，计算其他位数的选择方式
	sum += first*(length-1)*pow(10,length-2);
	//200001-21424由于高位固定为2，所以只要计算1-21424的个数，用递归实现
	sum += countOne(number+1);
	return sum;
}	

int main(int argc, char const *argv[])
{
	int test = 21345;
	cout<<"从1到"<<test<<"中的十进制1的数量为："<<NumberOf1Between1AndN(test)<<endl;
	return 0;
}