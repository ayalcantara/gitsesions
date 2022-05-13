rest =[]
scoreList = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rest += [[name,score]]
        scoreList += [score]
    pivot = sorted(list(set(scoreList)))[1] 
    for listName,key in sorted(rest):
        if key == pivot:
            print(listName)