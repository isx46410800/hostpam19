#! /bin/bash
bash /opt/docker/install.sh
/sbin/nscd
/sbin/nslcd
/usr/sbin/rpcbind && echo "rpcbind Ok"
/usr/sbin/rpc.statd && echo "rpc.stad Ok"
