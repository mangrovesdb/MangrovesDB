Ethereum
==============================
Mangroves is fully adaptable to the Ethereum blockchain networks, and it can connect to all the projects on the Ethereum mainnet, layer 2 projects, and private Ethereum networks. 

Ethereum Mainnet
++++++++++++++++++
`Mainnet <https://ethereum.org/en/developers/docs/networks/>`_ is the primary public Ethereum production blockchain, where actual-value transactions occur on the distributed ledger.

.. Note:: 

    You can use this `tutorial <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of **mangroves-cli** services on ``Ethereum mainnet``.
    You can also use this `tutorial <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of **mangroves SQLite compatible API** on ``Ethereum mainnet``.





Ethereum Layer 2
++++++++++++++++++
`Layer 2 projects <https://ethereum.org/en/layer-2/#:~:text=Layer%202%20projects%20will%20post,secure%20and%20validate%20the%20network>`_ will post their transaction data onto Ethereum, relying on Ethereum for data availability. These platforms are decentralized Ethereum scaling solutions.
Mangroves support all the projects on the Ethereum network, including all layer 2 projects. For mangroves, it is as easy as just replacing the ``--url`` with reliable RPC gateways to make a connection with these platforms.

.. Note:: 

    The URL can be any available Ethereum gateway. Mangroves can handle all nodes in different network layers. You can also try your custom full node.
   
   .. tabs::

      .. group-tab:: Polygon

         .. code-block:: bash

            ./mangroves-cli --url https://polygon-rpc.com


      .. group-tab:: Fantom

         .. code-block:: bash

            ./mangroves-cli --url https://rpc.ftm.tools

      .. group-tab:: arbitrum

         .. code-block:: bash

            ./mangroves-cli --url https://arb1.arbitrum.io/rpc


.. Note:: 

    You can use this `tutorial <https://killercoda.com/mangroves/scenario/cli-polygon>`_ to test the free version of mangroves services on ``Polygon`` platform, and `tutorial <https://killercoda.com/mangroves/scenario/cli-arbitrum>`_  to test the free version of mangroves services on ``Arbitrum`` platform.
    Feel free to replace the ``--url`` to make a connection with other projects.
    You can also use this `tutorial <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the accessible version of **mangroves SQLite compatible API** on ``Polygon`` and ``Arbitrum``.