'''

Source:
https://www.hackerrank.com/challenges/flatland-space-stations/problem

Problem:
Flatland is a country with a number of cities, some of which have space stations.
Cities are numbered consecutively and each has a road of 1km length connecting it to the next city.
It is not a circular route, so the first city doesn't connect with the last city.
Determine the maximum distance from any city to its nearest space station.

'''
def flatlandSpaceStations(n, c):
    res=-1
    cons=0
    for i in range(n):
        if i not in c:
            cons+=1
        else:
            if cons>res:
                res=cons
            cons=0

    res = (res+1)//2        

    if cons>res:
        return cons
    else:
        return res 
    
def flatlandSpaceStationsSort(n, c):
    if c:
        c.sort()
        res=-1        
        for i in range(len(c)):
            #first element
            if i == 0:
                cur=c[i]
            #in-between
            else:
                cur=(c[i]-c[i-1])//2
            if cur > res:
                res = cur       
        cur=n-1-c[-1]
        if cur>res:
            return cur
        else:         
            return res


if __name__=="__main__":
    print(flatlandSpaceStations(5, [0,2]))
    print(flatlandSpaceStationsSort(5, [0,2]))
    print(flatlandSpaceStations(6, [0,1,2,4,3,5]))
    print(flatlandSpaceStationsSort(6, [0,1,2,4,3,5]))
