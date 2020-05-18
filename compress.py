#Run length encoding is a simple compression algorithm useful for files with long sequences of repeated bytes (certain uncompressed images)
#Run length encoding would compress the following ten bytes:
# A A A A A B C C C C
#Into 7 bytes
# A A [5] B C C [4]
#As with any compression algorithm, not all inputs are compressible

#Writes sequences of 2+ repeated bytes as Byte Byte [Length]
#Writes single bytes as Byte
out = open("compressed.txt","wb")
with open("unCompressed.txt","rb") as file:
    byte = file.read(1) #Read in the first byte
    prevByte = byte
    runLength = 0 #Length this byte has ran for
    while prevByte: #Until we reach end of file
        if((byte==prevByte) & (runLength < 255)): #If the run contines & we haven't reached max val in one byte
            runLength += 1
        elif((runLength > 1) or (runLength == 255)): #If this run either stopped here or we've reached 255
            out.write(prevByte) #Write Byte Byte (signify a run)
            out.write(prevByte)
            out.write(bytes([runLength])) #Write byte representation of the run length
            runLength = 1 #Reset runlength
        elif(runLength == 1): #If the run was only one long,
            out.write(prevByte) #Write just Byte to represent this
            runLength = 1 #Reset runlength

        prevByte = byte #Advance
        byte = file.read(1)
out.close()
