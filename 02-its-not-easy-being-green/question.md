'It's not easy being green,' was the frequent refrain of Kermit the frog. 

'It seems you blend in<br>With so many other ordinary things,'

he says. Let's find him some friends, shall we? Each input is a string of length $n$ made up of numbers and uppercase letters. Your task is to find the number of 6-character substrings which, when read as a hex colour code, are shades of green. Substrings may overlap with each other.

To determine whether a substring is a shade of green or not, check for the following conditions to be true:

- the amount of blue in the colour is less than 80\% of the amount of green
- the amount of red in the colour is less than 64\% of the amount of green

Given a string of length $n$, how many substrings can you find that satisfy the conditions?

### Input Format
The first line of the input contains a string of length $n$ containing numbers and uppercase letters.

### Output Format
The first and only line of your output must contain a single integer $m$, denoting the the number of substrings that satisfy the conditions.

### Constraints
$ 10^4 \le n \le 10^6 $