import hang_man






def game():

    print(hang_man.title)   
    
    while hang_man.check in hang_man.chosenlist and hang_man.wrong <= 5:

        guess = input("guess a letter: ").lower()


        
    
     
        if guess not in hang_man.chosenword and hang_man.wrong == 0:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[1])
        elif guess not in hang_man.chosenword and hang_man.wrong == 1:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[2])
        elif guess not in hang_man.chosenword and hang_man.wrong == 2:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[3])
        elif guess not in hang_man.chosenword and hang_man.wrong == 3:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[4])
        elif guess not in hang_man.chosenword and hang_man.wrong == 4:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[5])
        elif guess not in hang_man.chosenword and hang_man.wrong == 5:
            print("not in word")
            hang_man.wrong +=1
            print(hang_man.HANGMANPICS[6])
            print(f"GAME OVER {hang_man.chosenword.upper()} WAS THE CORRECT WORD")
            
                            

        #checks if a letter is in the chosen word and then
        #sets it equal to the index in chosen list. 
        for i in range(0,len(hang_man.chosenword)):
            if guess in hang_man.chosenword[i]:
                hang_man.chosenlist[i] = guess
                print(hang_man.HANGMANPICS[hang_man.wrong])
            


        if hang_man.wrong <= 5:
            result = ' '.join(hang_man.chosenlist)
            print(result)

    if hang_man.check not in hang_man.chosenlist:
        print("YOU WIN")

game()