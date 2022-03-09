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
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#--------------------------------------------------------------------------#
def fibonacci(n): # O(2^n)
    if n == 2:
      return 1
    elif n == 1:
      return 0
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)

def FibonacciFast(n): # O(N)
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]



def main():
    # print(fibonacci(inp()))
    print(FibonacciFast(inp()))
    

if __name__ == '__main__':
    main()