.. _mgeth:

Ethereum Catalog
======================
There are Seven main catalog tables for the Ethereum-based blockchain networks. These pre-defined tables are:
* :ref:`Block Table <blocks>`
* :ref:`Contracts Table<contracts>`
* :ref:`Logs Table<logs>`
* :ref:`Token Transfers Table<token_transfers>`
* :ref:`Tokens Table <tokens>`
* :ref:`Traces Table <traces>`
* :ref:`Transactions Table<transactions>`

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+


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


.. _logs:
Logs Table
-----------------


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


.. _token_transfers:
Token Transfers Table
------------------------


token_address	     varchar(42),
from_address	     varchar(42),
to_address	     varchar(42),
value	     numeric(78),
transaction_hash	     varchar(66),
log_index	     bigint,
block_timestamp	     timestamp,
block_number	     bigint,
block_hash	     varchar(66)