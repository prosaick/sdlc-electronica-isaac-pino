#

""""
Se quedará vacio este archivo, pero podemos agregar algunas librerias despues para que sean llamadas en los demas archivos desde este
por ejemplo: from init.py import pin, ADC, version, Open, etc .
es decir, si queremos usar una libreria en varios archivos, podemos importarla en este archivo y luego llamarla desde los demas archivos  
y el script donde sea llamado este archivo solo usará los metodos que se encuentren en este archivo, es decir, no se podra llamar a 
metodos de otras librerias que no esten en este archivo, solo se podran llamar los metodos que esten en este archivo y que sean 
importados desde otros archivos y solo usará los necesarios y declarados sin mostrar errores de compilasción o sintaxis.
 
"""