import pyautogui as pg 
import time 
# this is the function who will run the auto messages sender
def meg_sender(meg,times,val):
    
    print("the message will reapet for {} between avery single message there is{}".format(times,val))
    print("Operation will start in 5 sec ..")

    pg.sleep(5)

#After 5 sec ..

    for _ in range(times):
        pg.write(meg)
        pg.press("Enter")
        pg.sleep(val)
        print(f"messege completed")
bool(exit)        
exit=0
while exit!=1 :
    message=input("Enter your message: ")
    many_times=input("How many times? (Enter number up of 1): ")
    interval=input("How secends do u want to sleep between every message: ")
    many_times=int(many_times)
    interval=float(interval)
    meg_sender(meg=message,times=many_times,val=interval)
    print("Have fan :)")
    exit=input("Type 0 to restart: ")
    
    
