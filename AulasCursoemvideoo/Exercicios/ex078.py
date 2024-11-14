nums = []
mai = 0
men = 0
for c in range(0,5):
    nums.append(int(input(f"Digite um valor apra a posição {c}: ")))
    if c == 0:
        mai = men = nums[c]
    else:
        if nums[c] > mai:
            mai = nums[c]
        if nums[c] < men:
            men = nums[c]
print("=-"*30)
print(f"Você digitou os valores {nums}")
print(f"O maior valor digitado foi o: {mai} nas posições:")
for i, v in enumerate(nums):
    if v == mai:
        print(f'{i}...', end="")
print(f"\nO menos valor digitado foi o {men} nas posições")
for i, v in enumerate(nums):
    if v == men:
        print(f'{i}...', end="")