You're a researcher deep in the jungles of the Amazon plotting flight paths for a few rare birds. But there's a problem - planes! Planes seem to be interfering with your plotting of flight paths, and you need to filter them out to get your data. Every flight path that you capture, plane or bird, is denoted by a space-separated string of coordinates for each stop the object makes in the format $T(x,y)$, where $T$ denotes the type of stop (short, medium, long) and $x$ and $y$ denote the coordinates of the stop. Birds follow a pattern in their stops, either in terms of cycling between the coordinates or cycling through a pattern of durations of their stops, while planes do not follow any discernible pattern. For example:

$S0,0\ L0,2\ S0,3\ L0,4$ is a bird,<br>
$S0,0\ L0,4\ M0,3\ M0,0\ M0,4\ S0,3$ is a bird,<br>
$S0,0\ L0,1\ S0,3\ M0,0\ L0,4\ S0,2\ M0,5$ is a plane

Can you find how many birds you've captured?

### Input Format
-  The first line of the input contains an integer $n$, denoting the number of flight paths.
-  The next $n$ lines of input each contain a flight path.

### Output Format
The first and only line of your output must contain a single integer $m$, denoting the number of birds.

### Constraints
-  $ 100 \le n \le 1000 $
-  $ x,y \le 10^3 $
-  The number of coordinates in each path is between $100$ and $1000$