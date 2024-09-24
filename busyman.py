# FIFIFI LU:1084/22
# usé el siguiente recurso https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list

def efficiency(activities):
    actsorted = sorted(activities,key=lambda tup: tup[1])
    min = actsorted[0][1]
    ans = 1
    for i in range(1,len(actsorted)):
        if actsorted[i][0] >= min:
            min = actsorted[i][1]
            ans = ans + 1
    return ans

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        acts = []
        for j in range(n):
            (s,e) = map(int, input().split())
            acts.append((s,e))
        print(efficiency(acts))

if __name__ == "__main__":
    main()