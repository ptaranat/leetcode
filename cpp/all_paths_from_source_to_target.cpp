#include <bits/stdc++.h>

using namespace std;

bool visited(int x, vector<int>& path) {
  int size = path.size();
  for (int i = 0; i < size; i++) {
    if (path[i] == x) {
      return true;
    }
  }
  return false;
}

vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
  queue<vector<int>> q;
  vector<int> path;
  vector<vector<int>> allpaths;
  path.push_back(0);
  q.push(path);
  while (!q.empty()) {
    path = q.front();
    q.pop();
    int last = path[path.size() - 1];
    if (last == graph.size() - 1) allpaths.push_back(path);
    for (int i = 0; i < graph[last].size(); ++i) {
      if (!visited(graph[last][i], path)) {
        vector<int> newpath(path);
        newpath.push_back(graph[last][i]);
        q.push(newpath);
      }
    }
  }
  return allpaths;
}
