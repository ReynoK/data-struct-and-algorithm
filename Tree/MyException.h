#ifndef MYEXCEPTION_H
#define MYEXCEPTION_H
#include <string>
#include <iostream>
using namespace std;

class MyException{
public:
	MyException(string err_msg):err_msg(err_msg){}
	~MyException(){}
	void showMessage(){cout<<err_msg<<endl;}
private:
	string err_msg;
};

#endif