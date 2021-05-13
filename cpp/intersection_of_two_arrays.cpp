#include <bits/stdc++.h>
using namespace std;

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
  set<int> s(nums1.begin(), nums1.end());
  vector<int> out;
  for (int x : nums2) {
    // If we can remove a key from A that appears in B,
    // then x is the common element
    if (s.erase(x)) out.push_back(x);
  }
  return out;
}