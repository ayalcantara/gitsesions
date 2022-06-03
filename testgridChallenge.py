def gridChallenge(grid):
    # Write your code here
    res = [sorted(g) for g in grid]
    res_t = [list(x) for x in zip(*res)]
    test_res_t = [sorted(t) for t in res_t]
    return 'YES' if res == sorted(res) and res_t == test_res_t else 'NO'

if __name__ == '__main__':
    n = int(input().strip())
    gridChallenge(n)