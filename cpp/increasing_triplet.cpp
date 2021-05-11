#include <bits/stdc++.h>
using namespace std;

bool increasingTriplet(vector<int>& nums) {
  int i = INT_MAX, j = INT_MAX;
  for (int x : nums) {
    if (x <= i)
      i = x;  // x could be i
    else if (x <= j)
      j = x;  // x is greater than i and might be j
    else
      return true;  // x is greater than i and j, and i < j
  }
  return false;
}