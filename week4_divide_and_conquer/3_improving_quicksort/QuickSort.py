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

def sol(arr):
  sort = sorted(arr)
  return sort
          
def main():
  global n, arr
  n = inp()
  arr = mulinp()
  print(*sol(arr))

if __name__ == '__main__':
    main()