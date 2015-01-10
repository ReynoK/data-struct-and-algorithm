#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const int maxSize = 10;
char combineStr1[2*maxSize+1];
char combineStr2[2*maxSize+1];

int compare(const void * str1,const void *str2){
	strcpy(combineStr1,*(char**)str1);
	strcat(combineStr1,*(char**)str2);

	strcpy(combineStr2,*(char**)str2);
	strcat(combineStr2,*(char**)str1);

	return strcmp(combineStr1,combineStr2);
}

void printMiniNumber(int *arr,int length){
	if(arr==NULL || length<=0)
		return;
	// cout<<"test"<<endl;
	char ** strings = (char**)(new char*[length]);
	for(int i=0;i<length;i++){
		strings[i] = new char[maxSize+1];
		sprintf(strings[i],"%d",arr[i]);
	}
	qsort(strings,length,sizeof(char*),compare);
	for(int i=0;i<length;i++)
		printf("%s",strings[i] );
	printf("\n");
	for(int i=0;i<length;i++)
		delete []strings[i];
	delete []strings;
}

int main(){
	int arr[] = {123,123,123};
	printMiniNumber(arr,sizeof(arr)/sizeof(int));
	return 0;
}