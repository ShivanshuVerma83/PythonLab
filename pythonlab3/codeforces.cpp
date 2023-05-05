#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> a(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        int mx=*max_element(a.begin(),a.end());
        int ans;
        for(int i=0i<n;i++){
            if(a[i]==mx){
                ans=i+1;
                break;
            }
        }
        cout<<ans<<endl;
    }
}