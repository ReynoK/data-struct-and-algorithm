#include <cstdlib>
#include <cstdio>

void InsertSort(int *a,int length);

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
	InsertSort(a,length);
	//打印排序数组
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	delete [] temp;
	return 0;
}

void InsertSort(int *a,int length){
	int i,j;
	for(i=2;i<=length;i++){
		if(a[i]<a[i-1]){	//如果a[i]大于等于已排序的最大值，则位置不变，否则要在已排序的序列中寻找位置
			a[0]=a[i];		//设置哨兵
			for(j=i-1;j>=1 && a[j]>a[0];j--){
				a[j+1] = a[j];		//序列往后移
			}//退出循环的条件，当前值小于哨兵，或达到数组开头位置为0，所以赋值时的位置为j+1
			a[j+1] = a[0];		//插入到正确位置
		}
	}
}