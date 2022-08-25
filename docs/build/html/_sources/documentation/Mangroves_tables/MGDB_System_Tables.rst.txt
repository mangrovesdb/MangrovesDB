.. _mgTables:

MangrovesDB Tables
==============================
Technically, liek the other relational database management systems, the system Tables are the palce where all the data related to the schema metadata, such as information about tables and columns, and internal bookkeeping information, are stored.
MGDB-SQL's system Tables are regular tables pre-defined in the platform, i.e., the approach of the PostgreSQL as well. 
Similar to the PostgreSQL, you can apply SQL statements, e.g., drop and recreate the tables, add columns, insert and update values in these Table Tables. This is how 
you can set up what is best for your buisiness, however, this can cause severe problems and mess up with your system. Please kindly follow the guidance provided in this section to use SQL commands if
you want to make changes to these tables. The alternation should not be made by hand.
In what follows information related to these Table tables are provided:


* :ref:`Ethereum Table <mgeth>`
* :ref:`HyperLedger Table <mghplegger>`
* :ref:`Time-Zone Table <mgtz>`
* :ref:`Database Table <mgdb>`
* :ref:`Aggregate Table <mgagg>`
* :ref:`Type Table <mgty>`


.. toctree::
   :maxdepth: 2
   :caption: Ethereum Table
   :hidden:

   mg_ETH

.. toctree::
   :maxdepth: 2
   :caption: HyperLedger Table
   :hidden:

   mg_HyperLedger

.. toctree::
   :maxdepth: 2
   :caption: Time-Zone Table
   :hidden:
   
   mg_TimeZone

.. toctree::
   :maxdepth: 2
   :caption: Database Table
   :hidden:
   
   mg_database

.. toctree::
   :maxdepth: 2
   :caption: Aggregate Table
   :hidden:
   
   mg_agg

.. toctree::
   :maxdepth: 2
   :caption: Type Table
   :hidden:
   
   mg_type
