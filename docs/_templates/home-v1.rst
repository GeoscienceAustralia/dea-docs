.. rst-class:: home-page

======================================================================================================================================================
{{ data.title }}
======================================================================================================================================================

{{ data.description }}

.. container:: card-list icons
   :name: data-products

   .. rubric:: Data Products

   Browse our catalogue of data products to find supporting information and ways to access the data.

   .. grid:: 2 2 3 5
      :gutter: 3

      {% for item in data.product_themes %}
      .. grid-item-card:: :fas:`{{ item.icon }}`
         :link: {{ item.link }}

         {{ item.name }}
      {% endfor %}

.. container:: showcase-panel bg-gradient-primary
   :name: user-guides

   .. container::

      .. rubric:: User Guides

      Find documentation, step-by-step instructions, and DEA publications on a variety of topics.

      `Visit the User Guides </guides/>`_

   .. container::

      .. image:: /_files/pages/dea-hero.jpg

.. container:: showcase-panel bg-gradient-forest reverse
   :name: dea-notebooks

   .. container::

      .. rubric:: DEA Notebooks

      Explore visual walkthroughs that show how to analyse our data using Python, including the use our DEA Tools package.

      `Visit the DEA Notebooks </notebooks/README/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg

.. container:: showcase-panel bg-gradient-stone
   :name: changelog

   .. container::

      .. rubric:: DEA Tech Alerts and Changelog

      Find out about the latest updates to DEA's products and services, planned maintenance, and any outages that may occur.

      `Visit the DEA Tech Alerts and Changelog </tech-alerts-changelog/>`_

   .. container::

      .. image:: /_files/reference/Reporting_dashboard.png

.. container:: showcase-panel bg-gradient-space reverse
   :name: dea-notebooks

   .. container::

      .. rubric:: Validation reports

      Assess the validity of our datasets against these validation reports.

      `Visit the Validation reports </validation/>`_

   .. container::

      .. image:: /_files/cmi/Kakadu-Mary_TCW-percentiles-wide_1.jpg

.. container:: showcase-panel
   :name: about-dea

   .. container::

      .. rubric:: About Digital Earth Australia

      `Digital Earth Australia <https://www.dea.ga.gov.au/>`_ (DEA) is a program of `Geoscience Australia <https://www.ga.gov.au/>`_, an entity of the Australian Government.

      It is our mission is to embed satellite imagery and data into decisions that support a sustainable Australian environment, a resilient society, and a strong economy.

      `Visit the DEA website <https://www.dea.ga.gov.au/>`_

      `Follow our newsletter <https://www.dea.ga.gov.au/news/dea-newsletter-and-communications-archive>`_

   .. container::

      .. image:: /_files/themes/sea-ocean-and-coast.* 
