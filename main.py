def show_message(func):
    def wrapper():
        print("starting...")
        func()
        print("finished!")
    return wrapper
#Decorator
@show_message
def say_hello(): #تابع رو تعریف و دیکوریت کردم
    print("hello world")

say_hello() #این باید حتما نوشته بشه وگرنه خروجی نداریم