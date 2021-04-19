.. highlight:: console

.. data_and_metadata:

Amazon Web Services
===================

Digital Earth Australia store a range of data products on Amazon Web Service's
S3 with free public access. In addition to data, there are a number of services
including an interactive code environment using Jupyter, a metadata explorer
and web services available. This page provides basic technical documentation for
the DEA data and services on AWS.

Data and Services Listing
-----------------------------

* The public S3 bucket can be explored using the interactive web application
  available at https://data.dea.ga.gov.au/.

* The extent and complete scene listing of each data product is available via explorer
  at https://explorer.sandbox.dea.ga.gov.au/.

* Explorer has a STAC endpoint, for listing or searching metadata records
  and is available at https://explorer.sandbox.dea.ga.gov.au/stac/.

* Open Web Services are available at https://ows.dea.ga.gov.au/ and provide
  access to visualisations and data exports via WMS, WMTS and WCS.

* The Sandbox is accessible at https://app.sandbox.dea.ga.gov.au/ (see sandbox_).


S3 Details
----------

DEA's public data bucket is named ``dea-public-data`` and the ARN for it is
``arn:aws:s3:::dea-public-data``. There is an inventory bucket available named
``dea-public-data-inventory`` with the ARN
``arn:aws:s3:::dea-public-data-inventory``.

.. note:

    If you use the public data bucket browser website_, you can replace the URL
    components with direct S3 HTTP references in the form
    ``https://dea-public-data.s3-ap-southeast-2.amazonaws.com/<path>``, so for example,
    a link like
    ``https://data.dea.ga.gov.au/baseline/ga_ls8c_ard_3/091/076/2019/07/31/ga_ls8c_nbart_3-1-0_091076_2019-07-31_final_thumbnail.jpg``
    could be changed to an S3 direct link like
    ``https://dea-public-data.s3-ap-southeast-2.amazonaws.com/baseline/ga_ls8c_ard_3/091/076/2019/07/31/ga_ls8c_nbart_3-1-0_091076_2019-07-31_final_thumbnail.jpg``.
    The S3 data is in AWS region ap-southeast-2
  
    Programmatic access requires the environment variable AWS_NO_SIGN_REQUEST=Yes
    

Key products that are available on S3 include the following:

* `DEA Surface Reflectance (Landsat 5 TM)`_: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls5t_ard_3/
* `DEA Surface Reflectance (Landsat 7 ETM+)`_: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls7e_ard_3/
* `DEA Surface Reflectance (Landsat 8 OLI-TIRS)`_: https://data.dea.ga.gov.au/?prefix=baseline/ga_ls8c_ard_3/
* DEA Water Observations: https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_wo_3/
* DEA Fractional Cover: https://data.dea.ga.gov.au/?prefix=derivative/ga_ls_fc_3/
* DEA Coastlines: https://data.dea.ga.gov.au/?prefix=derivative/dea_coastlines/


Notifications
-------------

We provide a number of notifications for newly produced data that lands on AWS.

* DEA New Data: ``arn:aws:sns:ap-southeast-2:538673716275:DEANewData`` - this is a bucket notifications
  that is triggered by every object that lands in the ``dea-public-data`` bucket.
* dea-public-data-landsat-3: ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3`` - this
  is a notification that is triggered for each new DEA Surface Reflectance scene
* dea-public-data-landsat-3-fc: ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3-fc`` - this
  is a notification for each DEA Fractional Cover scene produced
* dea-public-data-landsat-3-wo: ``arn:aws:sns:ap-southeast-2:538673716275:dea-public-data-landsat-3-wo`` - this
  is a notification for each DEA Water Observations scene produced

All the the scene level notifications include a STAC 1.0.0-beta.2 JSON document
and have message attributes including the following:
  
* ``action``: added or archived, whether the scene was created or deleted
* ``product``: the Open Data Cube product name for the scene
* ``datetime``: the datetime stamp for the scene, this is the capture time of the scene
* ``maturity``: the maturity level of the dataset, either "nrt", "interim" or "final"
* ``bbox.ll_lon``, ``bbox.ll_lat``, ``bbox.ur_lon``, ``bbox.ur_lat``: the lower left
  or upper right longitude or latitude of the scene

For Surface Reflectance products, the following additional attributes are included:

* ``cloud_cover``: percentage cloud cover, a number between 0 and 100
* ``gqa_iterative_mean_xy``: a measure of the scenes geometric accuracy in pixels


.. _`DEA Surface Reflectance (Landsat 5 TM)`: https://cmi.ga.gov.au/data-products/dea/358/dea-surface-reflectance-landsat-5-tm
.. _`DEA Surface Reflectance (Landsat 7 ETM+)`: https://cmi.ga.gov.au/data-products/dea/475/dea-surface-reflectance-landsat-7-etm
.. _`DEA Surface Reflectance (Landsat 8 OLI-TIRS)`: https://cmi.ga.gov.au/data-products/dea/365/dea-surface-reflectance-landsat-8-oli-tirs
.. _website: https://data.dea.ga.gov.au
