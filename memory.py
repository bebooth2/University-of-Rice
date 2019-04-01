# implementation of card game - Memory
# To play the game go to
# http://www.codeskulptor.org
# and clear the screen and copy and past this code 
import simplegui
import random
import math
cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
card_play=['','','','','','','','','','','','','','','','']
card_stay = ['','','','','','','','','','','','','','','','']
random.shuffle(cards)
card_stay_array = []
# helper function to initialize globals
def new_game():
    global state, index, index2, turn, turns
    state = 0
    turn = 0
    turns = "0"
    index = 16
    index2 = 16
   
    
     
# define event handlers#
def mouseclick(pos):
    global state,index, index2,card_play, turns, turn, card_stay_array
    card_position = pos[0]//50
    turn +=.5
    turns = str(int(math.floor(turn)))
    if card_position in card_stay_array:
        turn -=.5
        state = state
    
    elif state == 0:
        state = 1
        card_play[card_position] = cards[card_position]
      
        index = card_position
        print(index)
    elif state == 1:
        state = 2
        card_play[card_position] = cards[card_position]
      
        index2 = card_position
        if card_play[index] == card_play[index2]:
            card_stay[index] = card_play[index]
          
            card_stay[index2] = card_play[index2]
            card_stay_array.extend([index,index2])
            print(card_stay_array)
    else:
        state = 1
       
        
        card_play[index] = ""
        card_play[index2] = ""
        card_play[card_position] = cards[card_position]
      
        index = card_position
        print(index)
        
        
    
    
    
       
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        width_lf = i*50
        width_rt = (i+1)*50
        text_position = [width_lf+6,75]
        canvas.draw_polygon([[width_lf, 0],[width_rt,0], [width_rt, 100], [width_lf, 100]], 8, "Green")
        canvas.draw_text(str(card_play[i]), text_position, 75, "White")
        canvas.draw_text(str(card_stay[i]), text_position, 75, "Blue")
        label.set_text("Turns = " + turns)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
#frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric