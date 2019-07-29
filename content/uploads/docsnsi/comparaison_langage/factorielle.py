def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        i = 0
        while i < n:
            i = i + 1
            result = result * i
        return result

factorielle(5)

if __name__ == '__main__':
   import sys
   n = int(sys.argv[1])
   print( str(factorielle(n)) )