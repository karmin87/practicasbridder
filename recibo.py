
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
  
# lista de datos
DATA = [ 
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
    [ 
        "16/11/2020", 
        "Full Stack Development with React & Node JS - Live", 
        "Lifetime", 
        "10,999.00/-", 
    ], 
    [ "16/11/2020", "Classes: Live Session", "6 months", "9,999.00/-"], 
    [ "Sub Total", "", "", "20,9998.00/-"], 
    [ "Discount", "", "", "-3,000.00/-"], 
    [ "Total", "", "", "17,998.00/-"], 
] 
  
# creando un documento base para la factura tamaño a4
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 
  
# report lab lo define con el metodo standard
styles = getSampleStyleSheet() 
  
# fetching the style of Top level heading (Heading1) 
title_style = styles[ "Heading1" ] 
  
# alineamiento
title_style.alignment = 1
  
  
# el titulo 
title = Paragraph( "Christian" , title_style ) 
  
# crea tablas con el objeto y el estilo
# define el estilo por lineas
# las tuplas como coordenadas
# columnas y filas
style = TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
) 
  
# crea el objeto tabla y le pasa el estado estilo
table = Table( DATA , style = style ) 
  

# el pdf final
pdf.build([ title , table ]) 