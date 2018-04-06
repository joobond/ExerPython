s = int(input())

h = s/3600
s_rest = s%3600
m = s_rest/60
s_rest = s_rest%60

print(("%d:%d:%d")%(h,m,s_rest))