.. henrri-connect documentation master file

henrri-connect
==============

.. container:: hero-tagline

   Bibliothèque Python souveraine pour l'API de facturation `Henrri <https://henrri.io>`_.

.. grid:: 1 2 2 2
   :gutter: 2
   :padding: 0 0 3 0

   .. grid-item::

      .. button-link:: #installation
         :color: primary
         :shadow:
         :expand:

         Démarrer →

   .. grid-item::

      .. button-link:: api.html
         :color: secondary
         :outline:
         :expand:

         Référence API →

----

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: ⚡ Sync & Async
      :text-align: center

      Deux modes d'utilisation : synchrone et asynchrone, interchangeables à la volée.

   .. grid-item-card:: 🔒 Typage strict
      :text-align: center

      Modèles **Pydantic v2** avec annotations de types Python 3.11+.

   .. grid-item-card:: 📄 API complète
      :text-align: center

      Clients, factures, articles, unités, revenus, utilisateurs et plus.

   .. grid-item-card:: 🧪 Bien testé
      :text-align: center

      Suite de tests couvrant les modes synchrone et asynchrone.

   .. grid-item-card:: 📦 Léger
      :text-align: center

      Deux dépendances seulement : ``httpx`` et ``pydantic``.

   .. grid-item-card:: 🇫🇷 Souverain
      :text-align: center

      Conçu pour les entreprises françaises utilisant `Henrri <https://henrri.io>`_.

.. _installation:

Installation
------------

.. code-block:: bash

   pip install henrri-connect

Utilisation rapide
------------------

.. tab-set::

   .. tab-item:: Synchrone

      .. code-block:: python

         from henrri_connect import SyncHenrriClient

         client = SyncHenrriClient("client_id", "client_secret")

         # Lister les clients
         customers = client.customers.list()

         # Créer un document
         doc = client.documents.create(...)

   .. tab-item:: Asynchrone

      .. code-block:: python

         import asyncio
         from henrri_connect import AsyncHenrriClient

         async def main():
             client = AsyncHenrriClient("client_id", "client_secret")

             # Lister les clients
             customers = await client.customers.list()

         asyncio.run(main())

.. toctree::
   :maxdepth: 2
   :caption: Sommaire
   :hidden:

   api

