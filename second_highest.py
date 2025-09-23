def find_second_highest(num):
    if num:
        high=num[0]
        s_high = None
        for n in num:
            if n > high:
                s_high = high
                high = n
            elif n != high:
                if (s_high is None) or ( n > s_high):
                    s_high=n
        print(f"second highest {s_high}")
    else:
        print("empty")

find_second_highest([3,3,3,2,3,1,3])

# Find second lowest

def find_second_lowest(num):
    lowest = num[0]
    s_l = None
    for n in num:
        if n < lowest:
            s_l = lowest
            lowest=n
        elif n != lowest:
            if (s_l is None) or (n < s_l):
                s_l=n
    print("se l ", s_l)


find_second_lowest([5,5,3,4,2,2])



import asyncio

async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)
    print("Task 1 end")

async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
