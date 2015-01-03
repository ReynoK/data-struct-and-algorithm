#include "BitOperater.h"
#include <iostream>
using namespace std;

int main(){
	cout<<"19的二进制有"<<BitOperater::numberOf1InBinary1(19)<<"个1"<<endl;
	cout<<"19的二进制有"<<BitOperater::numberOf1InBinary2(19)<<"个1"<<endl;
	cout<<"-19的二进制有"<<BitOperater::numberOf1InBinary1(-19)<<"个1"<<endl;
	cout<<"-19的二进制有"<<BitOperater::numberOf1InBinary2(-19)<<"个1"<<endl;
	cout<<"1024是否是2的整数次幂："<<BitOperater::isPower(1024)<<endl;
	cout<<"1025是否是2的整数次幂："<<BitOperater::isPower(1025)<<endl;
	cout<<"10和15二进制相差的位数："<<BitOperater::changeNumberofBinary(10,15)<<endl;
	return 0;
}