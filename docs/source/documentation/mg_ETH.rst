.. _mgeth:

Ethereum Tables
======================
There are Seven main Table tables for the Ethereum-based blockchain networks. The main resource for these tables is this `library <https://pypi.org/project/ethereum-etl/1.0.0/>`_. 
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

Block Table
-----------------

The data related to the blocks of the Ethereum public network will be saved here. This base table can be used for any further design of a customized Ethereum-based
platform.

+------------------------+------------+
|      Column Name       |   Type     |
|                        |            |
+========================+============+
|      timestamp         | timestamp  |
+------------------------+------------+
|        number          |   bigint   | 
+------------------------+------------+
|        hash            | varchar(66)|
+------------------------+------------+
|      parent_hash       | varchar(66)| 
+------------------------+------------+
|      sha3_uncles       | varchar(66)|
+------------------------+------------+
|        nonce           | varchar(42)| 
+------------------------+------------+
|      logs_bloom        |   text     |
+------------------------+------------+
|   transactions_root    | varchar(66)| 
+------------------------+------------+
|      state_root        | varchar(66)|
+------------------------+------------+
|     receipts_root      | varchar(66)| 
+------------------------+------------+
|         miner          | varchar(42)| 
+------------------------+------------+
|      difficulty        | numeric(38)| 
+------------------------+------------+
|   total_difficulty     | numeric(38)| 
+------------------------+------------+
|      extra_data        |   text     |
+------------------------+------------+
|        size            |   bigint   |
+------------------------+------------+ 
|      gas_limit         |   bigint   |
+------------------------+------------+ 
|      gas_used          |   bigint   |
+------------------------+------------+ 
|  transaction_count     |   bigint   |
+------------------------+------------+ 
|   base_fee_per_gas     |   bigint   |
+------------------------+------------+ 

Sample Block Table Queries
+++++++++++++++++++++++++++++++++++

In order to read data from the ethereum public blockchain, as stated before simply run the MangrovesDB cli as shown below:

.. image:: /images/MGDB_CLI_Start.png
     :width: 600

Then you can query against the data realted to the blocks on the public blockchain.

.. image:: /images/read_first_blocks.png
     :width: 600

Feel free to try other queries as well:

.. image:: /images/read_less_than_10_blocks.png
     :width: 600

.. code-block:: sql

   SELECT nonce, size, gas_limit, min_gas_price, gas_used, difficulty, timestamp 
   FROM blocks WHERE number=15329147;


.. image:: /images/read_last_blocks_data.png
     :width: 600

.. tabs:: lang

    .. code-tab:: bash

        echo "Hello, group!"

    .. code-tab:: python

        print("Hello, group!")


.. tabs:: lang

    .. code-tab:: bash

        echo "Goodbye, group!"

    .. code-tab:: python

        print("Goodbye, group!")


.. _transactionsRef:

.. _transactions:

Transactions Table
------------------------
This table is designed to store the data related to the transactions of the Ethereum network. 

+---------------------------+-------------+
|         Column Name       |     Type    |
|                           |             |
+===========================+=============+
|             hash          | varchar(66) |
+---------------------------+-------------+
|             nonce         |   bigint    | 
+---------------------------+-------------+
|      transaction_index    |   bigint    |
+---------------------------+-------------+
|         from_address      | varchar(42) | 
+---------------------------+-------------+
|         to_address        | varchar(42) | 
+---------------------------+-------------+
|             value         | numeric(66) |
+---------------------------+-------------+
|              gas          |   bigint    | 
+---------------------------+-------------+
|           gas_price       |   bigint    |
+---------------------------+-------------+
|            input          |    text     | 
+---------------------------+-------------+
|receipt_cumulative_gas_used|   bigint    |
+---------------------------+-------------+
|      receipt_gas_used     |   bigint    | 
+---------------------------+-------------+
| receipt_contract_address  | varchar(42) |
+---------------------------+-------------+
|        receipt_root       | varchar(66) |
+---------------------------+-------------+
|      receipt_status       |   bigint    | 
+---------------------------+-------------+
|      block_timestamp      |  timestamp  |
+---------------------------+-------------+
|        block_number       |   bigint    | 
+---------------------------+-------------+
|         block_hash        | varchar(66) |
+---------------------------+-------------+
|      max_fee_per_gas      |   bigint    | 
+---------------------------+-------------+
| max_priority_fee_per_gas  |   bigint    | 
+---------------------------+-------------+
|      transaction_type     |   bigint    | 
+---------------------------+-------------+
|receipt_effective_gas_price|   bigint    | 
+---------------------------+-------------+


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
