#include <iostream>
using namespace std;

//要求：顺时针打印矩阵

void PrintMatrixCircle(int matrix[][4],int columns,int rows,int start){
	int startX = start;
	int startY = start;
	int endX = columns - start - 1;
	int endY = rows - start - 1;

	for(int i=startX;i<=endX;i++)
		cout<<matrix[startY][i]<<" ";
	//打印右列，当中间只有一列时，无需打印
	if(startY<endY)
		for(int i=startY+1;i<=endY;i++)
			cout<<matrix[i][endX]<<" ";
	//打印下列，至少需要两行两列
	if(startX<endX && startY<endY)
		for(int i=endX-1;i>=startX;i--)
			cout<<matrix[endY][i]<<" ";
	//打印左列，至少需要两列三行
	if(startY<endY-1 && startX < endX)
		for(int i = endY-1;i >= startY+1;i--)
			cout<<matrix[i][startX]<<" ";
	cout<<endl;
}

void PrintMatrixClockwise(int matrix[][4],int columns,int rows){
	if(matrix == NULL || columns <=0 || rows <= 0)
		return;
	int start = 0;
	while(columns>start*2 && rows>start*2){
		PrintMatrixCircle(matrix,columns,rows,start);
		start++;
	}
}




int main(int argc, char const *argv[])
{
	int matrix[][4] = {
		{1,2,3,4},
		{5,6,7,8},
		{9,10,11,12},
		{13,14,15,16},
		{17,18,19,20}
	};
	PrintMatrixClockwise(matrix,4,5);
	return 0;
}