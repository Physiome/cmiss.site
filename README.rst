CMISS Plone site
================

This is a fairly standard Plone buildout.

To test, just do::

    $ python bootstrap.py
    $ bin/buildout

Start it off by::

    $ bin/zeoserver-testing start
    $ bin/instance-testing start

If you are trying to stage this, please use the appropriate buildout
configuration file::

    $ bin/buildout -c staging-instance.cfg
