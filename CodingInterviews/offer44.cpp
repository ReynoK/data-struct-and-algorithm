#include <iostream>
#include <cstdlib>
using namespace std;

/*要求：判断是否为顺子，设A为1，2为2......K为13，大小王为0，大小王可以代替任何数
思路：先排序，然后判断0的数量，在统计排序后相邻数字之间的空缺数目（除0以外的数），然后判断0
的数量是否大于1
*/
int compare(const void *num1,const void *num2){
	return (*(int*)num1)-(*(int*)num2);
}

bool IsContineus(int *arr,int length){
	if(arr==NULL)
		return false;
	//排序
	qsort(arr,length,sizeof(int),compare);
	int zeroConunt = 0;
	bool two = false;
	//统计0的数量
	for(int i=0;i<length;i++)
		if(arr[i]==0)
			zeroConunt++;
	int interval = 0;
	//统计空缺数目
	for(int i=1;i<length;i++){
		//排除0
		if(arr[i-1]!=0){
			//出现对子时，肯定不是顺子，无需判断
			if(arr[i]==arr[i-1]){
				two = true;
				break;
			}else
				interval+=(arr[i]-arr[i-1]-1);
		}
	}
	if(two || interval>zeroConunt)
		return false;
	else
		return true;
}

int main(){
	int arr[] = {1,0,0,0,5};
	int length = sizeof(arr)/sizeof(arr[0]);
	cout<<IsContineus(arr,length)<<endl;
	for(auto item : arr){
		cout<<item<<" ";
	}
	cout<<endl;
	return 0;
}