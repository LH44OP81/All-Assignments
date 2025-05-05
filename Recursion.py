#def Fibonacci(n):
#
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#        return Fibonacci(n-1) + Fibonacci(n-2)
#for n in range(1, 500):
#    print(n, ":", Fibonacci(n))


#holds key-value pairs
#  cache = {}
#
#  value = 0
#
#  def Fibonacci2(n):
#
#      if n in cache:
#          return cache[n]
#
#      if n == 1 or n == 2:
#          value = 1
#      elif n == 2:
#          value = 1
#      elif n> 2:
#          value = Fibonacci2(n-1) + Fibonacci2(n-2)
#
#      cache[n] = value
#      return value
#
# for i in range(1, 500):
#     print(f"{i} Term: {Fibonacci2(i)}")

# from functools import lru_cache
#
# #L->Last ,R->Recently, C-> Cache
#
# @lru_cache(maxsize=1000)
# def Fibonacci3(n):
#
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return Fibonacci3(n-1) + Fibonacci3(n-2)
#
# for i in range(1, 10000):
#     print(i, ":", Fibonacci3(i))

def TowerofHanoi(n, source, destination_rod, auxilliary_rod):

    if n == 1:
        print("Move disk 1 from source ", source,"to destination", destination_rod)
        return
    TowerofHanoi(n-1, source, auxilliary_rod, destination_rod)
    print("Move disk ", n, "from source", "to destination ", destination_rod)
    TowerofHanoi(n-1,source, auxilliary_rod, destination_rod)

n = 15
TowerofHanoi(n,"A", "B", "C")
