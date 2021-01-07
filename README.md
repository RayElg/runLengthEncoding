# runLengthEncoding
Run-Length compression algorithm

Run length encoding is a simple compression algorithm useful for files with long sequences of repeated bytes (certain uncompressed images). Run length encoding would compress the following ten bytes:

 A A A A A B C C C C
 
Into 7 bytes

 A A [5] B C C [4]

Example:

**uncompressed** - 1.16 kb
```
The  following sequence is "x" 1020 times (255 * 4)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
It will be written as xx[255] 4 times

Abcde
abaaccaaaaaddeeeffgggghhiiii
Raynor Elgie
AAAAABBBCCCCDDDDEEEEFFFF
```

**compressed** - 185 bytes
```
The  following sequence is "x" 1020 times (255 * 4)
xxÿxxÿxxÿxxÿ
It will be written as xx[255] 4 times

Abcde
abaaccaaddeeffgghhii
Raynor Elgie
AABBCCDDEEFF
```

### Usage:
Running compress.py will compress the contents of unCompressed.txt, output file being compressed.txt  
Running decompress.py will uncompress the contents of compressed.txt, output file being deCompressed.txt
 
As with any compression algorithm, not all inputs are compressible

https://en.wikipedia.org/wiki/Run-length_encoding
