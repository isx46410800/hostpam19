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

## Hacemos el  modulo pam_mates.py
## Compilamos para hacer el pam_python.so
tar -xvzf pam-python-1.0.7.tar.gz
dnf install -y sphinx python3-sphinx python2-sphinx gcc
dnf -y install pam-devel
dnf -y install python-devel
cambiamos la linea 201 de /usr/include/features.h
make
```
[isx46410800@i05 hostpam19:aware]$ ll /tmp/mozilla_isx464108000/pam-python-1.0.7/src/pam_python.so
lrwxrwxrwx. 1 isx46410800 hisx2    40 Nov 28 11:47 /tmp/mozilla_isx464108000/pam-python-1.0.7/src/pam_python.so -> build/lib.linux-x86_64-2.7/pam_python.so
```
cp pam_python.so /usr/lib64/security/.

## Tornem a construir la imatge

## Comprobamos que nos haga la pregunta matematica para el chfn

### github: https://github.com/isx46410800/hostpam19/tree/master/hostpam19:aware
### dockerhub: https://hub.docker.com/repository/docker/isx46410800/hostpam19
