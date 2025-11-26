#Remove first n character from a string Write a program to remove character from a string strting from zeri up to n and return a new string
#For example:
#remove_chr("pynative",4) so output must be live.Here we need to remove first four character from a
#string remove_char("pynative",2)so output must be native. here we need to remove first two characters from a string Note; n must be less than the lenghth of the string.

def remove (word,n):

    x=len(word)
    p=list(word)

    for i in p:
        if n<=x:
            z=word[n:]
    print(z)
remove("pynative",2)