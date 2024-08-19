Hitchhiking through the galaxy, you come across a series of strange planetary systems -- where planets seem to be laid out in triangles. Only a few of these, however, can emit a certain type of radiation that you have been searching for, and the others cannot. Only the systems where the area bounded by the triangles is 42 square units can emit the required radiation. Given a set of $n$ coordinates for planets, can you find how many systems exist that emit the radiation you are looking for? Assume that systems can overlap.

For example, given the coordinates $(0,0)$, $(0,28)$, $(3,9)$, and $(5,2)$, here are all the triangles and areas that can be formed:

- $(0,0)$, $(0,28)$, $(3,9)$, with an area of 42.
- $(0,0)$, $(0,28)$, $(5,2)$, with an area of 70.
- $(0,0)$, $(5,2)$, $(3,9)$, with an area of 19.5.
- $(5,2)$, $(0,28)$, $(3,9)$, with an area of 8.5.

Only one system has an area of 42.


Hint 1: the number of triangles that can be formed by $n$ coordinates is equal to the number of **combinations** of points that can be chosen at random.<br>
Hint 2: the area of a triangle represented by $A(x_1, y_1), B(x_2, y_2), B(x_3, y_3)$ is $\frac{1}{2}(x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2))$.

### Input Format
- The first line of the input contains an integer $n$, denoting the number of coordinates.
- The next $n$ lines of the input each contain the space-separated coordinates of a planet.

### Output Format
The first and only line of your output must contain a single integer $m$, denoting the number of systems that produce the radiation you are looking for.

### Constraints
$ 10^2 \le n \le 10^3 $