# Bit manipulations
## Bitshift operator
there are two types in it one being right shift and other one is left 

the right shift syntax is x >> y where the binary representation of x is being right shifted by y bits

for example consider 5 >> 2

the binary representation of 5 would be 00000101 so the right shift would be xx000001 so the xx here would be dependent on what sort of shift we are performing 

two types of right shifts are arithmetic and logical 

the arithmetic shift keep the final bit intact(the final bit is for sign) and the logical shift pads it by 0 no matter what 

# Python syntax for binary manipulations
## Decimal to binary 
bin(int) give the '0bxxx' where the first two char of this string denotes its a binary representation to chop them off we could use bin(int)[2:]
## binary to Decimal 
x = '10011'
int(x,2) where 2 denotes it is in binary representation
## Bitwise AND
now one thing to keep in mind is bitwise operation can be directly performed on the int themselves and also the result is in terms of int
5 & 7 i.e 101 & 111 which gives 101 = 5
## Bitwise OR
5 | 7 i.e 101 | 111 which gives 111 = 7
## Bitwise XOR
5 ^ 7 i.e 101 ^ 111 which gives 010 = 2
## Bitwise NOT
~ 5 i.e ~ 101 = 010 = 2
## Left shift
5 << 2 i.e 101 << 2 100 = 4
## Arthmetic (Signed) Right shift
5 >> 2 101 >> 2 001 which gives 1 

python only supports Arthmetic right shift

# Combinadic Hashmap

## The Combinadic of an Integer

The combinadic of an integer is an alternative representation of the number based on combinations that maps nicely to a combination element. Consider for example the number 27. If we fix n = 7 and k = 4, it turns out that the combinadic of 27 is ( 6 5 2 1 ). This means that:

```
  27 = Choose(6,4) + Choose(5,3) + Choose(2,2) + Choose(1,1).
```

With n = 7 and k = 4, any number z between 0 and 34 (the total number of combination elements for n and k) can be uniquely represented as:

```
  z = Choose(c1,4) + Choose(c2,3) + Choose(c3,2) + Choose(c4,1)
```

This representation is where n &gt; c1 &gt; c2 &gt; c3 &gt; c4. Notice that n is analogous to the base because all combinadic digits are between 0 and n-1 (just like all digits in ordinary base 10 are between 0 and 9). The k value determines the number of terms in the combinadic. The combinadic of a number can be calculated fairly quickly.

Let me show you a second example of the combinadic of a number, but this time I'll show you how to calculate it. Suppose we have the integer 8, with n and k set to 7 and 4 respectively, and we want the combinadic. The combinadic of 8 will have the form:

```
  8 = Choose(c1,4) + Choose(c2,3) + Choose(c3,2) + Choose(c4,1)
```

We first determine the value of c1. We try 6 (the largest number less than n = 7) and get **Choose(6,4)** = 15, which is too much because we're over 8. Next, we try 5 and get **Choose(5,4)** = 5, which is less than 8, so bingo, c1 = 5. Now we have used up 5 of the original number 8 so we have 3 left to account for. To determine the value of c2, we try 4 (the largest number less than the 5 we got for c1), but get **Choose(4,3)** = 4, which is barely too much. Working down we get to 3 and **Choose(3,3)** = 1, so c2 = 3. We used up 1 of the remaining 3 we had to account for, so we have 2 left to consume. Using the same ideas we'll get c3 = 2 with **Choose(2,2)** = 1, so we have 1 left to account for. And then we'll find that c4 = 1 because **Choose(1,1)** = 1. Putting our four c values together we conclude that the combinadic of 8 with n = 7 and k = 4 is ( 5 3 2 1 ).

Well, this is all rather strange and perhaps somewhat interesting but what makes the combinadic useful is that the combinadic of a number indirectly maps to its lexicographic element and gives us a way to quickly compute an arbitrarily specified combination element.

## The Combination.Element() Method

Before I show you how to use the combinadic of a number to determine the mth lexicographical element of a combination, I need to explain the idea of the dual of each lexicographic index. Suppose n = 7 and k = 4. There are **Choose(7,4)** = 35 combination elements, indexed from 0 to 34. The dual indexes are the ones on opposite ends so to speak: indexes 0 and 34 are duals, indexes 1 and 33 are duals, indexes 2 and 32, and so forth. Notice that each pair of dual indexes sum to 34, so if we know any index it is easy to find its dual.

Now, continuing the first example above for the number 27 with n = 7 and k = 4, suppose we are able to find the combinadic of 27 and get ( 6 5 2 1 ). Now suppose we subtract each digit in the combinadic from n-1 = 6 and get ( 0 1 4 5 ). Amazingly, this gives us the combination element [7], the dual index of 27! Putting these idea together we have an elegant algorithm to determine an arbitrarily specified combination element for given n and k values. To find the combination element for index m, first find its dual and call it x. Next, find the combinadic of x. Then subtract each digit of the combinadic of x from n-1 and the result is the mth lexicographic combination element. The table below shows the relationships among m, the dual of m, **Comination.Element(m)**, the combinadic of m, and (n-1) - ci for n=5 and k=3.

```
m  dual(m)  Element(m)  combinadic(m)  (n-1) - ci
=================================================
0    9      { 0 1 2 }   ( 2 1 0 )      ( 2 3 4 )
1    8      { 0 1 3 }   ( 3 1 0 )      ( 1 3 4 )
2    7      { 0 1 4 }   ( 3 2 0 )      ( 1 2 4 )
3    6      { 0 2 3 }   ( 3 2 1 )      ( 1 2 3 )
4    5      { 0 2 4 }   ( 4 1 0 )      ( 0 3 4 )
5    4      { 0 3 4 }   ( 4 2 0 )      ( 0 2 4 )
6    3      { 1 2 3 }   ( 4 2 1 )      ( 0 2 3 )
7    2      { 1 2 4 }   ( 4 3 0 )      ( 0 1 4 )
8    1      { 1 3 4 }   ( 4 3 1 )      ( 0 1 3 )
9    0      { 2 3 4 }   ( 4 3 2 )      ( 0 1 2 )
```



Let's walk through how the **Element()** method calculates and returns the [6] lexicographic combination element for n = 7 and k = 4, which is { 0, 1, 3, 6 }. **Element()** starts by creating an array of size 4 to hold the digits of our answer. Next, we compute the dual index of the input parameter m, making use of the fact that the duals sum to **Choose(n,k)** - 1. Because m is 6, the dual index x is 34 - 6 = 28. Now we will compute the combinadic of 28. Most of the work is done with a strange little helper function, **LargestV()**. We know the basic structure of the combinadic of 28 will be ( c1, c2, c3, c4 ) where:

```
  28 = Choose(c1,4) + Choose(c2,3) + Choose(c3,2) + Choose(c4,1)
```

So, we need to find values c1, c2, c3, and c4. The **LargestV(a,b,x)** function returns the largest value v that is less than a given value a, and so that **Choose(v,b)** is less than or equal to x. Believe me, this made my head spin when I was first working out the details. To compute c1, we call **LargestV(7,4,28)**, the largest value v less than 7, so that **Choose(v,4)** is less than or equal to 28. In this case, **LargestV()** returns 6 because **Choose(6,4)** = 15, which is less than 28. The value 6 is the first number c1, of the combinadic.

Now to compute the c2 value, we subtract 15 from 28 and see that we now only have 13 left to consume because we used up 15 for the c1 coefficient. We call **LargestV(6,3,13)**, which returns 5 and note that **Choose(5,3)** is 10, leaving us with 3. The combinadic is now ( 6 5 ? ? ). Next, we call **LargestV(4,2,10)** and get 3 for c3, noting that **Choose(3,2)** is 3, leaving us with 0 left. Finally, to compute c4, we call **LargestV(3,1,0)**, which returns 0.

Now that we have the combinadic ( 6 5 3 0 ) in our answer array, we map it to a combination element by subtracting each of the combinadic values from n-1 = 6, giving us ( 0 1 3 6 ). Finally, we feed our answer array to our auxiliary constructor to convert it into a combination object and get { 0, 1, 3, 6 }—combination element [6] in lexicographical order for n = 7 and k = 4. Whew!

Notice that the **LargestV(a,b,x)** function calls the **Choose(n,k)** method in such a way that n can be less than k. This is why we allow this possibility in the **Choose()** method, and also in the Combination constructor.

To summarize, an important fundamental operation on combinations is generating the mth lexicographic combination element for given n and k values. A naive approach that iterates from the first element up to the mth element is not always effective because the number of elements can be very large. I discovered that the little-known combinadic of a number could be used to quickly generate the mth combination element.

## Discussion

The idea of the combinadic of a number is closely related to the *factoradic* of a number. In an MSDN article (http://msdn.microsoft.com/library/enus/dnnetsec/html/permutations.asp) on mathematical permutations (all possible orderings of a set of integers from 0 to n-1), I describe how the factoradic of a number is a representation based on factorials. For example, the factoradic of integer value 53 is ( 2 0 1 3 ) because:

```
  53 = (2 * 4!)  +  (0 * 3!)  +  (1 * 2!)  +  (3 * 1!)
```

The factoradic can be used to generate the mth permutation element for a given n in a way that is analogous to the way the combinadic can be used to generate the mth combination element. I have observed a general theme that when you are trying to map from an index value to a vector value, alternate number representations are often the key to an elegant solution.

Although the combinadic can calculate the mth combination element much faster than an iterative solution for large values of m, my **Element()** method was not coded for optimum speed. The algorithm I implemented in this article was designed for clarity rather than performance. In particular, I used a crude way to find the values of the combinadic. As you may recall, I started at n-1, computed **Choose(n-1,k)** and if that result was greater than m, then I tried 1 less, and so forth until I found a value for the combinadic. For large values of n, a binary search approach could improve performance. I could also have improved performance by recasting the **Element()** method to eliminate calls to the **Choose()** and **LargestV()** helper methods.

While researching this article, I discovered that B. P. Buckles and M. Lybanon published an article and algorithm titled, "Algorithm 515: Generation of a Vector from the Lexicographical Index" in the June, 1977 issue of ACM Transactions on Mathematical Software. I was not able to access the article online because it required a subscription. The article implements an alternative, but copyrighted algorithm in Fortran.



