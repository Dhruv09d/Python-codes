import tkinter
from tkinter import font
import requests
import datetime
from playsound import playsound



def Weather_forecast():
    Height = 500
    Width = 600
    #to create GUI window
    window = tkinter.Tk()

    # da17b531a0772d971477a83b89291371
    # api.openweathermap.org/data/2.5/weather?q={city name}
    def for_result(weather):
        try:
            Name = weather["name"]
            Description = weather["weather"][0]["description"]
            Temperature = weather["main"]["temp"]
            final_result = "City: %s \nCondition: %s \nTemperature(in celsius): %s"\
                           % (Name, Description, Temperature)

        except:
            final_result = "Error"
        return final_result

    def weather(city):
        weather_key = "da17b531a0772d971477a83b89291371"
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"APPID": weather_key, "q": city, "units": "metric"}
        response = requests.get(url, params=params)
        weather = response.json()
        entry_result['text'] = for_result(weather)

    # to pass multiple function in search button
    def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

    def play():
        playsound("sound/click.mp3")



    # define size of window
    canvas = tkinter.Canvas(window, height=Height, width=Width)
    canvas.pack()

    #************** background image **************#
    background_image = tkinter.PhotoImage(file="img\img.png")
    background_label = tkinter.Label(window, image=background_image)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    #**************  title *********************#
    # top most label,  # co-ordinates relative to window
    label = tkinter.Label(window, text="Weather Forecast",font=40, bg="#fa2fa6")
    label.place(relx=0.2, rely=0.01, relheight=0.05, relwidth=0.6)

    #*************** date ***********************#
    # to input date,  co-ordinates relative to window
    frame_date = tkinter.Frame(window, bg="#fa2fa6")
    frame_date.place(relx=0.2, rely=0.06, relheight=0.05, relwidth=0.6)

    # co-ordinates relative to frame_date
    date = tkinter.Label(frame_date,bg="white", font=("Verdana", 10))
    date.place(relx=0.01, rely=0.06, relheight=0.85, relwidth=0.98)

    # date format (yyyy/mm/dd) time format h:m:s:xxxx
    Date = datetime.datetime.now()
    date["text"] = Date

    #**************  search ********************#

    # frame for input,  co-ordinate relative to window
    frame_input = tkinter.Frame(window, bg="#fa2fa6")
    frame_input.place(relx=0.2, rely=0.12, relheight=0.07, relwidth=0.6)

    #********** search input ******************#

    # co-ordinates relative to frame
    entry_search = tkinter.Entry(frame_input, bg="white", font=10)
    entry_search.place(relx=0.01, rely=0.085, relheight=0.8, relwidth=0.98)

    #************** button *********************#
    # frame for button,  co-ordinates relative to window
    frame_button = tkinter.Frame(window, bg="#fa2fa6")
    frame_button.place(relx=0.2, rely=0.22, relheight=0.05, relwidth=0.3)

    # frame for Exit button, co-ordinate relative to window
    frame_quit_button = tkinter.Frame(window, bg="#fa2fa6")
    frame_quit_button.place(relx=0.5, rely=0.22, relheight=0.05, relwidth=0.3)

    # search button
    button = tkinter.Button(frame_button, text="Search", font=25,
    bg="#ffffff", bd=5, command=combine_funcs(lambda: play(), lambda: weather(entry_search.get())))

    # relative to frame button
    button.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.98)

    # exit button
    button = tkinter.Button(frame_quit_button, text="Exit", font=25,
    bg="#ffffff", bd=5, command=combine_funcs(lambda: playsound('sound/exitd.mp3'),quit))
    button.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.98)

    #************** result *********************#

    # result frame, co-ordinates relative to window
    frame_result = tkinter.Frame(window, bg="#fa2fa6")
    frame_result.place(relx=0.2, rely=0.3, relheight=0.5, relwidth=0.6)

    entry_result = tkinter.Label(frame_result, bg="white", font=("Verdana", 15))
    entry_result.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

    #************ side frame ********************#
    frame_left = tkinter.Frame(window, bg="#fa2fa6")
    frame_left.place(relx=0, rely=0, relheight=1, relwidth=0.01)

    frame_right = tkinter.Frame(window, bg="#fa2fa6")
    frame_right.place(relx=0.99, rely=0, relheight=1, relwidth=0.01)

    frame_bottom = tkinter.Frame(window, bg="#fa2fa6")
    frame_bottom.place(relx=0, rely=0.99, relheight=0.01, relwidth=0.99)

    frame_top = tkinter.Frame(window, bg="#fa2fa6")
    frame_top.place(relx=0, rely=0, relheight=0.01, relwidth=0.99)



    window.mainloop()

# to create password
username = "Admin"
password = "Abcd@123"
print("Login")
a = 3

for i in range(3):
    user_name_1 = input("User name = ")
    password_1 = input("Password = ")
    if username == user_name_1 and password == password_1:
        print("login successful")
        playsound('sound/login.mp3')
        Weather_forecast()
        break

    else:
        print("no of tries left:", a - i - 1)
        print("username or password do not match!!!")
        playsound('sound/error.mp3')
        if a - i != 0:
            print("Try again!")
        else:
            pass
else:
    print("Too many invalid try!\nclosing program")
    playsound('sound/exitd.mp3')
    exit(0)
