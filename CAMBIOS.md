# Gestión de Cambios

## Traer cambios
Antes de empezae a programar es importante tener actualizado nuestro espacio de trabajo.

En la consola, usaremos el comando:
```
git pull
```

## Guardar cambios
Para guardar los cambios ya realizados **sin subirlos** usamos el commando:
```
git add .
```
para marcar los cambios como 'staged'. Podemos añadirle comentarios mediante:
```
git commit -m 'Mensaje'
```

## Subir cambios a la nube
Para poder guardar correctamente en github, es imprescindible haber realizado los pasos anteriores y escribir el comando:
```
git push
```

## Cambio/Creación de rama de trabajo
Para evitar hacer cambios que rompan las funcionalidades ya implementadas, usaremos una copia de la rama 'main' para hacer pruebas. La crearemos con 

```
git branch nuevaRama
```

y accederemos a esta mediante:

```
git checkout nuevaRama
```

Importante recalcar que esta rama no existe en github, por lo que debemos de subir los cambios para que esta se cree:

```
git push --set-upstream origin nuevaRama
```

Una vez tengamos la funcionalidad completa, cambiaremos a la rama 'main' y trearemos los cambios, ya que esta es el principal que se mostrará:

```
git checkout main
git pull
git merge nuevaRama
```

Una vez hayamos copiado los nuevos cambios a la rama 'main', tendremos que subirlos para que se vea reflejado