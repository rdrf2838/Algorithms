#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <unordered_map>
#include <tuple>
#define MINVAL -5000
#define MAXVAL 10001
using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int log2_floor(unsigned long long i){
    return i? __builtin_clzll(1)-__builtin_clzll(i):-1;
}

int main(){
    int t;cin>>t;
    while(t--){
        int n;cin>>n;
        vi results(n+1);
        for(int i=3;i<=n;i++){
            cout<<"? 1 2 "<<i<<"\n";
            cout.flush();
            cin>>results[i];
        }
        bool same=true;
        for(int i=3;i<n;i++){
            if(results[i]!=results[i+1]){same=false;break;}
        }
        if(same){
            vi results3(n+1);
            for(int i=4;i<=n;i++){
                cout<<"? 1 3 "<<i<<"\n";
                cout.flush();
                cin>>results3[i];
            }
            bool actual_best=true;
            for(auto v:results3){
                if(v>results[0]){actual_best=false;break;}
            }
            if(actual_best){
                cout<<"! 1 2\n";
                continue;
            }
        }
        int best_idx=-1,best_val=-1;
        for(int i=3;i<=n;i++){
            if(results[i]>best_val){
                best_val=results[i];
                best_idx=i;
            }
        }
        vi indices;
        for(int i=1;i<=n;i++)if(i!=best_idx)indices.push_back(i);

        vi results2(indices.size());
        for(int i=0;i<indices.size()-1;i++){
            int idx_a=indices[i],idx_b=indices[i+1];
            cout<<"? "<<best_idx<<" "<<idx_a<<" "<<idx_b<<"\n";
            cout.flush();
            cin>>results2[i];
        }

        int maxval=-1;
        for(auto v:results2)maxval=max(maxval,v);
        vi maxval_indices;
        for(int i=0;i<results2.size();i++){
            if(results2[i]==maxval)maxval_indices.push_back(indices[i]);
        }
        if(maxval_indices.size()==1){
            if(maxval_indices[0]==0){
                cout<<"! 0 "<<best_idx<<"\n";
                cout.flush();
            }else{
                cout<<"! "<<maxval_indices[0]+1<<" "<<best_idx<<"\n";
                cout.flush();
            }
        }else{
            cout<<"! "<<best_idx<<" "<<maxval_indices[1]<<"\n";
            cout.flush();
        }

    }
}