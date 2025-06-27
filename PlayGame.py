import csv
import random
import re
class Player:
    def __init__(self,name,playertype):
        self.name=name
        self.playertype=playertype

class Player1(Player):
    def __init__(self,name,fileno,playertype=1):
        super().__init__(name,playertype)
        self.filename=fileno
        self.wordlist = []
        self.opponent=""
        self.opponent_guessword=""
        self.opponent_guessposition = None
    
    def validate_word(self,word):
        if not re.fullmatch(r'[A-Za-z]+', word):
            raise ValueError(f"Invalid word: '{word}' (must contain only alphabets).")
        
    def read_words_from_file(self,filename):
        nos_words=10
        with open(self.filename,newline='') as fp:
            reader = csv.reader(fp)
            header = next(reader, None)
            words = [row[0] for row in reader if row]
            if len(words) < nos_words:
                raise ValueError(f"File must contain at least {nos_words} words. ")
            random.shuffle(words)
            nextwords = words[:10]
            for word in nextwords:
                self.validate_word(word)
            yield nextwords

    def query_process(self,wordlist,player2):
        print("3 chances given to guess the word")
        count = 0
        while count < 3:
            print("Guess : ", count+1)
            ans = player2.makewordguess()
            if ans in wordlist:
                self.opponent_guessword=ans
                player2.guessword=ans
                player2.level=1
                print("\nCorrect Guess !! Congratulations !!")
                print("You enter Level 2 now !!")
                break
            else:
                count += 1
        else:
            print("\n3 chances finished for guessing the right word")
            print(player2.name, ", Sorry, You have lost the game")
            player2.status="Lost"
            return None
        print(f"\nGuess {self.opponent_guessword}'s position ")
        print("2 chances given to guess its position\n")
       
        '''for i,j in enumerate(self.wordlist):
                        print(i,j)'''
        count = 0
        pos=None
        while count < 2:
            print("Guess : ",count+1)
            guesspos = player2.makeposguess()
            try :
                gotpos = wordlist.index(player2.guessword)
                print("Position found in wordlist ",gotpos)
            except ValueError as e:
                print(f"Guessed value missing in list {player2.guessword!s}")
                exit()
            for i,j in enumerate(self.wordlist):
                print(i,j)
            if gotpos == guesspos:
                self.opponent_guessposition=guesspos
                player2.positionguess=guesspos
                player2.status="Won"
                player2.level=2
                print("Congratulation !! You have Won the game")
                break
            else:
                print(f"Sorry guessed wrong. You have used {count+1} out of 2 chances ")
                count += 1
        else:
            print("2 chances finished for guessing the right position")
            print(player2.name, ", Sorry, You have lost the game")
            player2.positionguess=guesspos
            self.opponent_guessposition=guesspos
            player2.status="Lost"
            player2.level=1
            return self.opponent_guessword,self.opponent_guessposition
    def result_declaration(self, player2):
        print(f"\nResult Declaration of game : Player1 - {p1.name} and Player2 - {p2.name}")
        print('='*65)
        print(f"{player2.name} has {player2.status} and completed level {player2.level}")
        print('='*65)
        if player2.level > 0:
            actpos=self.opponent_guessposition
        else:
            actpos = None
        return player2.guessword, player2.positionguess, actpos

class Player2(Player):
    def __init__(self,name,playertype,statusp):
        super().__init__(name,playertype)
        self.status=statusp
        self.guessword=""
        self.positionguess=None
        self.level = 0
    def makewordguess(self):
        print("Guessing word ...")
        self.guessword=input("My guess : ")
        return self.guessword.lower()
    def makeposguess(self):
        print(f"Guessing Position for {self.guessword} ...")
        self.positionguess = int(input("My guess is :  "))
        return self.positionguess
print("Start of Play")
print("Enter names of two players : ")
a = input("Enter a name : ")
b = input("Enter another name : ")
while True:
    x = int(input(f"{a} is Player 1 or Player 2 ? (Enter 1 or 2) : "))
    if x == 1:
        p1=Player1(a,"a.csv",1)
        p2=Player2(b,2,"Playing")
    else:
        p1=Player1(b,"b.csv",1)
        p2=Player2(a,2,"Playing")
    genwordlist = p1.read_words_from_file(p1.filename)
    p1.wordlist = next(genwordlist)
    print("word list")
    #print(p1.wordlist)
    onep = p1.query_process(p1.wordlist,p2)
    output = p1.result_declaration(p2)
    for x,y in enumerate(p1.wordlist):
        print(x,y)
    print("\nWord Guessed : ", output[0])
    print("Position guessed : ", output[1])
    print("Position of the word : ", output[2])
    ans = input("\nWish to play again (y/n) ? ")
    ans = ans.lower()
    if ans == 'n':
        print("Game End !!")
        break
    print("Playing again !!")
print("Hope you liked the game !!")


        
        

    






