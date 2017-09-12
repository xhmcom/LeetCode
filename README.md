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

### No. 15 problem: 3Sum
[Link](https://leetcode.com/problems/3sum/description/)

找到列表中所有三个相加和为0的子集。
首先想到的方法是遍历两个数，然后直接找列表中是否有毎两个数相加后与0的差的那个值，若有就说明找到一个子集。理论上是复杂度是O(n<sup>2</sup>)，但是写出来一个68ms就能跑出来的答案还是TLE了。
最后看Discuss，题解是排序后固定第一个数，然后找到另外两个数，十分巧妙，但也是O(n<sup>2</sup>)的复杂度。不过精确算起来是比我的方法复杂度要低的。

* * *

### No. 665 problem: Non-decreasing Array
[Link](https://leetcode.com/problems/non-decreasing-array/description/)

分两次遍历。先遍历一次，找到下降的部分，把这部分去掉再遍历一次。