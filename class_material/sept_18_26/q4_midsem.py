def locate_footprint(s):
  ans = []
  for i in range(len(s)):
    if s[i]=='F' and s[i-1]!="F":
      a = i
    if s[i]=='F' and s[i+1]!='F':
      b = i+1
      ans.append((a,b))
  return ans 
s = "..F.a.faFFF..."
print(locate_footprint(s))
# for i in range(len(s)):
#   print(i,s[i])