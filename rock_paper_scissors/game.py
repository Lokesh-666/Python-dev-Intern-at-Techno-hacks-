def pc_plays():
    # Import the random module
    import random
    
    # Randomly select between ROCK, PAPER, SCISSORS
    pc_Plays = random.randint(1, 3)
    if pc_Plays == 1:
        pc_Plays = "ROCK"
    elif pc_Plays == 2:
        pc_Plays = "PAPER"
    elif pc_Plays == 3:
        pc_Plays = "SCISSORS"
    return pc_Plays

def decideWinner(pc_Plays, Player):
    # Convert inputs to uppercase to standardize
    pc_Plays = pc_Plays.upper()
    Player = Player.upper()
    
    # Determine the winner based on the rules of the game
    match pc_Plays:
        case "ROCK":
            match Player:
                case "ROCK":
                    print("It's a tie!")
                case "PAPER":
                    print("You Win!")
                    print("Keep it up!!")
                case "SCISSORS":
                    print("Ohh No, You Lost!")
                    print("Try Again")
        case "PAPER":
            match Player:
                case "ROCK":
                    print("Ohh No, You Lost!")
                    print("Try Again")
                case "PAPER":
                    print("It's a tie!")
                case "SCISSORS":
                    print("You Win!")
                    print("Keep it up!!")
        case "SCISSORS":
            match Player:
                case "ROCK":
                    print("You Win!")
                    print("Keep it up!!")
                case "PAPER":
                    print("Ohh No, You Lost!")
                    print("Try Again")
                case "SCISSORS":
                    print("It's a tie!")

def play_game():
    # Announce the game
    print("ROCK, PAPER, SCISSORS")
    
    # Get the computer's choice
    PC = pc_plays()
    
    # Get the player's choice
    player = str(input("What do you choose (ROCK / PAPER / SCISSORS): "))
    
    # Decide the winner
    decideWinner(PC, player)

def main():
    # Ask if the user wants to play the game
    print("Do you wish to play ROCK, PAPER, SCISSORS??")
    answer = str(input("Y/N? "))
    
    # If the user wants to play
    if answer.upper() == "Y":
        print("Let's Play!!")
        
        # Ask how many times the user wants to play
        NumberOfGamePlays = int(input("How many times do you wish to play: "))
        
        # Play the game the specified number of times
        i = 0
        while i < NumberOfGamePlays:
            play_game()
            i = i + 1
    else:
        # If the user doesn't want to play
        print("Goodbye")

# Run the main function
if __name__ == '__main__':
    main()
