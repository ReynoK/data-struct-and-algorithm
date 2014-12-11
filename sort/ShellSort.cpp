#include <cstdlib>
#include <cstdio>

void ShellSort(int *a,int length);
void InsertSort(int *a,int length,int incre=1);
void ShellSort2(int *a,int length);

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
	ShellSort2(a,length);
	a[0]=0;
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	
	delete [] temp;
	return 0;
}
//希尔排序
void ShellSort(int *a,int length){
	int i,j;
	int increment = length;//初始增量为length
	while(increment>1){	//增量小于1说明上次的增量小于2，那上次的增量只能为1
		increment = increment/2;		//增量每次为原来的一半
		for(i=1;i<=increment;i++) 		//以增量为间隔的子序列进行插入排序
			InsertSort(a,length,i);
	}
}

//带增量的直接插入排序
void InsertSort(int *a,int length,int incre){
	int i,j;
	for(i=2*incre;i<=length;i+=incre){
		if(a[i]<a[i-incre]){	 
			a[0]=a[i];		 
			for(j=i-incre;j>=1 && a[j]>a[0];j-=incre){
				a[j+incre] = a[j];		 
			} 
			a[j+incre] = a[0];		 
		}
	}
}

void ShellSort2(int *a,int length){
	int i,j;
	int increment=length;
	while(increment>1){
		increment/=2;
		//对后面的数使用插入排序的方法插入前面已排好的子序列
		//对于每个子序列都是从第2个开始的，所以这里的i从increment+1处开始，前面的数都是每个子序列的
		//的第一个数
		for (i=increment+1; i<=length; ++i)
		{
			if(a[i]<a[i-increment]){
				a[0] = a[i];
				for(j=i-increment;j>=0&&a[j]>a[0];j-=increment)
					a[j+increment] = a[j];
				a[j+increment]=a[0];
			}
		}
	}
}