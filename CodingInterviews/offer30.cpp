#include <iostream>
#include <set>
#include <functional>
using namespace std;


int Partition(int *a,int low,int heigh);

/*要求：求出数组最小的k个数，这k个数字不一定要排序的
思路：最小的k个数，可以使用快速排序的方法，当坐标为k时左边值是最小的
缺点：需要改变数组
优点：运算时间快，时间复杂度为O(n)
*/
void GetLeastNumbers(int *arr,int length,int k){
	if(arr == NULL || length<=0 || k<=0)
		return;
	int index = Partition(arr,0,length-1);
	int end = length-1;
	int start = 0;
	while(k-1!=index){
		if(index<k-1){
			start = index+1;
			index = Partition(arr,start,end);
		}else{
			end = index-1;
			index = Partition(arr,start,end);
		}
	}
	cout<<"最小的"<<k<<"个数为：";
	for(int i=0;i<k;i++)
		cout<<arr[i]<<" ";
	cout<<endl;
}

/*
思路：用multiset里存k个数，multiset用红黑树来存储，可以很快的得到k个数的最大值，
可以利用通过比较来判断当前数组的值是否可以放入multiset中，
得到set最大值的时间为O(1)，更改set中最大数的时间为O(logk),对于n个输入数字而言，总的时间效率为O(nlogk)
好处：不会修改数组，比较适合大数据处理，因为大数据可能不能一次性把数据全部导入内存
适合n很大，但k很小的场合
*/
void GetLeastNumbers2(int *arr,int length,int k){
	if(arr == NULL || length<=0 || k<=0)
		return;
	multiset< int,greater<int> > set;
	typedef multiset<int,greater<int> >::iterator multiIterator;
	for(int i=0;i<length;i++){
		if(set.size()<k){//multiset中的值的个数小雨k
			set.insert(arr[i]);
		}else if(arr[i]<*(set.begin())){//判断multiset中的最大数是否小于当前数组的数
			set.erase(set.begin());
			set.insert(arr[i]);
		}
	}
	for(multiIterator iter = set.begin();iter!=set.end();iter++)
		cout<<*iter<<" ";
	cout<<endl;
}

int main(){
	int arr[] = {4,5,1,6,2,7,3,8};
	GetLeastNumbers2(arr,sizeof(arr)/sizeof(int),1);
	return 0;
}