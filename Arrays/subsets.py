def subsets(arr):
    res = []
    def backtrack(i, curr):
        if i == len(arr):
            res.append(tuple(curr))
            return
        # exclude current
        backtrack(i + 1, curr)
        # include current
        curr.append(arr[i])
        backtrack(i + 1, curr)
        curr.pop()
    backtrack(0, [])
    return res

if __name__ == '__main__':
    arr = [1, 2, 3]
    print('Subsets of', tuple(arr))
    for s in subsets(arr):
        print(s)
