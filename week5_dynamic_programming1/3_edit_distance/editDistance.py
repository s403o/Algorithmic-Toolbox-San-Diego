######################################################
#                ▄▄▄     ▄▄▄▄     ▄▄▄▄▄              #
#               ▄███    ██▀▀██   █▀▀▀▀██▄            #
#  ▄▄█████▄    █▀ ██   ██    ██       ▄██   ▄████▄   #
#  ██▄▄▄▄ ▀  ▄█▀  ██   ██ ██ ██    █████   ██▀  ▀██  #
#   ▀▀▀▀██▄  ████████  ██    ██       ▀██  ██    ██  #
#  █▄▄▄▄▄██       ██    ██▄▄██   █▄▄▄▄██▀  ▀██▄▄██▀  #
#   ▀▀▀▀▀▀        ▀▀     ▀▀▀▀     ▀▀▀▀▀      ▀▀▀▀    #
#                                                    #
######################################################
import sys, math

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def inp():
    return((input()))
def mulinp():
  return([int(x) for x in input().strip().split()])
def inlt():
    return(list(map(int,input().split())))
def insertionr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#--------------------------------------------------------------------------#

def sol(firstString,SecondString):
  n, m = len(firstString) + 1, len(SecondString) + 1
  distance = [[0 for i in range(m)] for j in range(n)]
  for i in range(n):
    distance[i][0] = i
  for i in range(m):
    distance[0][i] = i
  
  for j in range(1, m):
    for i in range(1, n):
      match, dismatch = distance[i-1][j-1], distance[i-1][j-1] + 1
      insertion, deletions = distance[i][j-1] + 1, distance[i-1][j] + 1
      if firstString[i-1] == SecondString[j-1]:
        distance[i][j] = min(match, insertion, deletions)
      else:
        distance[i][j] = min(dismatch, insertion, deletions)
  
  return distance[n-1][m-1]

def main():
  s1, s2 = inp(), inp()
  print(sol(s1, s2))

if __name__ == '__main__':
    main()