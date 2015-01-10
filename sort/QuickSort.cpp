#include <cstdlib>
#include <cstdio>

void QSort(int *a,int low,int heigh);
int Partition(int *a,int low,int heigh);
void swap(int *a,int m,int n);
//改进的排序算法
void QSort1(int *a,int low,int heigh);
int Partition1(int *a,int low,int heigh);

// int main(int argc, char const *argv[])
// {
// 	//a[0]用作哨兵或临时变量
// 	int a[]={0,5,3,2,34,21,225,76,45,36,24,164,24,75,34,23,56,34,55,15,67,65,34,75,43};
// 	int length = sizeof(a)/sizeof(int)-1;
// 	//辅助数组，因为在排序过程中传入了坐标的范围，每次操作只在一定范围内,不会影响到其他递归，所以可以只用一个辅助数组即可
// 	int *temp = new int[length+1];
// 	//打印未排序数组
// 	for(auto item:a)
// 		printf("%d ",item);
// 	printf("\n");
// 	QSort1(a,1,length);
// 	//打印排序数组
// 	for(auto item:a)
// 		printf("%d ",item);
// 	printf("\n");
// 	delete [] temp;
// 	return 0;
// }


void QSort(int *a,int low,int heigh){
	int pivot;	//枢轴
	//递归到子序列无法再分解
	if(low < heigh){
		pivot = Partition(a,low,heigh);//得到枢轴值，将枢轴值放到合适的位置
		QSort(a,low,pivot-1);	//左子序列
		QSort(a,pivot+1,heigh);	//右子序列
	}
}

int Partition(int *a,int low,int heigh){
	int pivotkey = a[low];		//把第一个参数作为枢轴变量
	while(low<heigh){
		//从表的两端往中间扫描
		while(low<heigh && a[heigh]>=pivotkey )
			heigh--;
		swap(a,low,heigh);	//把比枢轴变量小的放到低端
		while(low<heigh && a[low]<=pivotkey)
			low++;
		swap(a,low,heigh);	//把比枢轴变量大的放到低端
	}
	return low;				//返回枢轴变量坐标
}

void swap(int *a,int m,int n){
	int temp = a[m];
	a[m] = a[n];
	a[n] = temp;
}

void QSort1(int *a,int low,int heigh){
	int pivot;
	while(low < heigh){
		pivot = Partition1(a,low,heigh);
		QSort1(a,low,pivot-1);
		low = pivot+1;			//尾递归，采用迭代，第一次递归后low没用了，所以可以这样赋值，
	}							//下次调用的时候，就等同于Partition1(a,pivot+1,heigh)
}

int Partition1(int *a,int low,int heigh){
	int m = low + (heigh-low)/2;
	int pivotkey;
	//寻找3个值中的中间值，放到最左边
	if(a[low] > a[heigh])
		swap(a,low,heigh);	
	if(a[m] > a[heigh])
		swap(a,m,heigh);
	if(a[low] < a[m])
		swap(a,low,m);
	//将枢轴存到a[0]中
	pivotkey=a[0] = a[low];			
	while(low<heigh){
		while(low<heigh && a[heigh]>=pivotkey)
			heigh--;
		a[low]=a[heigh];//直接替换，而不是交换
		while(low<heigh && a[low]<=pivotkey)
			low++;
		a[heigh]=a[low];//直接替换，而不是交换
	}
	a[low]=a[0];		//将枢轴值放回本应该放的位置
	a[0]=0;
	return low;
}