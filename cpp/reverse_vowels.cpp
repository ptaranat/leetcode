#include <bits/stdc++.h>
using namespace std;

string reverseVowels(string s) {
  int i, j;
  int len = s.length();
  string vowels = "aeiouAEIOU";
  for (i = 0, j = len - 1; i < j; i++, j--) {
    i = s.find_first_of(vowels, i);
    j = s.find_last_of(vowels, j);
    if (i < j) {
      swap(s[i], s[j]);
    }
  }
  return s;
}