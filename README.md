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

python only supports arthmetic shift 

