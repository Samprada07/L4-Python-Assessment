import enchant
import sys

class Decryptor:
    #constructor to initialize fileName when object is made
    def __init__(self, fileName):
        self.fileName = fileName
        self.dict = enchant.Dict("en_US")
        
    def fileReader(self):
        with open(self.fileName, 'r') as init_file:
            en_mesg = init_file.read()
            return en_mesg
        
    def getDecryptedOutput(self, shiftNum, en_msg):
        de_msg_list = [] # declaring list to store decrpyed letter
        # iteration over encrypeted message of file by single character
        for w in en_msg:
            # if character is upper case it's asci code starts with 65
            if w.isupper(): 
                asciValue = ord(w) # to obtain the ascii code of english character
                deAsciVal = asciValue + shiftNum # decryption is done adding shift number to character ascii code
                #if character's ascii code elasped 90 then should be substracted from 26(for eg: 92=>(92-26)=>66=>B ) 
                if(deAsciVal > 90):
                    deAsciVal = deAsciVal - 26
                de_char = chr(deAsciVal) # again character ascii code change into character
            # if character is lower case it's asci code starts with 97
            elif w.islower():
                #same logic as for upper case except it's ascii code starts with 97
                asciValue = ord(w)
                deAsciVal = asciValue + shiftNum
                if(deAsciVal > 122):
                    deAsciVal = deAsciVal - 26
                de_char = chr(deAsciVal)
            else: 
                # if character is neither upper nor lower case then it is left as usual
                de_char = w
            de_msg_list.append(de_char) # decrpyted character, punctuation and spaces are appended into list 
        return de_msg_list # list is then returned
    
    #gives the boolean value list checking if word is english or not
    def getPositiveFrequencyList(self, deMesg):
        pos_freq = [self.dict.check(bl) for bl in "".join(deMesg).strip().split(" ")] # boolean true or false is stored to the list 
        return pos_freq
    
    #gives the total percentage of english word in decrypted mesgclear
    def getEnglishWordPercentageInDecMesg(self, decMessage, pos_freq_list):
        return round((max(pos_freq_list)/len(decMessage.split(" ")) * 100), 2)

try:      
    file_name = sys.argv[1]
    decrypt = Decryptor(file_name)
    en_msg = decrypt.fileReader()
    pos_freq_list = []
    for shift_no in range(1, 27):
        deMesgList = decrypt.getDecryptedOutput(shift_no, en_msg)
        pos_freq = decrypt.getPositiveFrequencyList(deMesgList)
        pos_freq_list.append(pos_freq.count(True))
        
    actual_shift_num = pos_freq_list.index(max(pos_freq_list)) + 1
    result = decrypt.getDecryptedOutput(actual_shift_num, en_msg)
    decMessage = "".join(result)
    engWordPer = decrypt.getEnglishWordPercentageInDecMesg(decMessage, pos_freq_list)
    if engWordPer < 80:
        print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")  
    else: 
        print(decMessage)
except FileNotFoundError:
    print("Cannot open " + file_name + ". Sorry about that.")
except IndexError:
    print("Missing command line arguments")
    
    
    
    
    

        
        
        
            