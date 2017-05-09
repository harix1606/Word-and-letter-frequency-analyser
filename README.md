# pride-and-prejudice
def words(line, lettercount):            #defining function which seperates line into words and counts letters. 
    vals=[0]      #saves the indices where a space (" ") occurred. Adding index where first word starts (0).                          
    for i in range(0,len(line)):
        c=line[i].lower()     #c for character. 
        if c== " ":
            vals= vals+[i]    #saves index if c was space.
        if c == "a":          #else adds one to the value corresponding to the letter key in dictionary defined below.
            lettercount[0]+= 1
        if c == "b":
            lettercount[1]+= 1
        if c == "c":
            lettercount[2]+= 1
        if c == "d":
            lettercount[3]+= 1
        if c == "e":
            lettercount[4]+= 1
        if c == "f":
            lettercount[5]+= 1
        if c == "g":
            lettercount[6]+= 1
        if c == "h":
            lettercount[7]+= 1
        if c == "i":
            lettercount[8]+= 1
        if c == "j":
            lettercount[9]+= 1
        if c == "k":
            lettercount[10]+= 1
        if c == "l":
            lettercount[11]+= 1
        if c == "m":
            lettercount[12]+= 1
        if c == "n":
            lettercount[13]+= 1
        if c == "o":
            lettercount[14]+= 1
        if c == "p":
            lettercount[15]+= 1
        if c == "q":
            lettercount[16]+= 1
        if c == "r":
            lettercount[17]+= 1
        if c == "s":
            lettercount[18]+= 1
        if c == "t":
            lettercount[19]+= 1
        if c == "u":
            lettercount[20]+= 1
        if c == "v":
            lettercount[21]+= 1
        if c == "w":
            lettercount[22]+= 1
        if c == "x":
            lettercount[23]+= 1
        if c == "y":
            lettercount[24]+= 1
        if c == "z":
            lettercount[25]+= 1
    vals= vals+[len(line)+1]    #adds index where the last word ends
    newwords= []     #lsit that will store all the words.

    for i in range (0, len(vals)-1):
        newwords+= [line[vals[i]:vals[i+1]].lower()]   #saving words intoo newwords. 
        
    for index in range(0, len(newwords)):
        newwords[index]= newwords[index].strip(string.punctuation).strip().strip('"()')     #removing all punctuation that occurrs before and after words.
        

        

    return newwords    #returning the list of words.
