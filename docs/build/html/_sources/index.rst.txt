.. henrri-connect documentation master file

henrri-connect
==============

Bibliothèque Python souveraine pour l'API de facturation `Henrri <https://henrri.io>`_.

Installation
------------

.. code-block:: bash

   pip install henrri-connect

Utilisation rapide
------------------

.. code-block:: python

   from henrri_connect import HenrriClient

   # Client synchrone
   client = HenrriClient("client_id", "client_secret")

   # Client asynchrone
   client = HenrriClient("client_id", "client_secret", async_mode=True)

.. toctree::
   :maxdepth: 2
   :caption: Sommaire

   api

