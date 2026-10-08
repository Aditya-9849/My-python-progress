import time
import datetime #it helps working with date & time in string formats
import pygame #for sound effects

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    audio_file = "052.2_apple_alarm.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S") #capital is must
        print(current_time)
        if current_time == alarm_time:
            print("Wake up !!")
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():  #get_busy() returns a boolean
                time.sleep(1) #this makes sure that the program checks every 1 second for the music
#                               and hence keeping it playing until the music ends
            is_running = False
        
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Please enter your time for alarm(HH:MM:SS): ")
    set_alarm(alarm_time)