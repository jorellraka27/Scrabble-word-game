#

#to be completed by students
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
alphabets = VOWELS + CONSONANTS

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():# Load the WORDLIST_FILENAME and transfer its data into the list wordlist
  
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())#adding all the valid words into the wordlist list
    print("  ", len(wordlist), "words loaded.")
    return wordlist #return the value wordlist: list


def get_word_score(word, n):#Getting the score for the valid word entered by the user
  
    wordlower = word.lower()#convert the string in word into all lower case. Data is kept in wordlower
    firstcomponent = 0 #score for the first component of the score system
    n2 = 0 # variable which represent the position of letter in the string(e.g n2=0 represent the 1st letter in the string) 
    for x in range(len(wordlower)):# x is a control variable which allows the loop to occur as many as the number of letters in the word
        firstcomponent = firstcomponent + SCRABBLE_LETTER_VALUES[wordlower[n2]]#adding the firstcomponent with the score value of the letter in "n2" position of the wordlower
        n2 = n2+1#increment the position of letter(n2) each loop
    secondcomponent = (7*len(wordlower)) -( 3*(n - len(wordlower)))#the score for the second component of the scoring system, where n represent the number of letter in the current hand
    
    if secondcomponent < 1:# if the score component is less than 1, the secondcomponet score will automatically be 1
        secondcomponent = 1
    score = firstcomponent + secondcomponent# adding firstcomponent and secondcomponent for the final score
    return score
  
def display_hand(hand):# displays the letters in the current hand
   for l in hand:#l represent letter in hand
    if hand[l] >= 0:
      for c in range(hand[l]):# c is a condition variable which loop the code as many as the value of the letter in the current hand
       print(l, end = " ")


  
def deal_hand():# deal the hand with 3 vowels and other 4 letters from the alphabet
    alphabets = VOWELS + CONSONANTS 
    hand1 = []#list 
    hand= {}
    for vowel in range(3):
        v = random.randint(0,4)
        hand1.append(VOWELS[v])
    for letter in range(4):
        v = random.randint(0,25)
        hand1.append(alphabets[v])
    for letter in hand1:
        if letter in hand:
            hand[letter] = hand[letter]+1
        else:
            hand[letter] = 1

	
	
    return hand
def update_hand(hand, word):
   
    
   
    wordlower = word.lower()
    newhand = hand
    order = 0
    for l in range(len(wordlower)):
      if wordlower[order] in newhand:
          if newhand[wordlower[order]] > 1:
              newhand[wordlower[order]] = newhand[wordlower[order]]-1
          else:
            del newhand[wordlower[order]]
      order = order + 1
    return newhand
              
           
    



    
def is_valid_word(word, hand, word_list):
   
    wordlower = word.lower()
    letterposition = 0
    numberoftruewords = 0
    boolean1 = wordlower in word_list
    for letter in range(len(word)):
     if wordlower[letterposition] in hand:
         numberoftruewords = numberoftruewords+1
     letterposition = letterposition+1
     if numberoftruewords == len(wordlower):
      boolean2 = True
     else:
      boolean2 = False
    if boolean1 == True & boolean2 == True:
        boolean = True
    else:
        
       boolean = False



    return boolean

 

def play_hand(hand, word_list):

 totalscore = 0
 playhand= {}
 for w in  hand:
      playhand[w] = hand[w]
 gameover = "ran out of letters"
 while len(playhand) > 0:
     n=0
     for alp in playhand:
      n = n + playhand[alp]
     display_hand(hand)
     word = input("Please enter a word or '!!' to indicate you are done: ")
     if word != "!!":
         if is_valid_word(word, hand, word_list) == True:
           totalscore = totalscore + get_word_score(word, n)

           print(word,"earned:",get_word_score(word, n),"point")
           print("Total:",totalscore)
           print("")
         else:
              print("word invalid")
              print("")

         playhand = update_hand(hand, word)

     else:
         gameover = ""
         break
 if gameover == "ran out of letters":
         print(gameover)
 print("Total score for this hand:",totalscore)
 print("--------")

 return totalscore

def substitute_hand(hand, letter):
 
  subtitutehand ={}
  nosubtituteletter = hand[letter]
  for w in  hand:
      subtitutehand[w] = hand[w]
  randnum = random.randint(0,25)
  subletter = alphabets[randnum]
  for numofletter in range(0,nosubtituteletter):
      while subletter in hand:
 
        randnum = random.randint(0,25)
        subletter = alphabets[randnum]
      if subletter in subtitutehand:
          subtitutehand[subletter] = subtitutehand[subletter] + 1
      else:
          subtitutehand[subletter] = 1
      for w in hand:
       subletter = w
  del subtitutehand[letter]
     
  return subtitutehand





    
       
    
def play_game(word_list):

 hand = deal_hand()
 handori = {} #hand original after substitution
 
 totalgamescore = 0
 #subtitute 
 display_hand(hand)
 change = input("Would you like to substitute a letter? (enter y to substitute):")
 if change == "y":
    letter = input("enter the a letter?: ")

    hand = substitute_hand(hand, letter)
 for w in hand:
  handori[w] = hand[w]

 #playhand
 handscore = play_hand(hand, word_list)
 totalgamescore = totalgamescore + handscore
 print("totalgamescore: ",totalgamescore)
 replayhand = input("replay hand? (enter y to  play again): ")
 #replayhand
 while replayhand == 'y':
    for w in handori:
        hand[w] = handori[w]
    handscore = play_hand(hand, word_list)
    totalgamescore = totalgamescore + handscore
    print("totalgamescore: ",totalgamescore)
    replayhand = input("replay hand?: ")

 
 



 playagain = input("play again? (enter y to play again): ")
 #play again
 while playagain == "y":
  hand = deal_hand()
  handori = {} #hand original after substitution
 
 #subtitute 
  display_hand(hand)
  change = input("Would you like to substitute a letter? (enter y to substitute): ")
  if change == "y":
    letter = input("enter the a letter?: ")

    hand = substitute_hand(hand, letter)
  for w in hand:
   handori[w] = hand[w]

 #playhand
  handscore = play_hand(hand, word_list)
  totalgamescore = totalgamescore + handscore
  print("totalgamescore: ",totalgamescore)
  replayhand = input("replay hand? (enter y to replay): ")
 #replayhand
  while replayhand == 'y':
    for w in handori:
        hand[w] = handori[w]
    handscore = play_hand(hand, word_list)
    totalgamescore = totalgamescore + handscore
    print("totalgamescore: ",totalgamescore)
    replayhand = input("replay hand? (enter y to replay): ")
  playagain = input("play again? (enter y to play again): ")
 print("totalgamescore: ",totalgamescore)

word_list = load_words()
play_game(word_list)
