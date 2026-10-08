# multi threading = used to perform multiple tasks at the same time in a program
#                   good for I/O bound tasks, reading files, fetching data from API etc
#                   not good for CPU bound tasks, heavy calculations, image processing etc
#                   threading.Thread(target = my_function, args = (), kwargs = {})

'''cannot rename args and kwargs in this topic'''

import threading
import time

def walking_dog(name, duration):
    time.sleep(duration)
    print(f"{name} has been walked")

def throw_trash():
    time.sleep(3)
    print("Trash has been thrown")

def get_letter():
    time.sleep(5)
    print("You got your letters")

# if we call these three functions they will complete in 7+3+3 = 13 seconds and
# will go one by one, because they are running on the same thread, the main thread

# if we try multithreading, it will take a lot less time

'''walking dog has keyword argument, so pass a tuple with a comma, and also kwargs'''
kaam_1 = threading.Thread(target = walking_dog, args = ("Kukur",), kwargs = {"duration":7})
kaam_1.start()

kaam_2 = threading.Thread(target=throw_trash)
kaam_2.start()

kaam_3 = threading.Thread(target=get_letter)
kaam_3.start()
# now this method will take a total of 7 seconds here

kaam_3.join()
kaam_2.join()
kaam_1.join()

# by joining the tasks, now this line will run after the threads complete
# otherwise this line would have been completed first 
print("All tasks have been completed !") 