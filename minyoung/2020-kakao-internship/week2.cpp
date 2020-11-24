#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long calculate(long long a, long long b, char op) {
	if (op == '+')
		return a + b;
	else if (op == '-')
		return a - b;
	else
		return a * b;
}


long long solution(string expression) {
	long long answer = 0;

	string curr = "";
	vector<long long> num;
	vector<char> op;
	vector<char> idx;
	
	for (int i = 0; i < expression.size(); i++){
		if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*'){
			num.push_back(stoi(curr));
			curr = "";
			if (find(op.begin(), op.end(), expression[i]) == op.end())
				op.push_back(expression[i]);
			idx.push_back(expression[i]);
		}
		else
			curr += expression[i];
	}

	num.push_back(stoi(curr));
	sort(op.begin(), op.end());

	do{
		vector<long long> tmp_num = num;
		vector<char> tmp_loc = idx;

		for (int i = 0; i < op.size(); i++){
			for (int j = 0; j < tmp_loc.size(); j++){
				if (op[i] == tmp_loc[j]){
					tmp_num[j] = calculate(tmp_num[j], tmp_num[j + 1], op[i]);
					tmp_num.erase(tmp_num.begin() + j + 1);
					tmp_loc.erase(tmp_loc.begin() + j);
					j--;
				}
			}
		}

		if (answer < abs(tmp_num[0]))
			answer = abs(tmp_num[0]);
	} while (next_permutation(op.begin(), op.end()));

	return answer;
}