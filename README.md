# PyMCNPmanager

This python library aims to help developing and managing an MCNP simulation. When
installed you'll be able to execute the python script ```MCNPmanager -h```. The -h
parameter will *help* and guide you through the usage of the script.

### version 0.1.1
it is still a development version, but these commands work:

+ MCNPmanager init PATH #start a new MCNPmanager project
+ MCNPmanager cd PATH #copy an MCNPmanager project into an existing one
+ MCNPmanager build # build the MCNP input file

Requirements
------------

+ Python. Versions >= 3 are not supported

Installation
------------

Installing the latest stable repo is an easy task, just:

```
pip install git+https://github.com/ipostuma/PyMCNPmanager.git
```

While if you want to get the latest *development* **unstable** repo, just execute
the command above and ad this trailing string ```@dev``` .

######to uninstall:

```
pip uninstall PyMCNPmanager
```

Contacts
--------
e-mail: ian.postuma [аt] gmail.com

List of authors: Ian Postuma

License
-------
[I'm an inline-style link](https://github.com/ipostuma/PyMCNPmanager/blob/master/LICENSE)
