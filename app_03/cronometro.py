import time 
  
# define la funcion para contar
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  
# para que el usuario ponga el tiempo en segundos
t = input("Enter the time in seconds: ") 
  
# llamando a la funcion
countdown(int(t)) 