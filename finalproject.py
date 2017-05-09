import string
import time

def palindrome_checker(word):    #checks if word is palindrome. Returns True if palindrome, else returns False.
    length= len(word)
    if length==0:
        return False
    if length==1:
        if word== "a" or word=="i":
            return True
        else:
            return False      
    if not word.isalpha():       
        return False
    
    if length>1:
        
        word = word.lower()     #convert the word into lower case and then compare.
        compare = word[length:0:-1]+word[0]    #adding word[0] because previous slice doesn't include last index(0).
        if word == compare:
            return True
        else:
            return False




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



allwords={}    #dictionary to store occurrences of each word.
allletters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lettercount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    #list to store occurrences of each letter. 
palindromes={}     #dictionary to store occurrences of each palindrome.



#error handling while taking input for filename in case file name is invalid.

count=0   #variable to check if errors have previously occurred while enterring filename.

while True:
    try:
        if count==0:    #no errors have previously occurred.
            inputed_file_name= raw_input("please enter address of text file to be evaluated: ")
            pride= open(inputed_file_name, "r")    #opening file in read mode.
            print "File accepted. Evaluation in process"
            break
        
        if count >0:    #error has previously occurred.
            inputed_file_name= raw_input("File name not recognized. Please reenter: ")
            pride= open(inputed_file_name, "r")
            print "File accepted. Evaluation in process"
            break

            
    except:   #if error occurs
       count= count+1

count=0 #resetting variable for future use.



for line in pride:   #iterating through the file line by line.

    temp= line.strip()  #removing all spaces before and after each line.
    newwords= words(temp,lettercount)   #calls function words defined above.

    for word in newwords:    
        
        if (palindrome_checker(word)):   #calls palindrome_checker function defined above to check if word is palindrome.
            if word not in palindromes:
                palindromes[word]=1   #adds new key and value to palindrome dictionary if not already present in it.
            else:
                palindromes[word]+= 1   #edits value of preexisting key  
            
        if word not in allwords:    #adds new key and value to allwords dictionary if not already present in it.
            allwords[word]=1

        else:    #only eidts value if word is already present.
            allwords[word]= allwords[word]+1



perclettercount=[]

count= 0
for letter in lettercount:
    count= count+ letter     #counts total number of letters to calculate percentage occurrence of each letter.


print "\n \n \nOccurences of Each Letter in the given text \n \n"
time.sleep(1)    #pause after print statement allows user to read. 

for i in range(0,26):
    perc= (float(lettercount[i])/count)*100
    perclettercount += [perc]
    
    print allletters[i], ":", lettercount[i], " "*(8-len(str(allletters[i])+":"+str(lettercount[i]))),"(", '%.2f' %perc, "%", ")"   #string after third comma is to calculte number of spaces to print for editing purposes.

time.sleep(1)

words_printed= int(raw_input("\nHow many of the top most frequently occurring words do you want to see: "))
print "\n"
time.sleep(1)

import operator
sorted_allwords = sorted(allwords.items(), key=operator.itemgetter(1))   #converts the dictionary into a list of sorted lists on the basis of values.
sorted_palindromes= sorted(palindromes.items(), key= operator.itemgetter(1))
                       
count=1
for i in range (len(sorted_allwords)-1, len(sorted_allwords)-(words_printed+1),-1):   #Iterates through the most frequent words in descending order
    print str(count)+ ")", sorted_allwords[i][0], " "*(18- len(str(count)+ ")"+ (str(sorted_allwords[i][0])))), ":", sorted_allwords[i][1], "occurences"
    
    count += 1

time.sleep(0.5)
print "\n \n \nOccurences of Palindromes in the given text \n \n"
time.sleep(1)

count=1
for i in range(len(sorted_palindromes)-1, -1,-1):
    print str(count)+ ")", sorted_palindromes[i][0], " "*(15- len(str(count)+")"+ (str(sorted_palindromes[i][0])))), ":", sorted_palindromes[i][1]
    count+=1


#Program to print graph of percentage of each letter occurrence.

import numpy as np
import matplotlib.pyplot as plt

N = 26

ind = np.arange(N)  # the x locations for the groups
width = 0.45    # the width of the bars

ax = plt.subplots()[1]   #plt.subplots()[1] returns the axes objects that are later used to specify the labels and ticks.

white_means = (14, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
rectdummy = ax.bar(ind + width, white_means, width, color='w')   #dummy values to get the scale correct. Printed in white so invisible.

#bars of the expected letter frequencies of each letter
expected_means = (8.16, 1.49, 2.78, 4.25, 12.70, 2.22, 2.01, 6.09, 6.96, 0.15, 0.77, 4.02, 2.40, 6.74, 7.50, 1.92, 0.09, 5.98, 6.32, 9.05, 2.75, 0.97, 2.36, 0.15, 1.97, 0.07)
expectedbars = ax.bar(ind, expected_means, width, color='yellow')

#bars of the actual letter frequencies of each letter.
actual_means = perclettercount
actualbars = ax.bar(ind + width, actual_means, width, color='lightblue')

# labels, title and axes ticks for the graph
ax.set_ylabel('Percentage')
ax.set_xlabel('Letter')
ax.set_title('Expected vs Actual Letter Frequency \n(Please Maximize Window)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))

ax.legend((expectedbars[0], actualbars[0]), ('Expected', 'Actual'))   #expectedbars[0] returns colour of said bar 


def label(rects):    #adding a label to print the letter frequency above each graph.
   
    for rect in rects:
        plt.rcParams.update({'font.size': 6})   #updates font size to be used above each rectangle.

        height = (rect.get_height())    
        ax.text(rect.get_x() + rect.get_width()/2.0, 1.0*height,
                '%.1f' % float(height),
                ha='center', va='bottom')   #specifying position of text above each bar"

label(expectedbars)
label(actualbars)

graph_print ='n'  #setting variable of y/n flag as "n" initially
count=0
print 
while graph_print != 'y':
    if count== 0:
        graph_print= raw_input("display graph showing letter frequencies (y/n)?")
    if count >0:
        graph_print= raw_input("Input not recognized. If you want graph, enter 'y'. Otherwise, enter 'n'") 
        
    if graph_print.lower()=='y':
        plt.show()   #if flag is yes, graph is shown.
        break
    elif graph_print.lower()=='n':
        print "ok, not showing graph"
        break
    else:
        count += 1



