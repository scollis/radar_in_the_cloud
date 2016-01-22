How to set up Py-ART on an EC2 instance
---------------------------------------

Setting up the instance

Setting up your instance using apt-get

sudo apt-get update

sudo apt-get -y install git

sudo apt-get -y install build-essential 

sudo apt-get install -y python-qt4

install Anaconda
----------------

cd

mkdir src

cd src

Go to https://www.continuum.io/downloads

left click and copy location of linux 64 bit

wget -ctrl v- 
chmod +x Anaconda2-2.4.1-Linux-x86_64.sh 
./Anaconda2-2.4.1-Linux-x86_64.sh 

follow prompts, choose Yes when prompted to add to .bashrc

install dependancies
--------------------

*You must loug out and log in again so .bashrc is run*

conda update conda

conda install basemap netCDF4

install Py-ART
--------------
cd

cd src

git clone https://github.com/ARM-DOE/pyart

cd pyart 

python setup.py install 

Install Boto
------------
cd

cd src

git clone https://github.com/boto/boto

cd boto

python setup.py install

*Configuring Boto*


Install StarCluster
-------------------
cd

cd src

git clone https://github.com/jtriley/StarCluster

cd boto

python setup.py install


Connect to the NEXRAD S3 bucket
-------------------------------


