# LeetCode
My code on LeetCode 

***

### No.4 problem: Median of Two Sorted Arrays
[Link](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

还未解决。

***

### No.6 problem: ZigZag Conversion
[Link](https://leetcode.com/problems/zigzag-conversion/description/)

找规律的题目，O(n)就能解决。

***

### No.11 problem: Container With Most Water
[Link](https://leetcode.com/problems/container-with-most-water/description/)

最简单的就是O(n<sup>2</sup>)的算法，但是TLE，需要找更快的算法。<br>
因为面积大小跟两点高度和距离有关，而高度又是取两点中较低的那个，所以可以用贪心的方法做。<br>
选取最远的两个点，做两个指针，向中间移动，如果移动较高的点，面积不可能比当前还大，所以每次只要移动较低的那个点就行了，算法复杂度O(n)。

***

### No. 15 problem: 3Sum
[Link](https://leetcode.com/problems/3sum/description/)

找到列表中所有三个相加和为0的子集。
首先想到的方法是遍历两个数，然后直接找列表中是否有毎两个数相加后与0的差的那个值，若有就说明找到一个子集。理论上是复杂度是O(n<sup>2</sup>)，但是写出来一个68ms就能跑出来的答案还是TLE了。
最后看Discuss，题解是排序后固定第一个数，然后找到另外两个数，十分巧妙，但也是O(n<sup>2</sup>)的复杂度。不过精确算起来是比我的方法复杂度要低的。

***

### No. 16 problem: 3Sum Closest
[Link](https://leetcode.com/problems/3sum-closest/description/)

和上一题的思路一样

***

### No. 19 problem: Remove Nth Node From End of List
[Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

简单的链表问题

***

### No. 23 problem: Merge k Sorted Lists
[Link](https://leetcode.com/problems/merge-k-sorted-lists/description/)

用最小堆做一个排序，代码里自己实现了最小堆。<br>
实际上python的queue库里也有priority queue函数可以直接用。

***

### No. 24 problem: Swap Nodes in Pairs
[Link](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

简单的链表处理

***

### No. 25 problem: Reverse Nodes in k-Group
[Link](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)

比上一题复杂一些的链表，思路就是遍历k的转换范围内的链表，每一个结点依次移到这段链表的头部就行了。

***

### No. 30 problem: Substring with Concatenation of All Words
[Link](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)

用最普通的字符串遍历方式，复杂度是0(words*s)，TLE了，需要更快的算法。

***

### No. 31 problem: Next Permutation
[Link](https://leetcode.com/problems/next-permutation/description/)

找到下一个排列的规律就可以了，注意考虑重复数字的情况。

***

### No. 32 Longest Valid Parentheses
[Link](https://leetcode.com/problems/longest-valid-parentheses/description/)

处理括号对齐的问题，一看就是用栈操作，但是开始没有找到好的统计匹配子串的方法。
看了题解，其实方法很简单，栈内保存括号的index就行了，遍历一遍之后栈内剩下的index之间差值就是匹配子串长度。

***

### No. 665 problem: Non-decreasing Array
[Link](https://leetcode.com/problems/non-decreasing-array/description/)

分两次遍历。先遍历一次，找到下降的部分，把这部分去掉再遍历一次。