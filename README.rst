
django-tls
==========
Stores the current request in `Thread Local Storage`_ using `Werkzeug`_.

Installation::

    pip install django-tls

Configuration::

    # settings.py
    MIDDLEWARE_CLASSES = (
        'tls.TLSRequestMiddleware',
        ...
    )

Usage::
    
    from tls import request
    # do something dangerous and useful with current request object

Worried about security? then read this `thread`_.


.. _Thread Local Storage: http://en.wikipedia.org/wiki/Thread-local_storage
.. _Werkzeug: http://werkzeug.pocoo.org/
.. _thread: http://groups.google.com/group/django-users/browse_thread/thread/e7af359d7d183e04

