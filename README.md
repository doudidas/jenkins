# Setup File

1) Install
2) Configure

## Install

### Install java SDK

- get Java rpm online (Ex: jdk-11.0.3_linux-x64_bin.rpm)
  - Be carefull java 12 is not yet supported !
- transfert rmp into offline host
- run `rpm -ivh jdk-11.0.3_linux-x64_bin.rpm`
- check that java is installed and well configured with those cmd:
  - `java -v`
  - `echo $JAVA_HOME`

- Cleanup rpm file `rm -ivh jdk-11.0.3_linux-x64_bin.rpm`

### Install Jenkins

- get Jenkins rpm online (Ex: jenkins-2.184-1.1.noarch.rpm)
- transfert rmp into offline host
- run `rpm -ivh jenkins-2.184-1.1.noarch.rpm`
- check that the file exist `/usr/lib/jenkins/jenkins.war`
- Cleanup rpm file

### Setup Service

- Create a new file at the path `/etc/systemd/system/jenkins.service`. Then add the following lines to the new jenkins.service file:

``` txt
[Unit]
Description=Jenkins Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/java -jar /usr/local/bin/jenkins.war
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

### Install PIP

- Download source code from [pip website](https://pypi.org/project/pip/#files) or directely from [link ](https://files.pythonhosted.org/packages/93/ab/f86b61bef7ab14909bd7ec3cd2178feb0a1c86d451bc9bccd5a1aedcde5f/pip-19.1.1.tar.gz)
- transfert it directly into your offline server

Install process:

``` bash
tar -xf pip-19.1.1.tar.gz
cd pip-19.1.1
python setup.py install
pip --version
```
