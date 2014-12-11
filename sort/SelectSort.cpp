#include <cstdlib>
#include <cstdio>

void SelectSort(int *a,int length);
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
	SelectSort(a,length);
	//打印排序数组
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	delete [] temp;
	return 0;
}

void SelectSort(int *a,int length){
	int i,j;
	int min;
	//从前往后
	for(i=1;i<length;i++){
		min = i;//将当前定义为最小值下标
		for(j=i+1;j<=length;j++)
			if(a[min]>a[j])	//若当前值比a[min]小，则将下标值赋给min
				min = j;
		if(min != i)
			swap(a,i,min);

	}
}

void swap(int *a,int m,int n){
	int temp = a[m];
	a[m] = a[n];
	a[n] = temp;
}