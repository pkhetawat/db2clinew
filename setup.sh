#!/usr/bin/sh

echo "Installing Required python, node and go module..";
yum install -y gcc python python-devel git go wget pam tar xz php php-devel make gcc-c++ php-pear python3 python3-devel 
cd /root 
wget -c https://bootstrap.pypa.io/get-pip.py
python get-pip.py 
pip3 install ibm_db_sa
#pip install ibm_db 
pip3 install ibm_db 
pip3 install --upgrade pip
wget -c https://nodejs.org/dist/v16.6.1/node-v16.6.1-linux-x64.tar.xz
unxz node-v16.6.1-linux-x64.tar.xz 
tar -xf node-v16.6.1-linux-x64.tar 
mv node-v16.6.1-linux-x64 /root/nodejs 
cd /root 
go get -d github.com/ibmdb/go_ibm_db 
cd /root/go/src/github.com/ibmdb/go_ibm_db/installer 
go run setup.go
