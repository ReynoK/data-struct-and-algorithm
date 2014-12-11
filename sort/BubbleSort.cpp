#include <cstdlib>
#include <cstdio>

void BubbleSort(int *a,int length);
void swap(int *a,int m,int n);

int main(int argc, char const *argv[])
{
	//a[0]用作哨兵或临时变量
	int a[]={0,5,3,2,34,21,225,76,45,36,24,164,24,75,34,23,56,34,55,15,67,65,34,75,43};
	int length = sizeof(a)/sizeof(int)-1;
	//辅助数组，因为在排序过程中传入了坐标的范围，每次操作只在一定范围内,不会影响到其他递归，所以可以只用一个辅助数组即可
	int *temp = new int[length+1];
	//打印未排序数组
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	BubbleSort(a,length);
	//打印排序数组
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	delete [] temp;
	return 0;
}

void BubbleSort(int *a,int length){
	int i,j;
	bool flag = true;	//用来优化排序，判断是否需要继续循环
	//从后往前冒泡
	for(i=1;i<length && flag;i++){//只需比较length-1次
		bool flag = false;
		for(j=length;j>i;j--){	//从后往前循环
			if(a[j] < a[j-1]){	//若后面的值小于前面的值，则交换
				swap(a,j,j-1);
				flag=true;		//若剩下的序列是有序的，则不会进入这个if语句，下次将不再循环
			}
		}
	}
}

void swap(int *a,int m,int n){
	int temp = a[m];
	a[m] = a[n];
	a[n] = temp;
}