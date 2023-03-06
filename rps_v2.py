# file created by david charles

# import libraries 
from random import randint
from time import sleep
import pygame as pg
import os

# game settings
WIDTH = 1200
HEIGHT = 800
FPS = 30


# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock Paper Scissors ")
clock = pg.time.Clock()
pg.font.init

# setup asset folders
# images and sounds as needed
game_folder = os.path.dirname(__file__)
print(game_folder)


# define colors
# a tuple is like a list but it doesnt change
# colors are defined by rgb values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sets variables to default values so if statements can recognize them
choices = ["ROCK", "PAPER", "SCISSORS"]
user_choice = ""
pc_choice = ""
winner = ""
# allowmouse and allowkey let the user press space or mouse
# toggled true of false depending on when user is allowed to interact
allowkey = True
allowmouse = True

# creates images
rock_image = pg.image.load(os.path.join(game_folder, "rocky.jpg")).convert()
paper_image = pg.image.load(os.path.join(game_folder, "jim.jpg")).convert()
scissors_image = pg.image.load(os.path.join(game_folder, "ezio.jpg")).convert()
background1 = pg.image.load(os.path.join(game_folder, "boxing.jpg")).convert()
# gets geometry of images
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
background1_rect = background1.get_rect()

# provides duplicates for each image in case of tie
rock_image2 = pg.image.load(os.path.join(game_folder, "rocky.jpg")).convert()
paper_image2 = pg.image.load(os.path.join(game_folder, "jim.jpg")).convert()
scissors_image2 = pg.image.load(os.path.join(game_folder, "ezio.jpg")).convert()
rock_rect2 = rock_image2.get_rect()
paper_rect2 = paper_image2.get_rect()
scissors_rect2 = scissors_image2.get_rect()

# creates text for play again
play_font = pg.font.Font(None, 96)
play_surface = play_font.render("PLAY AGAIN?", True, WHITE)
play_rect = play_surface.get_rect()
play_rect.center = (WIDTH // 2, 400)

# defines text for yes option in play again function
yes_surface = play_font.render("YES!", True, GREEN)
yes_rect = yes_surface.get_rect()
yes_rect.center = (450, 480)

#defines text for no option in play again
no_surface = play_font.render("nah", True, RED)
no_rect = no_surface.get_rect()
no_rect.center = (750, 480)

# function to universally draw text
# written by chris cozort
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('impact')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface, text_rect)



# function to tell the player to choose rps 
def display_choices():
    # allows variables to be accessed throughout code
    global pc_choice
    global user_choice
    global allowmouse
    allowmouse = True  
    # creates and blits text for choose your fighter
    if user_choice == "":
        # blits rps and the background
        screen.blit(background1, background1_rect)
        screen.blit(rock_image, rock_rect)
        screen.blit(paper_image, paper_rect)
        screen.blit(scissors_image, scissors_rect)
        # sets paper and scissors at different spots on the screen
        rock_rect.x = 100
        rock_rect.y = 200
        paper_rect.x = 450
        paper_rect.y = 200
        scissors_rect.x= 800
        scissors_rect.y = 200
        # sets text for rps and choose your fighter
        # uses draw text function
        draw_text("CHOOSE YOUR FIGHTER", 96, RED, WIDTH //2, 100)
        draw_text("ROCK", 48, WHITE, 250, 650)
        draw_text("PAPER", 48, WHITE, WIDTH //2, 650)
        draw_text("SCISSORS", 48, WHITE, 950, 650)

# function to display userchoice and pc choice
# called along with display_winner and play_again
def battle_screen():
    # blits background
    screen.blit(background1,background1_rect)
    # randint selects a random rps for pc choice
    pc_choice = choices[randint(0,2)]    

    global allowmouse
    allowmouse = False

    rock_rect.x = 50
    paper_rect.x = 50
    scissors_rect.x = 50
    # blits whatever the user chose on the left 
    if user_choice == "ROCK":
        screen.blit(rock_image,rock_rect)
        draw_text("YOU CHOSE ROCK", 96, RED, WIDTH //2, 100)
    elif user_choice == "PAPER":
        screen.blit(paper_image,paper_rect)
        draw_text("YOU CHOSE PAPER", 96, RED, WIDTH //2, 100)
    elif user_choice == "SCISSORS":
        screen.blit(scissors_image,scissors_rect)
        draw_text("YOU CHOSE SCISSORS", 96, RED, WIDTH //2, 100)
    
    # blits whatever the pc chose on the right
    if pc_choice == "ROCK":
        # rock rect2 is a duplicate of rock rect so two can be on screen if tie
        rock_rect2.x = 850
        rock_rect2.y = 200
        screen.blit(rock_image2,rock_rect2)
    elif pc_choice == "PAPER":
        paper_rect2.x = 850
        paper_rect2.y = 200
        screen.blit(paper_image2,paper_rect2)
    elif pc_choice == "SCISSORS":
        scissors_rect2.x = 850
        scissors_rect2.y = 200
        screen.blit(scissors_image2,scissors_rect2)
    
    # pc_text changes depending on what pc choice is
    pc_text = "THE ADVERSARY CHOSE " + (pc_choice) + "!"
    draw_text(pc_text, 84, RED, WIDTH //2, 700)
    
    # allows winner to be used in the main loop
    global winner

    # if userchoice and pc choice are the same its a tie
    if user_choice == pc_choice:
        winner = "Tie!"
    # any combination where user wins, sets winner to you win
    elif user_choice == "ROCK" and pc_choice == "SCISSORS":
        winner = "You win!"
    elif user_choice == "PAPER" and pc_choice == "ROCK":
        winner = "You win!"
    elif user_choice == "SCISSORS" and pc_choice == "PAPER":
        winner = "You win!"
    # if user doesnt win or tie computer wins
    else:
        winner = "Computer wins!"

    global allowkey
    allowkey = False

# Define a function to display the winner
def display_winner(winner):
    draw_text(winner, 72, WHITE, WIDTH //2, 250)
    global allowmouse
    allowmouse = False

# blits options for play again yes or no
# if you click yes it resets the game
# if you click no it quits
def play_again():
    screen.blit(play_surface, play_rect)
    screen.blit(yes_surface, yes_rect)
    screen.blit(no_surface, no_rect)
    global allowkey
    allowkey = False
    global allowmouse
    allowmouse = False
    #if they click yes 
    if yes_rect.collidepoint(mouse_coords):
        global user_choice
        global pc_choice
        global running
        global winner
        running = True
        allowmouse = True
        allowkey = True
        user_choice = ""
        pc_choice = "" 
        winner = ""
        # refreshes screen
        screen.blit(background1, background1_rect)
        screen.blit(rock_image, rock_rect)
        screen.blit(paper_image, paper_rect)
        screen.blit(scissors_image, scissors_rect)
        # sets paper and scissors at different spots on the screen
        rock_rect.x = 100
        rock_rect.y = 200
        paper_rect.x = 450
        paper_rect.y = 200
        scissors_rect.x= 800
        scissors_rect.y = 200
        # text options
        draw_text("CHOOSE YOUR FIGHTER", 96, RED, WIDTH //2, 100)
        draw_text("ROCK", 48, WHITE, 250, 650)
        draw_text("PAPER", 48, WHITE, WIDTH //2, 650)
        draw_text("SCISSORS", 48, WHITE, 950, 650)
    #if they click no
    if no_rect.collidepoint(mouse_coords):
        # turns off the game
        running = False

# re blits background to clear screen
# depending on what userchoice is it blits one of the rps
def refresh():
    screen.blit(background1, background1_rect)
    if user_choice == "ROCK":
        screen.blit(rock_image, rock_rect)
        draw_text("YOU CHOSE ROCK", 96, RED, WIDTH //2, 100)
    if user_choice == "PAPER":
        screen.blit(paper_image, paper_rect)
        draw_text("YOU CHOSE PAPER", 96, RED, WIDTH //2, 100)
    if user_choice == "SCISSORS":
        screen.blit(scissors_image, scissors_rect)
        draw_text("YOU CHOSE SCISSORS", 96, RED, WIDTH //2, 100)

mouse_coords = pg.mouse.get_pos()

# turns the game on
running = True
#while game is on
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        display_choices()
        # if you press spacebar it runs battle screen
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and allowkey == True:
                battle_screen()
                allowmouse = False
        if event.type == pg.MOUSEBUTTONUP and allowmouse == True:
            # creates a variable to find the x and y positional values of the mouse
            mouse_coords = pg.mouse.get_pos()
            # if user clicks on collison box for rps it sets userchoice
            if rock_rect.collidepoint(mouse_coords) and allowmouse == True:
                #user_choice is used in display choice function and winner
                user_choice = "ROCK"
                rock_rect.x = 450
                paper_rect.x = 2000
                scissors_rect.x = 2000
            if paper_rect.collidepoint(mouse_coords) and allowmouse == True:
                user_choice = "PAPER"
                rock_rect.x = 2000
                paper_rect.x = 450
                scissors_rect.x = 2000
            if scissors_rect.collidepoint(mouse_coords) and allowmouse == True:
                user_choice = "SCISSORS"
                rock_rect.x = 2000
                paper_rect.x = 2000
                scissors_rect.x = 450
            # whenever userchoice equals anything it refreshes
            # refresh blits your fighter 
            # tells you to press space to go to battle screen
            if user_choice != "":
                refresh()
                draw_text("PRESS SPACE TO FIGHT", 96, RED, WIDTH //2, 700)
                allowmouse = False
        # press space to go to battle screen
        elif event.type == pg.KEYDOWN and allowkey == True:
            if event.key == pg.K_SPACE:
                battle_screen()
                allowmouse == False
                            
    # if there is any value for winner, runs display winner function
    # play again function blits yes or no
    if winner != "":
        allowmouse = False
        display_winner(winner)
        play_again()
        display_choices()
    
    # quits the game
    if event.type == pg.QUIT:
        running = False

    #runs display
    pg.display.flip()

pg.quit()