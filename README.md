# Configuración Proyecto

## Configurar Visual Studio Code
### GIT
Ve a la terminal de tu PC y ejecuta
```
git --version
```
Si no te aparece, descárgalo aqui: https://git-scm.com/install/

### Visual Studio Code
Para configurar nuestra cuenta de git usaremos el siguiente comando usando la consola de VSCode<br>

**Ctrl + Ñ :**
```
git config --global user.name " TuNombre "
git config --global user.email " TuCorreoGitHub "
```


## Crear nuestro repositorio
Yendo a https://github.com/orgs/GS-FH-2025/repositories, pulsar el botón verde para crear un nuevo repositorio.  

Si miramos la siguiente foto, tan solo tendremos que cambiar la plantilla en el paso 2 para tener lo básico ya creado.

![https://imgur.com/gallery/t-TxzWO6K#G1ySDpE.png](https://i.imgur.com/bK7rdaQ.png)

## Acceder a nuestro repo desde Visual Studio Code
Por último, vamos a enlazar nuestro VSCode con GitHub.

En VSCode, pulsamos **Ctrl + Shift + P**, para abrir la barra superior y escribimos
```
git clone
```


Ponemos la url de nuestro repositorio el cual encontraremos aquí en el botón verde:


![](https://i.imgur.com/eK9JCTW.png)

Seleccionamos nuestra carpeta de destino y listo!!
