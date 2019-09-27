#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

vector<int> makePrimes(int n, int q) {
    
    int i,j;
    vector<int> primes;
    vector<int> leastDivisiblePrimePosition(n+1);

    
    primes.push_back(2);
    leastDivisiblePrimePosition[0] = -1;
    leastDivisiblePrimePosition[1] = -1;
    int primeCount = 0;

    for(i=3;i<=(n+1);i=i+2) {
        
        leastDivisiblePrimePosition[i-1] = 0;
        int flag = 1;

        for(j=0;j<primes.size();j++) {
            if((i%primes[j] == 0) || (primes[j] > (ceil(sqrt(i))))) {
                
                if(i%primes[j] == 0) {
                    leastDivisiblePrimePosition[i] = min(j,q);
                    flag = 0;
                }
                break;
            }
        }
        if(flag) {
            primeCount++;
            leastDivisiblePrimePosition[i] = min(primeCount,q);
            primes.push_back(i);
        }
    } 

    return(leastDivisiblePrimePosition);

}
/*
 * Complete the waiter function below.
 */
vector<int> waiter(vector<int> number, int q) {
    
    int i,j;
    int n = number.size();
    vector<int> leastDivisiblePrimePosition = makePrimes(10000,q);
    vector<pair<int,int>> bStack;
    vector<int> b;
    vector<int> count(q+1,0);
    
    for(i=0;i<n;i++) {
        bStack.push_back(make_pair(leastDivisiblePrimePosition[number[i]],i));
    }
    
    sort(bStack.begin(),bStack.end());

    // for (i=0;i<n;i++) {
    //     cout << bStack[i].first << ": " << number[bStack[i].second] << endl;
    // }
    

    for(i=0;i<n;i++) {
        count[bStack[i].first]++;
    }

    for(i=1;i<=q;i++) {
        count[i] += count[i-1];
    }

    int start;
    int end;

    for(i=0;i<=q;i++) {

        if(i%2 == 0 || ((i == q) && (q%2 == 1)) ) {
            if(i == 0) {
                start = 0;
                end = count[i];
            }
            else {
                start = count[i-1];
                end = count[i];
            }
            for(j=start;j<end;j++) {
                b.push_back(number[bStack[j].second]);
            }
        }
        else {
            start = count[i] - 1;
            end = count[i-1];
            for(j=start;j>=end;j--) {
                b.push_back(number[bStack[j].second]);
            }
        }
    }

    // for(i=0;i<n;i++) {
    //     cout << b[i] << " ";
    // }


    return(b);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nq_temp;
    getline(cin, nq_temp);

    vector<string> nq = split_string(nq_temp);

    int n = stoi(nq[0]);

    int q = stoi(nq[1]);

    string number_temp_temp;
    getline(cin, number_temp_temp);

    vector<string> number_temp = split_string(number_temp_temp);

    vector<int> number(n);

    for (int number_itr = 0; number_itr < n; number_itr++) {
        int number_item = stoi(number_temp[number_itr]);

        number[number_itr] = number_item;
    }

    vector<int> result = waiter(number, q);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
