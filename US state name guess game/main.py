import turtle
import pandas
screen=turtle.Screen()
screen.title("US states Guess Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
state_list=data["state"].to_list()
guessed_state=[]
while(len(guessed_state)<50):
    answer = screen.textinput(title=f"Guess the state {len(guessed_state)}/50", prompt="What's another state name")
    answer = answer.title()
    if answer=="Exit":
        learn_list=[]
        for state in state_list:
            if state is not guessed_state:
                learn_list.append(state)
        learn_file=pandas.DataFrame(learn_list)
        learn_file.to_csv("States_to_be_learned.csv")
        break

    if answer in state_list:
        if answer is not guessed_state:
            guessed_state.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            ans_state=data[data.state==answer]
            t.goto(int(ans_state.x),int(ans_state.y))
            t.write(ans_state.state.item())

screen.exitonclick()