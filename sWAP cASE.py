"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format:
A single line containing a string S.

Output Format:
Print the modified string S.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""
# swap_case function from skratch
# def swap_case(s):
#     y=""
#     for i in s:
#         if i.isupper():
#             y+=i.lower()
#         else:
#             y+=i.upper()
#     return y
def swap_case(s):
    return s.swapcase()

x=input()
print(swap_case(x))

