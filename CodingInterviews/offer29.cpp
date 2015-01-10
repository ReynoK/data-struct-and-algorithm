#include <iostream>
using namespace std;
int Partition(int *a,int low,int heigh);

/*要求：数组中超过一半的数字
思路：数组中超过一半的数字在排序后一定是中位数，所以只需要得到排序后数组的
中位数在数组中的数量是否超过一半即可。
缺点：需要更改数组
*/
int MoreThanHalfNum(int *arr,int length){
	if(arr==NULL || length<=0)
		return 0;
	int index = 0;
	int start = 0;
	int middle = length/2;
	int end = length-1;
	while(index != middle){
		if(index<middle){
			start = index+1;
			index = Partition(arr,start,end);
		}else{
			end = index-1;
			index = Partition(arr,start,end);
		}
	}
	int halfNUm = arr[middle];
	int count = 0;
	for(int i=0;i<length;i++){
		if(arr[i] == halfNUm)
			count++;
	}
	if(count<=length/2)
		halfNUm = 0;
	return halfNUm;
}
/*思路：根据数组的特性，超过一半的数字的总和比其他数字的总和要高，因此我们可以
这样做：每次删除数组中不同的数字（不管是否时我们要寻找的数字），
最后剩下来的就是所要的字数。如 1 2 2 4 2 2 4 2 1 2 
过程是这样的：2 4 2 2 4 2 1 2 -> 2 2 4 2 1(删除2 4)-> 2 2 1(删除2 1)->2
*/
int MoreThanHalfNum2(int *arr,int length){
	if(arr==NULL || length<=0)
		return 0;
	int count = 0;	//记录前面所记录的halfNum未被抵消的数目
	int halfNUm = arr[0];
	for (int i = 0; i < length; ++i)
	{
		if(count==0){//当half为0时，证明前面的已经刚好抵消完毕了
			halfNUm = arr[i];
			count++;
			continue;
		}
		if(halfNUm == arr[i])
			count++;
		else
			count--;
	}
	count = 0;
	for(int i=0;i<length;i++){
		if(arr[i] == halfNUm)
			count++;
	}
	if(count<=length/2)
		halfNUm = 0;
	return halfNUm;

}

int main(){
	int arr[] = {2,1,2,2,2,1,3,4,5};
	int halfNUm = MoreThanHalfNum2(arr,sizeof(arr)/sizeof(int));
	if(halfNUm)
		cout<<"出现超过一半的数字为："<<halfNUm<<endl;
	return 0;
}