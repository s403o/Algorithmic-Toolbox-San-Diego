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

def sol(money):
  coins = [1, 3, 4]
  minCoins = [0] + [math.inf] * money

  for i in range(1, money + 1):
    for coin in coins:
      if i >= coin:
        nCoins = minCoins[i - coin] + 1
        if nCoins < minCoins[i]:
          minCoins[i] = nCoins
  
  return minCoins[money]
          
def main():
  n = inp()
  print(sol(n))

if __name__ == '__main__':
    main()