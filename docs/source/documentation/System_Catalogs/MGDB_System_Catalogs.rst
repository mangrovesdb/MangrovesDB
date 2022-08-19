MGDB System Catalogs
==============================
Technically, liek the other relational database management systems, the system catalogs are the palce where all the data related to the schema metadata, such as information about tables and columns, and internal bookkeeping information, are stored.
MGDB-SQL's system catalogs are regular tables pre-defined in the platform, i.e., the approach of the PostgreSQL as well. 
Similar to the PostgreSQL, you can apply SQL statements, e.g., drop and recreate the tables, add columns, insert and update values in these Catalog Tables. This is how 
you can set up what is best for your buisiness, however, this can cause severe problems and mess up with your system. Please kindly follow the guidance provided in this section to use SQL commands if
you want to make changes to these tables. The alternation should not be made by hand.
In what follows information related to these catalog tables are provided:


* :ref:`Ethereum Catalog <mgeth>`
* :ref:`HyperLedger Catalog <mghplegger>`
* :ref:`Time-Zone Catalog <mgtz>`
* :ref:`Database Catalog <mgdb>`
* :ref:`Aggregate Catalog <mgagg>`
* :ref:`Type Catalog <mgty>`


.. toctree::
   :maxdepth: 2
   :caption: Ethereum Catalog
   :hidden:

   mg_ETH

.. toctree::
   :maxdepth: 2
   :caption: HyperLedger Catalog
   :hidden:

   mg_HyperLedger

.. toctree::
   :maxdepth: 2
   :caption: Time-Zone Catalog
   :hidden:
   
   mg_TimeZone

.. toctree::
   :maxdepth: 2
   :caption: Database Catalog
   :hidden:
   
   mg_database

.. toctree::
   :maxdepth: 2
   :caption: Aggregate Catalog
   :hidden:
   
   mg_agg

.. toctree::
   :maxdepth: 2
   :caption: Type Catalog
   :hidden:
   
   mg_type
