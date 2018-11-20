.. python-tutorials documentation master file, created by
   sphinx-quickstart on Mon Nov 19 03:08:20 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-tutorials!
============================

**Persistent Python practice produces prodigious productivity.**

Introduction
------------

Python is a great language for getting things done quickly; however, a good deal of resources (mainly
:abbr:`RAM (Random Access Memory)`) are recommended. There are ways to incorporate C/C++ from within Python, but some
may find it easier to port it over.

For more thorough intros, get lost in `Python's Beginner's Guide <https://wiki.python.org/moin/BeginnersGuide>`_ or
`Wikipedia's Python page <https://en.wikipedia.org/wiki/Python_(programming_language)>`_ for a day or so and come back.

*Looks up, then puts down Steam Controller*

You're back? Alright, let's continue.

Getting Started
---------------

There are many ways to install and use Python depending on platform and :abbr:`IDE (Integrated Development Environment)`
(if any). These docs cover the methods I frequently use.

Windows
^^^^^^^

For Windows, I use but one editor: :doc:`getting_started/atom_setup`; however, I give
:doc:`getting_started/pycharm_setup` an honorable mention. The Atom setup is lightweight and portable while the Pycharm
setup is extensible and full-featured.

I have Pycharm on a Windows 10 Technical Preview :abbr:`VM (Virtual Machine)`, and it works well, but is quite bloated
for a Windows VM running in Windows (Windows-ception?).

Linux
^^^^^

For Linux, I have two main IDEs: :doc:`getting_started/vim_setup` and :doc:`getting_started/pycharm_setup`.
The Vim setup is lightweight and available without too much effort while the PyCharm setup is extensible and
full-featured.

While I have a couple of Linux boxes (at the moment), I am very security minded when it comes to my Linux machines, so
I prefer to run a Development VM of Linux on Windows. Excessive, yes, but taking snapshots, cloning, and
reinstalling on VMs is easier than on physical machines.

I've read that some python bots can be run on a Raspberry Pi. I would like to tinker with this concept a bit, but I am
concerned that Raspberry Pis do not have enough RAM, so I will be sticking with VMs until I can get more tests done.

Disclaimer
----------

Though covered by the MIT License, I reiterate: executable programs written from code on the Internet can end up doing
bad things.

  Read and understand all code you copy and paste before running it.

.. toctree::
   :maxdepth: 3
   :caption: Getting Started

   getting_started/atom_setup
   getting_started/vim_setup
   getting_started/pycharm_setup

.. toctree::
   :maxdepth: 3
   :caption: Books

   books/automate/automate.rst
   books/cracking/cracking.rst

.. toctree::
   :maxdepth: 3
   :caption: Online Courses

   udacity

.. toctree::
   :maxdepth: 2
   :caption: Module Reference:

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`