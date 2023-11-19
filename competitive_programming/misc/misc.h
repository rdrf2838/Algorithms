#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int log2_floor(unsigned long long i){
    return i? __builtin_clzll(1)-__builtin_clzll(i):-1;
}

template<class T>
class minstack{
    private:
        stack<pair<T,T>> s;
    public:
        void push(T v){
            if (this->s.empty()) this->s.push({v,v});
            else this->s.push({v,min(this->s.top().second,v)});
        }
        T pop(){
            pair<T,T> p= this->s.top();
            this->s.pop();
            return p.first;
        }
        T minimum() {return this->s.top().second;}
        bool empty(){return this->s.empty();}
};

template<class T>
class minqueue{
    private:
        minstack<T> l,r;
    public:
        void push(T v){r.push(v);}
        T pop(){
            if (this->l.empty()) 
                while (!this->r.empty()) 
                    this->l.push(this->r.pop());
            return l.pop();
        }
        T minimum(){
            if (this->l.empty()||this->r.empty()) 
                return this->l.empty() ? this->r.minimum() : this->l.minimum();
            else return min(this->l.minimum(),this->r.minimum());
        }
        bool empty(){return this->l.empty()&&this->r.empty();}
};

vi rabin_karp(string const& s, string const& t){
    ulli p=1099511628211;
    ulli M=1000000000100011;
    ulli h_s=0;
    int S=s.size(),T=t.size();
    vector<ulli>p_pow(T), h(T+1,0);
    p_pow[0]=1;
    for(int i=1;i<T;i++)p_pow[i]=p*p_pow[i-1];
    for(int i=0;i<T;i++)h[i+1]=h[i]+(t[i]-'a'+1)*p_pow[i];
    for(int i=0;i<S;i++)h_s=h_s+(s[i]-'a'+1)*p_pow[i];
    vi occurences;
    for(int i=0;i+S<=T;i++){
        ulli curr_h=h[i+S]-h[i];
        if(curr_h==h_s*p_pow[i])occurences.push_back(i);
    }
    return occurences;
}
