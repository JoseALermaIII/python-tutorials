PyCharm
=======

`PyCharm <https://www.jetbrains.com/pycharm/>`_ is very much like Python itself: quick to develop on, full-featured,
and resource heavy. PyCharm is a true IDE: a console and debugger are all built-in. I especially like the PEP8 checks.

Linux Setup
-----------

Though Pycharm is multi-platform, I mainly use it on Linux.

Unless you are willing to pay for a license, you are probably going to want the `free community edition
<https://www.jetbrains.com/pycharm/download/#section=linux>`_. Download the ``tar.gz`` file wherever you like, then
extract the ``pycharm-community-20xx.x.x`` folder. Therein, run the ``pycharm-community-20xx.x.x/bin/pycharm.sh`` file
from within terminal.

Once setup is complete, on the menu bar, go to "Tools>Create Desktop Entry..." to make it easier to open later.
**Do not delete** the ``pycharm-community-20xx.x.x`` folder because that is where it is running from.

Upgrades follow the same procedure, except that you can delete the previous ``pycharm-community-20xx.x.x`` version
folder.

Python Binaries
---------------

Installing Python will depend on your Linux distro. Most will have some version of Python either built-in or available
from the package manager. PyCharm can auto-detect and use these installed versions. The `Ubuntu Setup
<http://josealermaiii.github.io/clashcallerbot-reddit/getting_started/ubuntu_setup.html>`_ of my ClashCallerBot is an
example of how easy setting up Python can be.

However, if you are unlucky, you will have to `download the source <https://www.python.org/downloads/source/>`_ and
compile it yourself.

Windows Setup
-------------

Windows installation is very straightforward:

* Install Python with the `Python executable installer <https://www.python.org/downloads/windows/>`_.
* Install PyCharm using the Community Edition `executable installer
  <https://www.jetbrains.com/pycharm/download/#section=windows>`_.

Any extra packages or modules would have to be added, but most programs can be run with the base installations.
