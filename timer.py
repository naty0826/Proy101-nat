import time
  
# define la función de conteo countdown timer 
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('¡Se acabó el tiempo!')
  
  
# input time in seconds
seconds = input("Ingresa el tiempo en segundos: ")
  
# function call
countdown_timer(int(seconds))