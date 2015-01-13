#include <iostream>
using namespace std;


void printEquation(int start,int end,int sum);
/*要求：求出递增数组中和为s的两个数字
思路：如果用普通的方法即固定一个遍历另一个，则时间复杂度为O(n的平方)
用两个指针从两段往中间遍历，可以达到O(n)的效果，和过大减少后端指针，和过小
增加前段指针。
*/
void FindNumberWithSum(int *arr,int length,int s){
	if(arr==NULL || length<2)
		return;
	int * p = arr;
	int * q = arr+length-1;
	int sum = 0;
	while(p<q){
		sum = *p + *q;
		if(sum>s)
			q--;	//和过小，减少后端指针
		else if(sum<s)
			p++;	//和过大，增加前端指针
		else{
			cout<<*p <<"+" <<*q <<"="<<s<<endl;
			p++;//放置和不变，造成死循环
		}
	}
}

/*要求：输入一个整数s，输出所有和为s的连续正数序列（至少包含2个数）
思路：由第一题的思路扩展而来，当和大于s时，使前端指针增加（相当于少了一个加数），
当和小于s时，使后端指针增加（相当于增加了一个加数）。
本程序没有用for循环累加序列的值，指针移动相当于增加了一个数或减少了一个数，这样
避免了每次都用for循环计算序列的值
*/
void FindContinousSequenceWithSum(int sum){
	if(sum<3)
		return;
	int middle = (sum+1)>>1;
	int start = 1;
	int end = 2;
	int s = sum-start-end;
	while(start<middle){
		//增加后端指针直到序列的和大于或等于s
		while(s>0 && end<sum){
			end++;
			s-=end;
		}
		//增加前端指针使序列的和小于或等于s
		while(s<0 && start<end){
			s+=start;
			start++;
		}
		if(s==0){
			printEquation(start,end,sum);
			s += start;
			start++;
		}
	}
}

void printEquation(int start,int end,int sum){
		// cout<<"printEquation"<<endl;

	for (int i = start; i < end; ++i)
	{
		cout<<i<<"+";
	}
	cout<<end<<"="<<sum<<endl;
}

int main(){
// 	int arr[] = {1,2,3,4,7,11,12,16};
// 	FindNumberWithSum(arr,sizeof(arr)/sizeof(arr[0]),15);
	FindContinousSequenceWithSum(100);
	return 0;
}