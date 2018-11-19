Atom
====

From the `Atom.io page <https://atom.io/>`_:

  Atom is a text editor that's modern, approachable, yet hackable to the core—a tool you can customize to do anything
  but also use productively without ever touching a config file.

Personally, I **have** had to edit a config file to setup a proxy, so :abbr:`YMMV (Your Mileage May Vary)`.

Atom is also surprisingly full-featured (e.g. plugins, themes, file system browsing) given that it can be installed in
a portable configuration and is multi-platform.

Windows Setup
-------------

While Atom is multi-platform, I only use it on Windows.

As aforementioned, I tend to use the `zipped Atom files <https://github.com/atom/atom/releases>`_ along with the
`PortableApps.com Platform <http://portableapps.com/download>`_ to create a portable base environment. Next, I extract
the zipped Atom files into ``X:\PortableApps\Atom\``, as an example.

Then, you'll need to get the `atom-runner package <https://atom.io/packages/atom-runner>`_ so that you can run the
Python programs with an ``ALT + R`` key combo. However, ``atom-runner`` will not work if you have to input data from
terminal, so you will need either the built-in Command Prompt or a PA.com portable enhancement like
`Console Portable <http://portableapps.com/apps/utilities/console_portable>`_. When you first open Atom, an ``.atom``
folder will be created in ``%USERPROFILE%``, this folder will need to be moved into ``X:\PortableApps\`` to keep your
settings.

As for Python, I get the `embeddable zip files <https://www.python.org/downloads/windows/>`_ and extract them into
``X:\PortableApps\CommonFiles\python3\`` to continue with the portable theme. If you want different versions of Python,
you can make different folders e.g. ``python2.7``, ``python3.6``, ``python3.5``

Finally, the easiest way to get Atom to find your portable Python installation is to use a shebang on the first line of
code ``#! X:\PortableApps\CommonFiles\python3\python.exe``
