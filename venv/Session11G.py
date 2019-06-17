cppCode ="""
#include<iostream>
using namespace std;
int main(){
    cout<<"Hello World";
    return 0;
}
"""

print(cppCode)
print(type(cppCode))

file = open("/Users/ishantkumar/Downloads/MyApp.cpp", "w")
file.write(cppCode)
file.close()

print(">> CPP Code Written")

# HW: Create Hello World Programs in
# 10 different computer programming languages
# Ruby, Dart, Kotlin, Scala, JS, Go

# PS: If you can use Inheritance RTP that will be more effective