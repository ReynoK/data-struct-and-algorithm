#include <cstdlib>
#include <cstdio>

void swap(int *a,int i,int j);
void HeapAdjust(int *a,int s,int e);
void HeapSort(int *a,int length);

int main(int argc, char const *argv[])
{
	//a[0]用作哨兵或临时变量
	int a[]={0,5,3,2,34,21,225,76,45,36,24,164,24,75,34,23,56,34,55,15,67,65,34,75,43};
	int length = sizeof(a)/sizeof(int)-1;
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	HeapSort(a,length);
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	return 0;
}

void HeapSort(int *a,int length){
	//create Heap
	int index = 0;
	for(index = length/2; index>0; index--)
		HeapAdjust(a,index,length);
	//start sort
	for(index=length; index>0; index--){
		swap(a,1,index);
		HeapAdjust(a,1,index-1);
	}
}

//a:array
//s:start index
//e:end index
void HeapAdjust(int *a,int s,int e){
	int temp = a[s];
	int j = 2*s;
	for(; j<=e; j*=2){
		if( j<e && a[j] < a[j+1])	//寻找左右子节点中比较大的那个数,j<e是为了防止最后一个节点为左节点
			++j;
		if(temp >= a[j])
			break;		//temp指向的一直不变，因为就是为了将开始的temp插入到合适的位置
		a[s]=a[j];			
		s = j;
	}
	a[s] = temp;
}

void swap(int *a,int i,int j){
	int temp = a[i];
	a[i]=a[j];
	a[j]=temp;
}
