#include <bits/stdc++.h>
using namespace std;

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
  set<int> A, B, intersect;
  for (int x : nums1) {
    A.insert(x);
  }
  for (int x : nums2) {
    B.insert(x);
  }
  set_intersection(A.begin(), A.end(), B.begin(), B.end(),
                   inserter(intersect, intersect.begin()));

  return vector<int>(intersect.begin(), intersect.end());
}