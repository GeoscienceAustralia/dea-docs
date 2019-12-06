.. Digital Earth Australia documentation master file, created by
   sphinx-quickstart on Wed Jun  7 17:22:24 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/dea-logo-inline.svg
   :align: center
   :alt: Digital Earth Australia Logo

|
|

Digital Earth Australia User Guide
##################################

Digital Earth Australia is an analysis platform for satellite imagery and other Earth observations.

For more information on the project, see http://www.ga.gov.au/dea

Digital Earth Australia is currently in beta for users with
accounts on the National Computational Infrastructure (NCI) or the Digital Earth Australia Sandbox (see the :ref:`Setup introduction <setup>` page).

Data can be viewed on `NationalMap <https://nationalmap.gov.au/>`_,
or accessed directly from `Amazon S3 Storage <https://data.dea.ga.gov.au>`_.

Our OGC Web Service supporting WMS, WCS and some WPS functionality is `<https://ows.services.dea.ga.gov.au/>`_.

If you notice an error in this documentation, things that could be explained more clearly, or things that are missing,
please let us know by creating an Issue in the
`dea-notebooks Github repository <https://github.com/GeoscienceAustralia/dea-notebooks/issues>`_,
and list what you would like to see changed.

.. toctree::
   :maxdepth: 1
   :caption: Overview

   about/intro.rst
   about/glossary.rst
   about/changelog.rst

.. toctree::
   :maxdepth: 1
   :caption: Setup

   setup/README.rst
   setup/sandbox.rst
   setup/NCI/README.rst
   setup/jupyter.rst


.. toctree::
   :caption: User Guide
   :maxdepth: 1
   :glob:

   notebooks/Beginners_guide/README.rst
   notebooks/DEA_datasets/README.rst
   notebooks/Frequently_used_code/README.rst
   notebooks/Real_world_examples/README.rst

.. toctree::
  :caption: Index

  genindex
