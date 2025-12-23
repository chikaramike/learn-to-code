responseTimes = [100, 200, 150, 300]
# print(type(responseTimes[0]))
# print(responseTimes[0])
# total = 0
# avg = 0
# count = 0
# for index, num in enumerate(responseTimes):
#     print(index, num)
#     total += num
#     avg = total / (index + 1)
#     if num > avg:
#         count += 1
#     print(avg,)

total = 0
count = 0

for i, num in enumerate(responseTimes, start=1):
    total += num
    avg = total / i
    if num > avg:
        count += 1
    print(avg, count)