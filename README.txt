Imhotep
=======

This is a Python package for playing with the
`Pyramid <http://docs.pylonsproject.org/projects/pyramid/>`_ web framework.
Currently the goal of the project is to create an application that allows
one to register a user account, upload an image and be able to perform simple
manipulations like crop, scale and rotate.

The application is built as a simple package rather than based around buildout
to make it easier to deploy on one of the new Python cloud hosting solutions.

#. Install pyramid

  ::

    $: pip install pyramid

#. Generate package scaffold

  ::

    $: paster create -t pyramid_routesalchemy imhotep

#. Install package for development

  ::

    $: cd imhotep
    $: python setup.py develop
