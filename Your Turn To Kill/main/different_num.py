import matplotlib.pyplot as plt

PEOPLE_NUM = 20

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
    successfulPossibilities = [0 for _ in range(PEOPLE_NUM + 1)]
    for i in range(1, PEOPLE_NUM + 1):
        successfulPossibilities[i] = successfulWays[i] / factorials[i]
    ### => 36.8% successful possibility

    percentPossibilites = [successfulPossibility * 100 for successfulPossibility in successfulPossibilities]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.plot(list(range(1, PEOPLE_NUM + 1)), percentPossibilites[1:], color="r")
    plt.xlabel("Total Number")
    plt.ylabel("Successful Possibility (%)")
    plt.grid()
    plt.title("Successful Possibilities for different Numbers")
    plt.savefig("images/successfulPossibilities.jpg", bbox_inches="tight", transparent=True)

if __name__ == "__main__":
    main()