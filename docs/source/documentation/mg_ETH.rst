.. _mgeth:

Ethereum Tables
======================
There are Seven main Table tables for the Ethereum-based blockchain networks. You can find the column names and data types using this reference. 
These pre-defined tables are:

* :ref:`Block Table <blocks>`
* :ref:`Transactions Table <transactions>`
* :ref:`Contracts Table <contracts>`
* :ref:`Logs Table <logs>`
* :ref:`Token Transfers Table <token_transfers>`
* :ref:`Tokens Table <tokens>`
* :ref:`Traces Table <traces>`


.. _blocksRef:

.. _blocks:

Blocks Table
-----------------

The data related to the blocks of the Ethereum public network will be saved here. This base table can be used for any further design of a customized Ethereum-based
platform.

+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|      timestamp         | Timestamp  |
+------------------------+------------+
|        number          |    Int     | 
+------------------------+------------+
|        hash            |    text    |
+------------------------+------------+
|      parent_hash       |    text    | 
+------------------------+------------+
|       mix_hash         |    text    |
+------------------------+------------+
|      sha3_uncles       |    text    |
+------------------------+------------+
|        nonce           |    Int     | 
+------------------------+------------+
|      logs_bloom        |    text    |
+------------------------+------------+
|   transactions_root    |    text    | 
+------------------------+------------+
|      state_root        |    text    |
+------------------------+------------+
|     receipts_root      |    text    | 
+------------------------+------------+
|         miner          |    text    | 
+------------------------+------------+
|      difficulty        |    text    | 
+------------------------+------------+
|   total_difficulty     |    text    | 
+------------------------+------------+
|      extra_data        |    text    |
+------------------------+------------+
|        size            |    Int     |
+------------------------+------------+ 
|      gas_limit         |    Int     |
+------------------------+------------+ 
|    min_gas_price       |    Int     |
+------------------------+------------+ 
|      gas_used          |    Int     |
+------------------------+------------+ 


Sample Blocks Table Queries
+++++++++++++++++++++++++++++++++++

To read data from the Ethereum blocks table, simply run your query on mangroves-cli or mangroves SQLite compatible API with the programming language of your choice, as shown below:


    - You can query against the data realted to the blocks on the public blockchain.

    .. image:: /images/read_first_blocks.png
        :width: 600

    - Feel free to try other queries as well:

    .. image:: /images/read_less_than_10_blocks.png
        :width: 600

    .. code-block:: sql

    SELECT nonce, size, gas_limit, min_gas_price, gas_used, difficulty, timestamp 
    FROM blocks WHERE number=15329147;


    .. image:: /images/read_last_blocks_data.png
        :width: 600


- How about **mangroves SQLite compatible API**? Let's try the query using ``Python`` anf ``JS``:

.. tabs:: lang

    .. code-tab:: python

         import sqlite3
         import pandas as pd

         from sqlite3 import Error
         try:
             url = 'https://cloudflare-eth.com/'
             con = sqlite3.connect(url)

             print(f"Connection is established: Mangroves connected to {url}")

             df = pd.read_sql_query("SELECT nonce, size, gas_limit, min_gas_price, gas_used, difficulty, timestamp FROM blocks WHERE number=15329147;", con)

             df.to_csv("blocks.csv")

         except Error:
            print(Error)

    .. code-tab:: js

         class Main {
            public static void main(String[] args) {
            }
         }



.. _transactionsRef:

.. _transactions:

Transactions Table
------------------------
This table is designed to store the data related to the transactions of the Ethereum network. 

+---------------------------+-------------+
|         Column Name       |     Type    |
|                           |             |
+===========================+=============+
|             hash          |    text     |
+---------------------------+-------------+
|      transaction_index    |     Int     |
+---------------------------+-------------+
|         from_address      |    text     | 
+---------------------------+-------------+
|         to_address        |    text     | 
+---------------------------+-------------+
|             value         |    text     |
+---------------------------+-------------+
|              gas          |     Int     | 
+---------------------------+-------------+
|           gas_price       |     Int     |
+---------------------------+-------------+
|            input          |    text     | 
+---------------------------+-------------+
|        block_number       |     Int     | 
+---------------------------+-------------+
|         block_hash        |    text     |
+---------------------------+-------------+


Sample Transactions Table Queries
+++++++++++++++++++++++++++++++++++
In order to read data from the Ethereum transactions table, as stated before, simply run your query on mangroves-cli or mangroves SQLite compatible API with the programming language of your choice as shown below:

   - Query the :ref:`Transactions Table <transactions>`:

      .. code-block:: SQL

            select transaction_index, from_address, to_address, value, gas
             from transactions where block_number=33243462 order by value desc limit 5;


   - You can expect a result like this:

   .. image:: /images/polygon_trnsaction.png
     :width: 600


- Let's **mangroves SQLite compatible API**. We can write our queries using any programming language. We show examples in ``Python`` anf ``JS``:

.. tabs:: lang

    .. code-tab:: python

         import sqlite3
         import pandas as pd

         from sqlite3 import Error
         try:
             url = 'https://cloudflare-eth.com/'
             con = sqlite3.connect(url)

             print(f"Connection is established: Mangroves connected to {url}")

             df = pd.read_sql_query("select count(hash) from transactions where block_hash='f8b492a7b7eb9396d95c6b9b2f81d19a3661b562460a91c854fd0cbe195e0210';;", con)

             df.to_csv("blocks.csv")

         except Error:
            print(Error)

    .. code-tab:: js

         class Main {
            public static void main(String[] args) {
            }
         }


.. _contractsRef:

.. _contracts:

Contracts Table
-----------------

The smart contracts data related to the Ethereum public network will be saved in this tabele. This table can be a good resource for the smart contracts data defined
in your platform.


+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|        address         | varchar(42)|
+------------------------+------------+
|        bytecode        |    text    | 
+------------------------+------------+
|   function_sighashes   |    text    |
+------------------------+------------+


.. _logsRef:

.. _logs:

Logs Table
-----------------
The logs related to the Ethereum network are stored in this table. The index of the log, transaction hash and index, adress and other related are inserted to this table. 

+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|        log_index       |   bigint   | 
+------------------------+------------+
|    transaction_hash    | varchar(66)|
+------------------------+------------+
|    transaction_index   |   bigint   | 
+------------------------+------------+
|        address         | varchar(42)|
+------------------------+------------+
|         data           |   text     |
+------------------------+------------+
|        topic0          | varchar(66)| 
+------------------------+------------+
|        topic1          | varchar(66)| 
+------------------------+------------+
|        topic2          | varchar(66)| 
+------------------------+------------+
|        topic3          | varchar(66)| 
+------------------------+------------+
|    block_timestamp     |  timestamp | 
+------------------------+------------+
|      block_number      |   bigint   | 
+------------------------+------------+
|      block_hash        | varchar(66)|
+------------------------+------------+


.. _token_transfersRef:

.. _token_transfers:

Token Transfers Table
------------------------
The tokens transferring data, including the address that the transfer originates from and the address receiving the data is added to this table.

+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|     token_address      | varchar(42)| 
+------------------------+------------+
|     from_address       | varchar(42)| 
+------------------------+------------+
|      to_address        | varchar(42)| 
+------------------------+------------+
|        value           | numeric(78)| 
+------------------------+------------+
|    transaction_hash    | varchar(66)| 
+------------------------+------------+
|       log_index        |   bigint   | 
+------------------------+------------+
|    block_timestamp     |  timestamp |
+------------------------+------------+
|      block_number      |   bigint   | 
+------------------------+------------+
|       block_hash       | varchar(66)| 
+------------------------+------------+


.. _tokensRef:

.. _tokens:

Tokens Table
------------------------
This table stores the tokens data. Address, name, symbol and other necessary data related to the Ethereum network tokens are stored in this table.

+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|        address         | varchar(42)| 
+------------------------+------------+
|         name           |    text    | 
+------------------------+------------+
|        symbol          |    text    | 
+------------------------+------------+
|      decimals          |   int(11)  | 
+------------------------+------------+
|    function_sighashes  |   string   | 
+------------------------+------------+


.. _tracesRef:

.. _traces:

Traces Table
------------------------
The traces of the Ethereum public blockchain are stored in this table. 

+------------------------+-------------+
|      Column Name       |   Type      |
|                        |             |
+========================+=============+
|    transaction_hash    | varchar(66) |
+------------------------+-------------+
|   transaction_index    |   bigint    | 
+------------------------+-------------+
|      from_address      | varchar(42) |
+------------------------+-------------+
|      to_address        | varchar(42) | 
+------------------------+-------------+
|        vlaue           | numeric(38) |
+------------------------+-------------+
|        input           |    text     |
+------------------------+-------------+
|        output          |    text     |
+------------------------+-------------+
|      trace_type        | varchar(16) | 
+------------------------+-------------+
|      call_type         | varchar(16) |
+------------------------+-------------+
|     reward_type        | varchar(16) | 
+------------------------+-------------+
|        gas             |   bigint    |
+------------------------+-------------+  
|      gas_used          |   bigint    |
+------------------------+-------------+ 
|      subtraces         |   bigint    |
+------------------------+-------------+ 
|    trace_address       |varchar(8192)|
+------------------------+-------------+ 
|        error           |    text     |
+------------------------+-------------+
|        status          |    int      |
+------------------------+-------------+
|   block_timestamp      |  timestamp  |
+------------------------+-------------+
|      block_number      |   bigint    |
+------------------------+-------------+ 
|      block_hash        | varchar(66) |
+------------------------+-------------+ 
|       trace_id         |    text     |
+------------------------+-------------+

