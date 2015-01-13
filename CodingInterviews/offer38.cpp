#include <iostream>
using namespace std;

int GetFirstIndexofK(int *arr,int length,int k){
	int index = -1;
	int middle = 0;
	int low = 0;
	int high = length-1;
	while(low<=high){	//当low<=high时，继续循环
		middle = (low+high)/2;	//获取中间值
		// cout<<"middle:"<<middle<<endl;
		if(arr[middle]==k){
			//当k在数组开头或k与前面的数组元素不等时，此时为k第一次出现的地方
			if(middle==0 || arr[middle-1]!=k){
				index = middle;
				break;
			}else		//不是k第一次出现的位置
				high = middle-1;
		}
		if(arr[middle]>k)
			high = middle-1;
		else if(arr[middle]<k)
			low = middle+1;
	}
	return index;
}
int GetLastIndexofK(int *arr,int length,int k){
	int index = -1;
	int middle = 0;
	int low = 0;
	int high = length-1;
	while(low<=high){
		middle = (low+high)/2;
		// cout<<"middle:"<<middle<<endl;
		//当k在数组尾部或k与后面的数组元素不等时，此时为k最后一次出现的地方
		if(arr[middle]==k){
			if((middle==length-1) || arr[middle+1]!=k){
				index = middle;
				break;
			}else		//不是k最后一次出现的地方
				low = middle+1;
		}
		if(arr[middle]>k)
			high = middle-1;
		else if(arr[middle]<k)
			low = middle+1;
	}
	return index;
}

/*
要求：数字在排序数组中出现的次数
思路：可寻找到数字在数组中最先出现和最后出现的位置，即可得出现的次数
如果用遍历的方法的话，时间复杂度为O(n)
因为是排序的，所以可以利用二分查找，其时间复杂度为O(logn)
*/
int GetNumberofK(int *arr,int length,int k){
	if(arr == NULL || length <=0)
		return 0;
	int first = GetFirstIndexofK(arr,length,k);
	int last = GetLastIndexofK(arr,length,k);
	// cout<<"first:"<<first<<endl;
	// cout<<"last:"<<last<<endl;
	if(first!=-1 && last!=-1){
		return last-first+1; 
	}else
		return 0;
}

int main(){
	int a[] = {1};
	int num = 1;
	cout<<"数"<<num<<"的数目为："<<GetNumberofK(a,sizeof(a)/sizeof(a[0]),num)<<endl;
	return 0;
}