
def main():
  s = "/bin/cat flag"
  ans = "\""
  for i in s:
    ans += "\\" + str( oct( ord(i) ) )
  ans += "\""
  print(ans.replace("0o", ""))
if __name__ == '__main__':
  main()
