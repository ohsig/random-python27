import webbrowser
import time

count = 0

print("The program has started at "+time.ctime())
while count < 3:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=LlU4FuIJT2k&start=31")
    count = count + 1
    
