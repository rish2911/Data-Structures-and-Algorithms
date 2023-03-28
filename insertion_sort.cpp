#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> ins_sort(vector<int> input) {
    int siz = input.size();

    for (int i=1;i<siz;i++) {
        int key = input[i];
        int k = i-1;
        while (k>=0 && input[k]>key) {
            input[k+1]=input[k];
            k-=1;
        }
        input[k+1]=key;

    }
    return input;
}
int main() {
    vector<int> inp={11,3,14,5,16};
    inp = ins_sort(inp);
    for (int i=0;i<inp.size();i++){
        cout<<inp.at(i)<<endl;
    }
   
    return 0;
}