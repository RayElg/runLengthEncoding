# runLengthEncoding
Run-Length compression algorithm

Run length encoding is a simple compression algorithm useful for files with long sequences of repeated bytes (certain uncompressed images)
Run length encoding would compress the following ten bytes:
 A A A A A B C C C C
Into 7 bytes
 A A [5] B C C [4]
As with any compression algorithm, not all inputs are compressible

https://en.wikipedia.org/wiki/Run-length_encoding
