
import pyscreenshot 
  
# captura la pantalla
image = pyscreenshot.grab() 
  
# display de la captura
image.show() 
  
# para salvar el screenshot
image.save("nuevoscreenshot.png") 