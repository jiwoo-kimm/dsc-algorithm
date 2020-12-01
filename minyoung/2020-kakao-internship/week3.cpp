#include <string>
#include <vector>

using namespace std;

# define MAX 200000;

bool visit[MAX];
int before[MAX]; 
int hang[MAX];
vector<int> edge[MAX];

void check(int node) {
	if (visit[node]) 
		return;

	if (!visit[before[node]]) {
		hang[before[node]] = node;
		return;
	}

	visit[node] = true;
	check(hang[node]);

	for (int n : edge[node]) 
		check(n);
}

bool solution(int n, vector<vector<int>> path, vector<vector<int>> order) {
	for (auto &it : path) {
		edge[it[0]].push_back(it[1]);
		edge[it[1]].push_back(it[0]);
	}

	for (auto &it : order) 
		before[it[1]] = it[0]; 

	if (before[0]) 
		return false;

	visit[0] = true;
	for (int n : edge[0]) 
		check(n);

	for (int i = 0; i < n; i++) 
		if (!visit[i]) 
			return false;

	return true;
}