# LeetCode
My code on LeetCode 

* * *

### No.4 problem: Median of Two Sorted Arrays
[Link](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

还未解决。

* * *

### No.6 problem: ZigZag Conversion
[Link](https://leetcode.com/problems/zigzag-conversion/description/)

找规律的题目，O(n)就能解决。

* * *

### No.11 problem: Container With Most Water
[Link](https://leetcode.com/problems/container-with-most-water/description/)

最简单的就是O(n<sup>2</sup>)的算法，但是TLE，需要找更快的算法。<br>
因为面积大小跟两点高度和距离有关，而高度又是取两点中较低的那个，所以可以用贪心的方法做。<br>
选取最远的两个点，做两个指针，向中间移动，如果移动较高的点，面积不可能比当前还大，所以每次只要移动较低的那个点就行了，算法复杂度O(n)。

* * *

### No. 665 problem: Non-decreasing Array
[Link](https://leetcode.com/problems/non-decreasing-array/description/)

分两次遍历。先遍历一次，找到下降的部分，把这部分去掉再遍历一次。