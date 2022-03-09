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
  return([int(x) for x in input().split()])
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#--------------------------------------------------------------------------#

def gcd(a, b):
  if a == 0:
    return b
  else:
    return gcd(b % a, a)
    
def main():
  a, b = mulinp()
  print(gcd(a, b))

if __name__ == '__main__':
    main()