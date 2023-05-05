class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        d1 = sum(distance[start: destination])
        d2 = sum(distance[:start]) + sum(distance[destination:])

        return min(d1, d2)

a=Solution()
listA = []

n = int(input("Enter number of elements in the list : "))

listA = list(map(int,input("Enter the numbers comma seperated : ").strip().split(',')))[:n]
start=int(input("Enter start: "))
dest=int(input("Enter the destination: "))
print(a.distanceBetweenBusStops(listA,start,dest))
