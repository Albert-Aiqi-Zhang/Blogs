### This program is used to calculate the failure possibility of 交換殺人ゲーム in　あなたの番です。
### Here failure means at least one person draw the sheet which he/she themself writes on.

### ==== Method 1. probabilistic approach ======
import random

PEOPLE_NUM = 13
GAME_NUM = 500000

def hasSamePerson(peopleNum):
    array = [i for i in range(peopleNum)]
    shuffledArray = random.sample(array, peopleNum)
    for initialPerson, shufflePerson in zip(array, shuffledArray):
        if initialPerson == shufflePerson:
            return True
    return False

def main():
    success_num = 0
    for _ in range(GAME_NUM):
        if hasSamePerson(PEOPLE_NUM):
            success_num += 1 # actually this is failure number
    successful_possiblity = 1 - success_num / GAME_NUM
    print(successful_possiblity)
    return successful_possiblity

if __name__ == "__main__":
    main()