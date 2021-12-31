# Your Turn to Kill (あなたの番です)

Recently I have watched a Japanese TV show あなたの番です (Your Turn to Kill). It is characterized by an exchange murder game (交換殺人). 13 residents in 
an apartment complex joined the exchange murder game, writing down the person who he/she wants to kill in a sheet, and draw others' sheet in random.
The resident will murder who he/she draws. A serial murder happens then.  

(insert a picture here)

The TV show is too interesting for me to mention some bugs. In an episode, a resident, Miss Kuroshima (黒島ちゃん) pointed out that this game may be a failure because
someone may draw their own sheet. In other words, it is possible that at least one person cannot actually participate in this game by killing someone else's target.

This is obviously a mathematical problem, so I think I can write a program to calculate the successful possibility, that is, everyone draws others' sheets.

## Method 1. Probabilistic Approach

I learnt about this approach when I tried to calculate Pi. In that problem, we can "throw darts" in a square randomly, and see how many darts are within the circle.

This approach lends itself very well in this problem. We can initialize with an array [0, 1, 2, ..., 12], and shuffle this array (shuffledArray), then compare it with the initial array. Then we can count if there is any duplicate numbers in the same position (initialPerson == shufflePerson). If there is any such case, it means this game cannot continue. Based on the law of large numbers, when we play this games for enormous times, we can get a successful possibility which is very close to the real possibility.

In the program probalisitic_approach.py, I complete a loop of 500,000 turns, and find the successful possibility is only 36.8%. In other words, it is very likely someone will leave the game because he/she draws their own sheet. What a pity! (lucky?)

## Method 2. Deterministic Approach

This first method is somewhat confusing, because we can directly calculate the possiblity with some more "mathematical" methods. Actually, we can start with some small numbers.

### (i) The idea
For example, we can start with only 1 person. He/She writes down who he/she hates, and he/she has to draw their own sheet. That is, one person cannot complete the
"exchange" murder game. (Of course not!)

Then we come up with 2 persons. We can give them IDs, e.g., 1 and 2. So 1 writes down someone 1 hates, and 2 writes down someone 2 hates, then they exchange with each other. For simplicity, here the we name victims with 1 and 2 as well. So here we have 2 different events: 1, 2 and 2, 1. This is a simple permutation problem. So obviously, there is only 1 way for the "exchange", i.e., 2, 1. So the successful possibility is 50%.

We can do the same thing for 3 people (1, 2 and 3). There are 3! = 6 ways in total, but here only two ways can work: (2, 3, 1), (3, 1, 2), so the successful possibility is 1/3, or 33.3%.

It is very tough to calculate the result by hand, but the computer can help us a lot. Actually, we can derive the recurrence relation of the possibility. Here we need two variables: successful ways (f(n)) and successful possibility (P(n)).

### (ii) Recurrence relation for successful ways

In the program deterministic_approach.py, I introduce the successfulWays f(n), where n is the total number. This is a critical intermidiate variable, with which we can easily calculate the successful possibility. For example, in (i) The idea, I have calculated successful ways for n = 1, 2 and 3. That is,  
f(1) = 0,  f(2) = 1,  f(3) = 2.  
For any large number n (n >= 3), we can find the following recurrence relation:    
![\Large C(n,k)=\frac{n!}{k!(n-k)!](https://latex.codecogs.com/svg.latex?\Large;f(n)=n!-C(n,n)-C(n,n-1)*f(n-1)-C(n,n-2)*f(n-2)-...-C(n,2)*f(2)).   
Here C(n, k) is the combinatorial number, which can be calculated by:  
![\Large C(n,k)=\frac{n!}{k!(n-k)!](https://latex.codecogs.com/svg.latex?\Large&space;C(n,k)=\frac{n!}{k!(n-k)!})






![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{b\pm\sqrt{b^2-4ac}}{2a})


