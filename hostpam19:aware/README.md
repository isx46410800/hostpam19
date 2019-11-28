# Examen practico M06-ASO PAM - Miguel Amoros

## Creamos un Dockerfile con lo basico para su construccion
## Creamos un install con los dos usuarios que nos piden: anna y miguel
## Creamos un startup para ejecutar el install y los demonios
## Construimos la imagen con docker build y docker run
+ docker build -t isx46410800/hostpam19:aware .
+ docker run --rm --name pam -h pam --privileged -it isx46410800/hostpam19:aware /bin/bash

## Al crearlo estaremos en el WORDIR de /opt/docker indicado en el Dockerfile
## Abriremos otra sesion para hacer las pruebas pertinentes, siempre una como root abierta
+ docker exec -it pam /bin/bash

## Comprobamos que podemos utilizar los usuarios creados y hacer el chfn
## Creamos el programa python pamaware.py para validar un usuari unix
Se utiliza:  
```
[root@pam docker]# python3 pamaware.py 
Usuari: anna
Passwd: anna
0 Success
Usuari UNIX valid
[root@pam docker]# python3 pamaware.py 
Usuari: kaka
Passwd: kaka
```

## Implementamos el modulo pam_mates.py

## Comprobamos que nos haga la pregunta matematica para el chfn

### github: https://github.com/isx46410800/hostpam19/tree/master/hostpam19:aware
### dockerhub: https://hub.docker.com/repository/docker/isx46410800/hostpam19
