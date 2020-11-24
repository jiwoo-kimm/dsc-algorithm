#include <string>
#include <vector>
#include <cmath>

using namespace std;

// �ε��� ã�Ƴ��� �Լ�
vector<int> get_index(int num) {
	vector<int> idx;
	if (num == 0)
		idx = { 3,1 };
	else
		idx = { (num - 1) / 3,(num + 2) % 3 };
	return idx;
}

// �Ÿ� ������ ã�Ƴ��� �Լ�
string get_Sdist(vector<int> left, vector<int> mid, vector<int> right, string hand) {
	int left_dist = abs(left[0] - mid[0]) + abs(left[1] - mid[1]);
	int right_dist = abs(right[0] - mid[0]) + abs(right[1] - mid[1]);

	if (left_dist < right_dist)
		return "left";
	else if (left_dist > right_dist)
		return "right";
	else
		return hand;
}

string solution(vector<int> numbers, string hand) {
	string answer = "";

	vector<int> left_curr = { 3,0 };
	vector<int> right_curr = { 3,2 };

	for (int i = 0; i < numbers.size(); i++) {
		vector<int> idx = get_index(numbers[i]);

		//�����е�
		if (idx[1] == 0) {
			left_curr = idx;
			answer += "L";
		}
		//�������е�
		else if (idx[1] == 2) {
			right_curr = idx;
			answer += "R";
		}
		// �߰��� �ִ� ���
		else {
			//�ּҰŸ� ã��
			string where = get_Sdist(left_curr, idx, right_curr, hand);

			if (where == "left") {
				answer += "L";
				left_curr = idx;
			}
			else if (where == "right") {
				answer += "R";
				right_curr = idx;
			}
		}
	}
	return answer;
}

