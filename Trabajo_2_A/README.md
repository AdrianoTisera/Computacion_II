<h1 align="center">🐍 Trabajo Práctico 2 - Ejercicio A</h1>

El programa inicia un servidor HTTP que convierte imágenes a escala de grises mediante solicitudes POST usando `http.server` y `PIL` en Python.

En caso de datos inválidos en una solicitud POST, el servidor responde con un código de error 400, señalando que el archivo no es una imagen.

## Ejecución
> Nota: Por conveniencia, se considera que la ubicación de `tp2.py` es el directorio actual.
1. Iniciar el servidor indicando IP y puerto, por ejemplo
```bash
python tp2.py -i localhost -p 8000
```

2. Una vez iniciado el servidor, se puede realizar una solicitud POST, utilizando Postman o curl. Dejé dos imágenes para probar el código y demostrar que admite cualquier formato:
```bash
curl -X POST -H "Content-Type: image/jpeg" --data-binary @ruta/a/la/imagen.xyz http://localhost:8000 > ruta/al/output.xyz
```
Los comandos utilizados para generar las imágenes de ejemplo son los siguientes respectivamente:
```bash
curl -X POST -H "Content-Type: image/jpeg" --data-binary @test.png http://localhost:8000 > output.png
```
```bash
curl -X POST -H "Content-Type: image/jpeg" --data-binary @test.png http://localhost:8000 > output.png
```
Por otra parte, si quisiera visualizarlo directamente en un visor de imágenes sin guardar el archivo, podría utilizar el siguiente comando:
```bash
curl -X POST -H "Content-Type: image/jpeg" --data-binary @test.png http://localhost:8000 | imv -
```
En este caso utilizo el visor `imv`, y el guión al final indica que debe leer desde la salida estándar. Debería funcionar con cualquier otro visor.
### Resultados
| Input   | Output    |
|--------------- | --------------- |
| ![](input.png)   | ![](output.png)   |
| ![](input.jpg)   | ![](output.jpg)   |

<p align="center">
<samp>
  <sup>
    <br>
    TISERA AGUILERA, Adriano Gabriel. | Legajo: 59059 | Ingeniería Informática
  </sup>
</samp>
</p>
