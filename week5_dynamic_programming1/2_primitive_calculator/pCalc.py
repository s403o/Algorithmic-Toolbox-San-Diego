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
import sys, math, copy

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def inp():
    return(int(input()))
def mulinp():
  return([int(x) for x in input().strip().split()])
def inlt():
    return(list(map(int,input().split())))
def insertionr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#--------------------------------------------------------------------------#

def sol(n):
  assert(1 <= n <= 10 ** 6)
  values = [[]]

  for val in range(1, n + 1):
    add1 = len(values[val - 1]) + 1

    mult2 = math.inf
    if val % 2 == 0:
      mult2 = len(values[val // 2]) + 1

    mult3 = math.inf
    if val % 3 == 0:
      mult3 = len(values[val // 3]) + 1

    operations = min(add1, mult2, mult3)

    idx = val - 1
    if operations == mult2:
        idx = val // 2
    elif operations == mult3:
        idx = val // 3

    new_list = copy.deepcopy(values[idx]) # create a new object and recursively adds the copies of the original elements.
    new_list.append(val)
    values.append(new_list)

  return values[n]
  

def main():
  n = inp()
  output = sol(n)
  print(len(output) - 1)
  print(*output)


if __name__ == '__main__':
    main()