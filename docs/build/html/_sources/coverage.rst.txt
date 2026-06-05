Coverage des tests
==================

Rapport de couverture
---------------------

`Voir le rapport de couverture <_static/coverage/index.html>`_

Résumé des test
---------------

.. literalinclude:: _static/coverage.txt
   :language: text

Commandes utilisées
-------------------

Pour reproduire le rapport de coverage, vous pouvez utiliser le code suivant.

.. code-block:: bash

    coverage run -m pytest
    coverage html
    coverage report -m
