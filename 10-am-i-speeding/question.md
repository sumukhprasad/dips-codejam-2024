Here is a simple road:

**4=====**

 The 4 means that I cross 4 unit distances per second. The road has 5 '=', so this means that time I need to cross the road is $\frac{5}{4} = 1.25s$.
 
 Here is a more complex road:

**3====7==========4==**

I cross 4 unit distances at 3u/s, 10 unit distances at 7u/s and 2 unit distances at 4u/s. So the time I take to cross the road is $\frac{4}{3}+\frac{7}{10}+\frac{2}{4} = 1.33+0.7+0.5 = 2.53s$. If the numbers represented the speed limits, the minimum time required to cross the road is 2.35s. 

Given a road like the ones above and the time I took to cross the road, can you tell me if I was speeding?

### Input Format
- The first line of the input contains an integer $n$, denoting the number of test cases.
- Each test case comprises of two lines -- the first line contains a decimal $m$, denoting the time I take to cross the road, and the second line contains the road itself.

### Output Format
The first and only line of your output must contain a single integer $s$, denoting the number of times I was speeding.

### Constraints
- $ 10^2 \le n \le 10^3 $
- Assume single-digit speeds.