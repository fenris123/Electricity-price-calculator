# Electricity-price-calculator
With this python program (in progres) you can calculate the cost of the electricity for the company that sells it tou you (Only for Spain).

Rest of the description is in spanish.


DESCRIPCION GENERAL:

Con este script EN DESARROLLO, pretendemos desarrollar un sistema que calcule el precio total de la energia para las comercializadoras entre una fecha determinada y otra.

Asi, podra compararse con la factura mensual que se recibe y calcular el beneficio que mete cada empresa.

AVISO:  Solo se introduciran los principales costes.  Componentes con una participacion muy pequeña o muy puntual no seran añadidos.




DATOS a analizar y su indicador (inclusion en el script, en progreso)


10211  Precio medio horario final suma de componentes
811    Precio medio horario componente banda secundaria
812    Precio medio horario componente desvíos medidos
10403  Precio medio horario componente mecanismo de ajuste RD-L 10/2022   (NOTA PARA MI:  Introducir solo entre junio del 22 y enero del 23, ambos incluidos.)
805    Precio medio horario componente mercado diario  (Equivalente a mercado spot, indicador 600. Identicos valores, solo cambia la nomenclatura)) 
806    Precio medio horario componente restricciones PBF
807    Precio medio horario componente restricciones tiempo real
813    Precio medio horario componente saldo de desvíos


El resto de los indicadores puede encontrarse aqui:

https://www.esios.ree.es/es/analisis/10211?compare_indicators=805%2C806%2C807%2C808%2C809%2C810%2C811%2C812%2C813%2C814%2C815%2C816%2C1277%2C10403%2C1286%2C1368&start_date=24-03-2025T00%3A00&geoids=&vis=1&end_date=24-03-2025T23%3A55&compare_start_date=23-03-2025T00%3A00&groupby=hour



ESTADO DE DESARROLLO:

Actualmente el script obtiene los datos por hora del precio del mercado y los guarda en un archivo JSON.
Debemos incluir en la peticion los demas datos, integrarlos y posteriormente realizar las operaciones necesarias con ellos.
