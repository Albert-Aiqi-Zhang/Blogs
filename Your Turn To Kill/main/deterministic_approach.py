
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