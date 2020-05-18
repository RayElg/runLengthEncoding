#If this algorithm finds a byte repeated twice (signifies a run)
#It will write the byte [following byte] times and advance to the next two

#Single unrepeated bytes (no run) will be written once and
# the algorithm will advance by one byte


out = open("deCompressed.txt","wb")
with open("compressed.txt","rb") as file:
    b1 = file.read(1) #Read first two bytes
    b2 = file.read(1)
    while(b1): #While the end hasn't been reached
        if(b1==b2): #If theres a byte repeated(a run)
            runLength = file.read(1) #Read length
            for i in range(0,int.from_bytes(runLength, byteorder='big')):
                out.write(b1) #Repeat byte length times
            b1 = file.read(1) #Advance to the next two bytes
            b2 = file.read(1)
        else: #No run
            out.write(b1) #Write the byte once
            b1 = b2 #Advance by one byte
            b2 = file.read(1)

out.close()
