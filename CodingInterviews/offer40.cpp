#include <iostream>
using namespace std;

/*
要求：寻找数组中只出现一次的数，一个整形数组除了2个数字以外，其他的数字都只出现
了两次，寻找出是哪两个数字，要求时间复杂度为O(n),空间复杂度为O(1)
思路：先考虑如何在只有一个数出现一次的数组中找出这个数，可以利用异或来寻找，因为
a^a=0;b^a^a=b=>可以得到这个数。然后我们可以将数组分为各包含出现一次数的两个部分，
然后各自找出。关键是如何分为两个这样的数组-》当两个数不同时，其c^d!=0，因此我们可以
根据不等于1的那一位来将数组分为两个部分。
*/
void FindAppearOnce(int *arr,int length){
	if(arr==NULL || length<2)
		return;
	int a = 0;
	for (int i = 0; i < length; ++i)
	{
		a^=arr[i];//得到整个数组即只出现一次的两个数的异或结果
	}
	int b = 1;
	while(!(a&b))
		b=b<<1;//寻找两个数从右边开始的第一个不同的位数
	int result1 = 0;
	int result2 = 0;
	for (int i = 0; i < length; ++i)
	{
		//分为两个子数组
		if(arr[i]&b)
			result1^=arr[i];
		else
			result2^=arr[i];
	}
	cout<<"appear once:"<<result1<<" "<<result2<<endl;
}

int main(int argc, char const *argv[])
{
	int arr[] = {4,6};
	FindAppearOnce(arr,sizeof(arr)/sizeof(arr[0]));
	return 0;
}