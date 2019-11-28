#! /bin/bash
useradd anna
useradd miguel
echo "anna" | passwd --stdin anna
echo "miguel" | passwd --stdin miguel
cp /opt/docker/login.defs /etc/login.defs
cp /opt/docker/nslcd.conf /etc/nslcd.conf
cp /opt/docker/nslcd.conf /etc/nscd.conf
cp /opt/docker/nsswitch.conf /etc/nsswitch.conf
cp /opt/docker/pam_python.so /usr/lib64/security/.
