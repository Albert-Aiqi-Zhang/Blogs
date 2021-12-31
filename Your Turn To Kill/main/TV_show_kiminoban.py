### This program is used to calculate the failure possibility of 交換殺人ゲーム in　あなたの番です。
### Here failure means at least one person draw the sheet which he/she themself writes on.

### ==== Method 1. probabilistic approach ======
# import random

# PEOPLE_NUM = 13
# GAME_NUM = 500000

# def hasSamePerson(peopleNum):
#     array = [i for i in range(peopleNum)]
#     shuffledArray = random.sample(array, peopleNum)
#     for initialPerson, shufflePerson in zip(array, shuffledArray):
#         if initialPerson == shufflePerson:
#             return True
#     return False

# def main():
#     success_num = 0
#     for _ in range(GAME_NUM):
#         if hasSamePerson(PEOPLE_NUM):
#             success_num += 1 # actually this is failure number
#     successful_possiblity = 1 - success_num / GAME_NUM
#     print(successful_possiblity)
#     return successful_possiblity

# if __name__ == "__main__":
#     main()



### ==== Method 2. deterministic approach with dynamic programming ======
### let f(n) be the successful ways (no one draws their own sheets) when the total
### people is n. In this way, we can calculate f(n) and the successful possibility of P(n)
### satisfies the recurrence relation:
### f(n) = n! - 1 - C(n, n - 1) * f(n - 1) - C(n, n - 2) * f(n - 2) - ... - C(n, 2) * f(2).
###     f(1) = 0, f(2) = 1
### P(n) = (n! - 1 - C(n, n - 1) * f(n - 1) - C(n, n - 2) * f(n - 2) - ... - C(n, 2) * f(2)) / n!
###      = f(n) / n!
### Mention that we cannot make just (n - 1) people get their own sheets when the total number is n.

PEOPLE_NUM = 13

def getFactorials(total_num):
    factorials = [1 for _ in range(total_num + 1)] # 0! = 1! = 1
    for i in range(2, total_num + 1):
        factorials[i] = factorials[i - 1] * i
    return factorials

def getCombinatorialNumber(n, k, factorials):
    return factorials[n] // (factorials[n - k] * factorials[k])

def getSuccessfulWays(total_num, factorials):
    successfulWays = [0 for _ in range(total_num + 1)] # We use 1-indexed to make it more readable
    successfulWays[2] = 1 # i.e., 1, 2 => 2, 1
    for num in range(3, total_num + 1):
        count = 0
        for idx in range(2, num):
            count += getCombinatorialNumber(num, idx, factorials) * successfulWays[idx]
        count += 1
        successfulWays[num] = factorials[num] - count
    return successfulWays


def main():
    factorials = getFactorials(PEOPLE_NUM)
    successfulWays = getSuccessfulWays(PEOPLE_NUM, factorials)
    successfulPossibility = successfulWays[PEOPLE_NUM] / factorials[PEOPLE_NUM]
    print(successfulPossibility)
    ### => 36.8% successful possibility

if __name__ == "__main__":
    main()



