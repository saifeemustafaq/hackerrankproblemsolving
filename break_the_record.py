def score(arra):
    first_ele = arr[0]
    win_count = 0
    loss_count = 0

    for x in arr:
        if first_ele < x:
            win_count += 1
            first_ele = x
    
    first_ele = arr[0]
    for x in arr:
        if first_ele > x:
            loss_count += 1
            first_ele = x
    
    return [win_count, loss_count]


if __name__ == "__main__":
    size = int(input())
    arr = [int(x) for x in input().split()]

    print(*score(arr), sep = ' ')
