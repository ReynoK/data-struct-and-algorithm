#include <iostream>
using namespace std;

int minNumber(int x,int y,int z);
/*要求：求出按从小到大的顺序的第n个丑数，丑数的定义X,X = 2的指数*3的指数*5的指数，把1当作
第一个丑数
思路：可以从大到小一个一个的判断，但是太慢了，因为很多不是丑数的也判断了，可以通过前面算的
丑数乘以2或3或5来得到新的丑数，因为丑数的定义就是这样，这样可以避免无谓的判断
以空间换时间
*/
int getUglyNumber(int index){
	if(index<=0)
		return 0;
	int * uglyArr = new int[index];
	for(int i=0;i<index;i++){
		uglyArr[i] = 0;
	}
	uglyArr[0] =1;
	int * ptr2 = uglyArr;
	int * ptr3 = uglyArr;
	int * ptr5 = uglyArr;
	int arrIndex = 0;	//已得到的丑数的坐标
	while(arrIndex<index){
		int min = minNumber(*ptr2*2,*ptr3*3,*ptr5*5);//得到比当前丑数大的最小丑数
		
		uglyArr[++arrIndex] = min;	//更新坐标并写入丑数
		while(*ptr2*2<=uglyArr[arrIndex])//得到可以形成比当前丑数还要大的丑数的坐标
			ptr2++;
		while(*ptr3*3<=uglyArr[arrIndex])//得到可以形成比当前丑数还要大的丑数的坐标
			ptr3++;
		while(*ptr5*5<=uglyArr[arrIndex])//得到可以形成比当前丑数还要大的丑数的坐标
			ptr5++;
	}
	int ugly = uglyArr[index-1];
	delete []uglyArr;
	return ugly;
}

int minNumber(int x,int y,int z){
	int temp = x>y?y:x;
	return temp>z?z:temp;
}
int main(int argc, char const *argv[])
{
	cout<<"第6个丑数为："<<getUglyNumber(6)<<endl;
	return 0;
}