#include <bits/stdc++.h>

using namespace std;

int twoStacks(long long int x, vector<int> a, vector<int> b) {
    long long int total = 0;
    int moves = 0;
    int i=0,j=0;
    
    while((total <= x) && (i < a.size()) && (j < b.size())) {
        if(a[i] < b[j]) {
            total += a[i];
            moves++;
            // cout << "I moved" << endl;
            i++;
        }
        else if(a[i] > b[j]){
            total += b[j];
            moves++;
            // cout << "J moved" << endl;
            j++;
        }
        else {
            int m = i;
            int n = j;
            while((a[m] == b[n]) && (total <= x) && (m < a.size()) && (n < b.size())) {
                total += a[m];
                moves++;
                m++;
                n++;
            }
            if(total < x) {
                if(m == a.size()) {
                    j = n;
                }
                else if(n == b.size()) {
                    i = m;
                }
                else {
                    if(a[m] < b[n]) {
                        i = m;
                    }
                    else {
                        j = n;
                    }
                }
            }   
        }
    }

    if(total > x) {
        moves--;
    }
    else {
        if(i == a.size()) {
            while((total <= x) && (j < b.size())) {
                total += b[j];
                moves++;
                j++;
            }
        }
        else {
            while((total <= x) && (i < a.size())) {
                total += a[i];
                moves++;
                i++;
            }
        }
        if(total > x) {
            moves--;
        }
    }

   
    
    return moves;
}

int main() {
   
    int g;
    cin >> g;

    for (int g_itr = 0; g_itr < g; g_itr++) {
        vector<int> a;
        vector<int> b;
        
        int i,n,m,num;
        long long int x;
        
        cin >> n >> m >> x;
        
        for(i=0;i<n;i++) {
            cin >> num;
            a.push_back(num);
        }
        
        for(i=0;i<m;i++) {
            cin >> num;
            b.push_back(num);
        }
        
        int result = twoStacks(x, a, b);

        cout << result << "\n";
    }

    return 0;
}

