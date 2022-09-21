.. _settingup:

Installation
===============

Using this guidance you can simply install mangroves CLI and mangroves compatible version with sqlite SDK on your system. You can then use the quick start tutorial to test the mangroves immediately.

* :ref:`Prerequisites <Prerequisites>`
* :ref:`Installation <Installation>`
* :ref:`Quickstart Tutorial <QuTut>`


.. _Prerequisites:

Prerequisites
-----------------
There are not that many requirements before installing MGDB. Just be sure you have an internet connection. 

- Internet connection
- OS of your choice. We are supporting all stacks.


.. _Installation: 

Installation
-----------------
Please follow the below guideline to install mangroves.

.. tabs::

   .. tab:: Linux

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: Binary download

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on x86-64 Linux** using binary download.
                        You can use this `link <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of the mangroves-cli.

                        .. code-block:: bash

                            echo "Will be publiched soon"

                     .. tab:: sqlite SDK

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on x86-64 Linux** for SQLite compatible sdk.
                        You can use this `link <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of SQLite compatible sdk on python.

                        .. code-block:: bash

                            echo "Will be publiched soon"

             .. tab:: ARM64

                 .. tabs::

                     .. tab:: Binary download

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on ARM64 Linux** using binary download.
                        You can use this `link <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of the mangroves-cli.

                        .. code-block:: bash

                            echo "Will be publiched soon"


                     .. tab:: sqlite SDK

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on ARM64 Linux** for SQLite compatible sdk.
                        You can use this `link <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of SQLite compatible sdk on python.

                        .. code-block:: bash

                            echo "Will be publiched soon"

   .. tab:: macOS

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: Binary download

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on x86-64 macOS** using binary download.
                        You can use this `link <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of the mangroves-cli.

                        .. code-block:: bash

                            echo "Will be publiched soon"

                     .. tab:: sqlite SDK

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on x86-64 macOS** for SQLite compatible sdk.
                        You can use this `link <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of SQLite compatible sdk on python.

                        .. code-block:: bash

                            echo "Will be publiched soon"
 
             .. tab:: ARM64

                 .. tabs::

                     .. tab:: Binary download

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on ARM64 macOS** using binary download.
                        You can use this `link <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of the mangroves-cli.

                        .. code-block:: bash

                            echo "Will be publiched soon"


                     .. tab:: sqlite SDK

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on ARM64 macOS** for SQLite compatible sdk.
                        You can use this `link <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of SQLite compatible sdk on python.


                        .. code-block:: bash

                            echo "Will be publiched soon"

   .. tab:: Windows

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: .exe download

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on WindowsS**. You shall download and run the installer for the latest release, or if using PowerShell, use terminal command.
                        You can use this `link <https://killercoda.com/mangroves/scenario/cli>`_ to test the free version of the mangroves-cli.

                        .. code-block:: bash

                            echo "Will be publiched soon"

                     .. tab:: sqlite SDK

                        We will open-source the project shortly and release the guideline for installing the **latest mangroves stable release on WindowsS**. You shall download and run the installer for the latest release, or if using PowerShell, use terminal command.
                        You can use this `link <https://killercoda.com/mangroves/scenario/sqlite>`_ to test the free version of SQLite compatible sdk on python.

                        .. code-block:: bash

                            echo "Will be publiched soon"



.. _QuTut:

Quickstart Tutorial
----------------------

You can easily use mangroves CLI to query data on the public blockchain, e.g., Ethereum. You can also test the mangroves SQLite compatible API in any programming language and platform. In what follows, there are some examples of how to test each of these services:

MangrovesDB CLI
+++++++++++++++++

- **1. Running mangroves CLI** 

After installation, in your terminal, run:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: bash

          ./mangroves-cli --url https://cloudflare-eth.com/


   .. group-tab:: Mac OSX

      .. code-block:: bash

          ./mangroves-cli --url https://cloudflare-eth.com/

   .. group-tab:: Windows

      .. code-block:: bash

          ./mangroves-cli --url https://cloudflare-eth.com/


.. Note:: 

    If installation is not available at this moment, you can use this `tutorial <https://killercoda.com/mangroves/>`_ to test the free version of mangroves services.

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

- **2. Querying the Blockchain** 

You can now run your queries in the mangroves CLI. Please see the following examples:

   - Query the :ref:`Blocks Table <blocks>`:

      .. code-block:: SQL

            select number, hash, parent_hash from blocks where number=15368213;


   - You can expect a result like this:

   .. image:: /images/sampQueBlocks1.png
     :width: 600


Verify the results in underlying blockchain networks and available blockchain explorer platforms. For the abovve query you can chack this `page <https://etherscan.io/block/15368213>`_.

.. Note:: 

    You can run other queries and extract other data related to :ref:`Block Table <blocks>`, :ref:`Transactions Table <transactions>`, :ref:`Contracts Table <contracts>`, :ref:`Logs Table <logs>`, :ref:`Token Transfers Table <token_transfers>`, :ref:`Tokens Table <tokens>`. Here are some samples: 
         
    .. code-block:: SQL

       select number, hash, nonce, gas_limit, min_gas_price, gas_used from blocks where number<20 order by number desc limit 5;



.. admonition:: Caution

    Do not forget to add **;** at the end of your query. This will enable the Mangroves CLI that your query statement is finished.

.. Attention::

    Find what you can query from the :ref:`Blocks Table <blocksRef>`.


.. DANGER::

    If you are using public Ethereum gateways, please do not use the mangroves CLI to extract huge portion of data from blockchain |:stop_sign:|. Such queries will last too long or failed. You can try mangroves sqlite sdk comaptible.


You can also run query against other tables on underlying blockchain network. For Ethereum mainnet, let's try another query on Transactions table on Polygon using its RPC gateway:

   - Query the :ref:`Transactions Table <transactions>`:

      .. code-block:: SQL

            select transaction_index, from_address, to_address, value, gas from transactions where block_number=33243462 order by value desc limit 5;


   - You can expect a result like this:

   .. image:: /images/polygon_trnsaction.png
     :width: 600




MangrovesDB sqlite library
++++++++++++++++++++++++++++

**Mangroves SQLite compatible API** is our powerful tool that can be used to write queries in any programming language of your choice on any platform. You can see some examples of how mangroves in integrated with SQLite SDK to perform queries.

.. tabs::

   .. code-tab:: py

         import sqlite3
         import pandas as pd

         from sqlite3 import Error
         try:
             url = 'https://cloudflare-eth.com/'
             con = sqlite3.connect(url)

             print(f"Connection is established: Mangroves connected to {url}")

             df = pd.read_sql_query("select * from blocks where number<20;", con)

             df.to_csv("blocks.csv")

         except Error:
            print(Error)


   .. code-tab:: js

         var sqlite3 = require('sqlite3');
         var db;

         function runQueries(db) {
         db.all("select count(hash) from transactions where block_hash='f8b492a7b7eb9396d95c6b9b2f81d19a3661b562460a91c854fd0cbe195e0210';", function(err, rows) {
             rows.forEach(row => {
             console.log(row);
             });
         });
         }

         db = new sqlite3.Database('https://cloudflare-eth.com/', (err) => {
             if (err && err.code == "SQLITE_CANTOPEN") {
             console.log("Getting error " + err);
             exit(1);
             }
             runQueries(db);
         });



   .. code-tab:: c

         #include <stdio.h>
         #include <sqlite3.h>

         int main() {
             sqlite3 *db;
             sqlite3_stmt *stmt;	
            
             sqlite3_open("https://cloudflare-eth.com/", &db);

             if (db == NULL) {
                 printf("Failed to open DB\n");
                 return 1;
             }

             printf("Performing query...\n");
             sqlite3_prepare_v2(db, "select number, hash, parent_hash from blocks where number<10", -1, &stmt, NULL);
                      
             printf("Got results:\n");
             while (sqlite3_step(stmt) != SQLITE_DONE) {
                 int i;
                 int num_cols = sqlite3_column_count(stmt);
                 printf("row> ");
                 for (i = 0; i < num_cols; i++)
                 {
                     switch (sqlite3_column_type(stmt, i))
                     {
                     case (SQLITE3_TEXT):
                         printf("%s, ", sqlite3_column_text(stmt, i));
                         break;
                     case (SQLITE_INTEGER):
                         printf("%d, ", sqlite3_column_int(stmt, i));
                         break;
                     case (SQLITE_FLOAT):
                         printf("%g, ", sqlite3_column_double(stmt, i));
                         break;
                     default:
                         break;
                     }
                 }
                 printf("\n");

             }

             sqlite3_finalize(stmt);

             sqlite3_close(db);
                
             return 0;
         }


.. Attention::

    As can be seen the real-time data can be extracted easily using any programming language. This SQLite compatible interface can be integrated with any 3rd party dashboard/analytical services. 