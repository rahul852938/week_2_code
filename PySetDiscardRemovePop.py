a = int(input())
nums = set(map(int, input().split()))
c = int(input())

for _ in range(c):
    cmd = input().split()
    op = cmd[0]

    if op == "pop":
        if nums:
            nums.remove(min(nums))
    elif op == "remove":
        x = int(cmd[1])
        if x in nums:
            nums.remove(x)
    elif op == "discard":
        x = int(cmd[1])
        nums.discard(x)

print(sum(nums))
