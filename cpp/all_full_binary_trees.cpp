// Practice, try with DP
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

vector<TreeNode *> allPossibleFBT(int n) {
  vector<TreeNode *> out;
  // Base case: Cannot have full binary tree with even number of nodes
  if (n < 1 || n % 2 == 0) {
    return out;
  }

  for (int k = 2; k < n; k += 2) {
    // Find all possible left and right subtree roots
    vector<TreeNode *> v1 = allPossibleFBT(k - 1);
    vector<TreeNode *> v2 = allPossibleFBT(n - k);

    int n1 = v1.size(), n2 = v2.size();

    for (int i = 0; i < n1; i++) {
      for (int j = 0; j < n2; j++) {
        TreeNode *newRoot = new TreeNode(0);
        newRoot->left = v1[i];
        newRoot->right = v2[j];
        out.push_back(newRoot);
      }
    }
  }
  // If n == 1
  if (out.empty()) {
    out.push_back(new TreeNode(0));
  }
  return out;
}