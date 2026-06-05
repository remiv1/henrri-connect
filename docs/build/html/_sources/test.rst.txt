Tests
=====

Résultats des tests
-------------------

Le rapport HTML complet est disponible ici :

`Voir le rapport de tests <_static/tests/report.html>`_

Résumé des tests
----------------

.. literalinclude:: _static/tests/pytest.txt
   :language: text

Commandes utilisées
-------------------

Pour reproduire le rapport de coverage, vous pouvez utiliser le code suivant.

.. code-block:: bash

    pytest | sed '/^rootdir:/d;/^asyncio:/d'
    pytest --html=report.html --self-contained-html
