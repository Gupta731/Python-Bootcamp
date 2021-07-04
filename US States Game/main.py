import turtle
import pandas
from write_name import WriteName

screen = turtle.Screen()
screen.setup(width=730, height=495)
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
answer_list = []

write_name = WriteName()

states_data = pandas.read_csv('50_states.csv')
while len(answer_list) < 50:
    answer_state = screen.textinput(title=f'{len(answer_list)}/50 States Correct',
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break

    data = states_data[states_data.state == answer_state]
    if not data.empty:
        state = data.state.item()
        if state not in answer_list:
            xcor = int(data.x)
            ycor = int(data.y)
            answer_list.append(state)
            write_name.writer(state, xcor, ycor)

state_list = states_data.state.to_list()
states_to_learn = [item for item in state_list if item not in answer_list]
df = pandas.DataFrame(data=states_to_learn, columns=["states_to_learn"])
df.to_csv('states_to_learn.csv')
screen.exitonclick()
