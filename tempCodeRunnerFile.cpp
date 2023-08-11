#include<bits/stdc++.h> 
using namespace std; 

static bool cmp(int a, int b){
    if(a==4) return a>b;
    else return b>a;  
}

int main(){
    int a[] = {4, 3,2,9,7,5}; 
    sort(a, a+6, cmp); 

    for(auto it: a){
        cout<<it<<" "; 
    }

    return 0; 
}