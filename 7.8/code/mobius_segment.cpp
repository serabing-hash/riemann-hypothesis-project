// code/mobius_segment.cpp
// Segmented sieve to compute Möbius mu(n) for [L, R] inclusive.
// Build: g++ -O3 -march=native -std=c++17 mobius_segment.cpp -o mobius_segment
// Usage: ./mobius_segment 1 100000000 mu.bin
#include <bits/stdc++.h>
using namespace std;

static inline void mobius_segment(uint64_t L, uint64_t R, vector<int8_t>& mu){
    uint64_t n = R - L + 1;
    vector<uint64_t> val(n);
    iota(val.begin(), val.end(), L);
    mu.assign(n, 1);
    vector<uint8_t> square(n, 0);

    uint64_t S = (uint64_t)floor(sqrt((long double)R)) + 1;
    vector<uint64_t> primes; primes.reserve(S/10);
    vector<uint8_t> mark(S+1, 0);
    for(uint64_t p=2;p<=S;++p){
        if(!mark[p]){
            primes.push_back(p);
            if (p*p <= S)
                for(uint64_t q=p*p;q<=S;q+=p) mark[q]=1;
        }
    }
    for(uint64_t p: primes){
        uint64_t start = (L + p - 1)/p * p;
        for(uint64_t x=start; x<=R; x+=p){
            size_t i = (size_t)(x - L);
            int k=0;
            while(val[i] % p == 0){ val[i] /= p; ++k; }
            if(k>=2) square[i]=1;
            if(k==1) mu[i] = -mu[i];
        }
    }
    for(size_t i=0;i<n;++i){
        if(val[i] > 1) mu[i] = -mu[i]; // remaining large prime
        if(square[i]) mu[i] = 0;       // not squarefree
    }
}

int main(int argc, char** argv){
    if(argc < 4){
        fprintf(stderr, "Usage: %s L R output.bin\n", argv[0]);
        return 1;
    }
    uint64_t L = strtoull(argv[1], nullptr, 10);
    uint64_t R = strtoull(argv[2], nullptr, 10);
    string out = argv[3];
    vector<int8_t> mu;
    mobius_segment(L, R, mu);
    FILE* f = fopen(out.c_str(), "wb");
    if(!f){ perror("fopen"); return 2; }
    fwrite(mu.data(), sizeof(int8_t), mu.size(), f);
    fclose(f);
    return 0;
}
