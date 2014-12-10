#include <cstdlib>
#include <cstdio>

void MSort(int *a,int *temp,int s,int e);
void Merge(int *a,int *temp,int s,int m,int e);

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
	MSort(a,temp,0,length);
	//打印排序数组
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	delete [] temp;
	return 0;
}
//递归
void MSort(int *a,int *temp,int s,int e){
	int m;
	//递归至排序集合就剩下一个元素
	if (s == e)
		temp[s] = a[s];
	else{
		m = (s+e)/2;		//分治
		MSort(a,temp,s,m);	//左边有序
		MSort(a,temp,m+1,e);	//右边有序
		Merge(a,temp,s,m,e);	//再将两个合并
	}
}

void Merge(int *a,int *temp,int s,int m,int e){
	int i,j,k,l;
	//从小到大合并两数组
	for(i=s,j=m+1,k=s;i<=m && j<=e;k++){
		if(a[i] > a[j])
			temp[k] = a[j++];
		else
			temp[k] = a[i++];
	}
	//将剩余的数组复制到数组a
	if(i<=m){
		for(l=i;l<=m;l++)
			temp[k++] = a[l];
	}
	if(j<=e){
		for(l=j;l<=e;l++)
			temp[k++]=a[l];
	}
	//将排序后的元素复制到数组a
	for(i=s;i<=e;i++)
		a[i]=temp[i];
}
