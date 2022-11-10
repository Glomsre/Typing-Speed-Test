from tkinter import *
import time

t = 60
tw = 0
cw = 0

s = 'There are many idiosyncratic typing styles in between novice-style "hunt and peck" and touch typing. For example, ' \
    'many "hunt and peck" typists have the keyboard layout memorized and are able to type while focusing their gaze on ' \
    'the screen.'

list_words = s.split()

show_words = "\n".join([" ".join(list_words[i:i+15]) for i in range(0, len(list_words), 15)])


def start_timer():
    global t
    input_text.config(state='normal')
    current_word.config(text=list_words[tw])

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        label_time.config(text=f'Time: {t}', bg='yellow')
        window.update()
        if t == 0:
            label_score.config(text=f'Your Score: Correct Words: {cw}, Typed Words: {tw}')
            window.update()
            input_text.config(state='disabled')


def restart():
    global cw
    global tw
    global t

    t = 60
    tw = 0
    cw = 0

    label_words_correct.config(text=f'Correct Words: {cw}')
    label_num_press.config(text=f'Typed Words: {tw}')
    label_time.config(text=f'Time: {t}')
    label_score.config(text=f'Your Score: Correct Words: {cw}, Typed Words: {tw}')
    input_text.config(state='normal')
    current_word.config(text='')
    input_text.delete(0, END)
    start_timer()


def score(event):
    global cw
    global tw
    global t

    my_word = input_text.get()

    if my_word == list_words[tw]:
        cw += 1
        tw += 1
        label_words_correct.config(text=f'Correct Words: {cw}')
        label_num_press.config(text=f'Typed Words: {tw}')
        window.update()
        input_text.delete(0, END)

    elif my_word == (str(' ') + list_words[tw]):
        cw += 1
        tw += 1
        label_words_correct.config(text=f'Correct Words: {cw}')
        label_num_press.config(text=f'Typed Words: {tw}')
        window.update()
        input_text.delete(0, END)
    else:
        tw += 1
        label_num_press.config(text=f'Typed Words: {tw}')
        window.update()
        input_text.delete(0, END)

    if len(list_words) == tw:
        tw = 0


window = Tk()
window.title('typing Speed Test')
window.config(padx=10, pady=10)


label_info = Label(window, font=('Helvetica', 14), text=f'How fast are you typing?\nYou have a minute to find out '
                                                       f'how fast you are.\nPress the space after each word')

label_info.grid(row=0, column=1, columnspan=7, pady=10)

button_start = Button(window, text="START", command=start_timer)
button_start.grid(row=1, column=1, columnspan=7, pady=10)

label_score = Label()
label_score.grid(row=2, column=1, columnspan=7)

label_line = Label(text='________________________________________________________________________________________')
label_line.grid(row=4, column=1, columnspan=7, pady=10)


label_words_correct = Label(window, text=f'Correct Words: {cw}')
label_words_correct.grid(row=5, column=1, padx=10)

label_num_press = Label(window, text=f'Typed Words: {tw}')
label_num_press.grid(row=5, column=3, padx=10)

label_time = Label(window, font=('Helvetica', 14), text=f'Time: {t} sec')
label_time.grid(row=5, column=5, padx=10)

button_restart = Button(window, text="Restart", command=restart)
button_restart.grid(row=5, column=7)

label_text = Label(font=('Helvetica', 20), text=show_words)
label_text.grid(row=6, column=1, columnspan=7, pady=10)

current_word = Label(text='Current Word')
current_word.grid(row=7, column=1, padx=10)

input_text = Entry(window, font=('Helvetica', 20), state='disabled')
input_text.bind("<space>", score)
input_text.grid(row=7, column=2, columnspan=6, pady=10)


window.mainloop()
