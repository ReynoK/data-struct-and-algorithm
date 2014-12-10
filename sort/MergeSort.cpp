#include <cstdlib>
#include <cstdio>

void MSort(int *a,int *temp,int s,int e);
void Merge(int *a,int *temp,int s,int m,int e);

int main(int argc, char const *argv[])
{
	//a[0]用作哨兵或临时变量
	int a[]={0,5,3,2,34,21,225,76,45,36,24,164,24,75,34,23,56,34,55,15,67,65,34,75,43};
	int length = sizeof(a)/sizeof(int)-1;
	int *temp = new int[length+1];
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	// HeapSort(a,length);
	MSort(a,temp,0,length);
	for(auto item:a)
		printf("%d ",item);
	printf("\n");
	return 0;
}

void MSort(int *a,int *temp,int s,int e){
	int m;
	if (s == e)
		temp[s] = a[s];
	else{
		m = (s+e)/2;
		MSort(a,temp,s,m);
		MSort(a,temp,m+1,e);
		Merge(a,temp,s,m,e);
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