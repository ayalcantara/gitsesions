if __name__ == "__main__":
    n = int(input())
    output = [] 

    for x in range(0, n):
        listCheck= input().split()
        if listCheck[0] == "print":
            print(output)
        elif listCheck[0] == "insert":
            output.insert(int(listCheck[1]), int(listCheck[2]))
        elif listCheck[0] == "remove":
            output.remove(int(listCheck[1]))
        elif listCheck[0] == "pop":
            output.pop()
        elif listCheck[0] == "append":
            output.append(int(listCheck[1]))
        elif listCheck[0] == "sort":
            output.sort()
        else:
            output.reverse()