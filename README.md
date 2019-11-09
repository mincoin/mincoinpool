Requirements:
-------------------------
Generic:
* Mincoin >=0.14.3
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6
* cd litecoin_scrypt
* sudo python setup.py install

Windows:
* Install [Python 2.7](http://www.python.org/getit/)
* Install [MinGW](http://www.mingw.org/wiki/Getting_Started)
* Install [Twisted](http://twistedmatrix.com/trac/wiki/Downloads)
* Install [Zope.Interface](http://pypi.python.org/pypi/zope.interface/3.8.0)
* Install [python win32 api](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/)
* Install [python win32 api wmi wrapper](https://pypi.python.org/pypi/WMI/#downloads)
* Unzip the files into C:\Python27\Lib\site-packages
* cd litecoin_scrypt
* C:\Python27\python.exe setup.py build --compile=mingw32 install

If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running MincoinPool:
-------------------------
To use MincoinPool, you must be running your own local mincoind. For standard
configurations, using MincoinPool should be as simple as:

    python run_mincoinpool.py

Then run your miner program, connecting to 127.0.0.1 on port 10335 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 10334 to the host running MincoinPool.

Run for additional options.

    python run_mincoinpool.py --help

License:
-------------------------

[Available here](COPYING)


