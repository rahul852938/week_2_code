def average(array):
    heigts = set(array)
    average = sum(heigts) / len(heigts)
    return round(average, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
