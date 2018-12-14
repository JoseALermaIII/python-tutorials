Installation
============

There are many ways to install and use Python depending on platform and :abbr:`IDE (Integrated Development Environment)`
(if any). These docs cover the methods I frequently use.

Windows
-------

For Windows, I use but one editor: :doc:`atom_setup`; however, I give
:doc:`pycharm_setup` an honorable mention. The Atom setup is lightweight and portable while the Pycharm
setup is extensible and full-featured.

I have Pycharm on a Windows 10 Technical Preview :abbr:`VM (Virtual Machine)`, and it works well, but is quite bloated
for a Windows VM running in Windows (Windows-ception?).

.. toctree::
    :maxdepth: 2

    atom_setup

Linux
-----

For Linux, I have two main IDEs: :doc:`vim_setup` and :doc:`pycharm_setup`.
The Vim setup is lightweight and available without too much effort while the PyCharm setup is extensible and
full-featured.

While I have a couple of Linux boxes (at the moment), I am very security minded when it comes to my Linux machines, so
I prefer to run a Development VM of Linux on Windows. Excessive, yes, but taking snapshots, cloning, and
reinstalling on VMs is easier than on physical machines.

I've read that some python bots can be run on a Raspberry Pi. I would like to tinker with this concept a bit, but I am
concerned that Raspberry Pis do not have enough RAM, so I will be sticking with VMs until I can get more tests done.

.. toctree::
    :maxdepth: 3
    :caption: Vim

    vim_setup

.. toctree::
    :maxdepth: 3
    :caption: PyCharm

    pycharm_setup

Building Documentation
----------------------

.. note::

    Building the documentation is **not needed or recommended** unless contributing to the documentation. The latest
    version of the documentation is available at `josealermaiii@github.io/python-tutorials
    <https://josealermaiii.github.io/python-tutorials/>`_ or as a `PDF in the source code
    <https://github.com/JoseALermaIII/python-tutorials/blob/master/manual.pdf>`_. You have been warned.

Building the docs requires a few more pip packages:

* sphinx
* sphinxcontrib-napoleon
* sphinx-rtd-theme

Now, we can build the docs in HTML format::

    cd absolute_path_here/python-tutorials/docs
    make html

This will save the docs website in ``../../python-tutorials-docs/``.

Building the PDF is even more involved. First, LaTeX must be installed on the OS. For example, in Ubuntu 18.04::

    sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-xetex

Installing these dependencies is not recommended, if not needed, because they require > 330 MB of disk space.

We also install XeLaTeX, ``texlive-xetex``, because some of the book corrections contain code snippets with unicode
characters that are not supported by the default LaTeX engine.

Now, we can build the docs in PDF format::

    cd absolute_path_here/python-tutorials/docs
    make latexpdf

This will save the doc's PDF in ``../manual.pdf``.

Disclaimer
----------

Though covered by the MIT License, I reiterate: executable programs written from code on the Internet can end up doing
bad things.

  Read and understand all code you copy and paste before running it.
