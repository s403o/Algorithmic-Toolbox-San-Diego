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
import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def inp():
    return(int(input()))
def mulinp():
  return([int(x) for x in input().strip().split()])
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#--------------------------------------------------------------------------#

def sol(right, key):
  left = 0
  while left <= right:
    mid = left + (right - left) // 2
    if l1[mid] == key:
      return mid
    elif l1[mid] < key:
      left = mid + 1
    else:
        right = mid - 1
  return -1
          
def main():
  n = inp()
  global l1 
  l1 = mulinp()
  n2 = inp()
  l2 = mulinp()
  
  result = []
  for i in l2:
    result.append(sol(len(l1) - 1, i))
  print(*result)

if __name__ == '__main__':
    main()