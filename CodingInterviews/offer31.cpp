#include <iostream>
using namespace std;

/*要求：寻找和最大的数组的和
思路：从头开始加，若当加到某一个位置，其累加值小于此位置的值，证明在累加下去都比
从这点开始累加要小，所以字数组的累计换成从这点开始，其时间复杂读为O(n),比累加全部的
子数组来判断的O（n的平方）快多了
*/
int FindGreatestSumofSubArray(int *arr,int length){
	if(arr==NULL || length <=0)
		return 0;
	int maxSum = arr[0];
	int tempSum = 0;
	int index = 0;
	while(index<length){
		tempSum+=arr[index];
		//如果累加值比当前值小，换成从这点开始
		if(tempSum<arr[index])
			tempSum = arr[index];
		//看是否有更大的累加值
		if(tempSum>maxSum){
			maxSum = tempSum;
			cout<<"maxSum:"<<maxSum<<endl;
		}
		index++;
	}
	return maxSum;
}

int main(int argc, char const *argv[])
{
	int arr[] = {2,8,1,5,9};
	cout<<"max sum of subarray:"
	<<FindGreatestSumofSubArray(arr,sizeof(arr)/sizeof(int))<<endl;
	return 0;
}