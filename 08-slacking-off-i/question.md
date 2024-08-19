As most developers know, the number 1 excuse for slacking off is that your code is [compiling](https://xkcd.com/303/). Bobby has a lot of programs to compile, but doesn't want to give his boss any chance to say he's not working. So he lays out all the programs he needs to compile an a table, with 2 numbers for each program - when he will receive the program and can start compiling, and approximately when the program will finish compiling. 

Can you help him decide what is the most number of programs he can compile?

### Input Format
- The first line of the input contains an integer $n$, denoting the number of programs.
- The next $n$ lines of the input each contain when he will receive the program and can start compiling, and approximately when the program will finish compiling, in the form of 2 space-separated integers.

### Output Format
The first and only line of your output must contain a single integer $m$, denoting the maximum number of programs Bobby can compile.

### Constraints
- $ 0 \le n \le 10^6 $
- Assume that the compilations are already sorted based on end times.
- Bobby has $10^4$ hours to finish his job.