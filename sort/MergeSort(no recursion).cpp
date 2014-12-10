#include <cstdlib>
#include <cstdio>


void Merge(int *a,int *temp,int s,int m,int e);
void MSort(int *a,int *temp,int length);

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
	//打印排序数组
	MSort(a,temp,length);
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	delete [] temp;
	return 0;
}
//非递归
void MSort(int a[],int *temp,int length){
	int k;
	int i;
	//步长，1-2-4-8-16.....，当k等于数组长度时，代表上一次循环已经将整个数组合并完成。
	for(k=1;k<length;k*=2){				//大小为k的子序列已经排序完		
		for(i=1;i<=length-2*k+1;i+=2*k){	//将2个大小为k的两两合并，为什么到length-2*k+1，因为可能数组大小不是刚好为2k的整数倍。	
			Merge(a,temp,i,i+k-1,i+2*k-1);	//所以当（length-i+1）>=2*k，即最后一次数量如果小于2*k，说明不能用这里的Merge合并，需要在外面合并
		}
		if((length-i+1)>k)			//当(length-i+1)>k，即剩下的数量超过k，说明需要归并最后两个序列，如果小于k，最后的这个序列已经有序
			Merge(a,temp,i,i+k-1,length);
	}
}


void Merge(int *a,int *temp,int s,int m,int e){
	int i,j,k,l;
	for(i=s,j=m+1,k=s;i<=m && j<=e;k++){
		if(a[i] > a[j])
			temp[k] = a[j++];
		else
			temp[k] = a[i++];
	}
	if(i<=m){
		for(l=i;l<=m;l++)
			temp[k++] = a[l];
	}
	if(j<=e){
		for(l=j;l<=e;l++)
			temp[k++]=a[l];
	}
	for(i=s;i<=e;i++)
		a[i]=temp[i];
}

