SQL Supported Statements
=================================

MangrovesDB support sqlite sql statements. It is also designed based on PostgreSQL and the features of this open source object-relational database system will be added to future cersion of MGDB. PostgreSQL with over 30 years of active development has earned a strong reputation for reliability, feature robustness, and performance.

Almost all the statements on PostgreSQL are supported in MGDB as well. 

* :ref:`Select <Select>`
* :ref:`Insert <Insert>`
* :ref:`Delete <Delete>`
* :ref:`Update <Update>`
* :ref:`Create Table <Create_Table>`
* :ref:`Create View <Create_View>`
* :ref:`Drop <Drop>`
* :ref:`Alter Table <Alter_Table>`

.. _select:

SELECT
--------------------
The **SELECT** statement retrieves data from the blockchain. Technically the rows returned by performing SELECT operation, are the data written on blockchain. You can use this statement in mangroves to simply read data from the blockchain considering mangroves supported tables.
Here is a sample query using this statement:

.. code-block:: SQL

     select number, gas_limit, timestamp from blocks where number=15415600;

Feel free to check the timestamp using this page. 


.. _Insert:

Insert
--------------------
The **INSERT** statement retrieves data from the blockchain. Technically the rows returned by performing SELECT operation, are the data written on blockchain.


.. _Delete:

Delete
--------------------

Using **Delete** statement you can delete a row from a table identified by its name.


.. _Update:

Update
--------------------

The **UPDATE** statement is used to modify the values in a table.


.. _Create_Table:

Create Table
--------------------

The **CREATE TABLE** statement creates a table in the database.


.. _Create_View:

Create View
--------------------

The **CREATE VIEW** statement defines a new view in the database.



.. _Drop:

Drop
--------------------

The **DROP** statement removes a database entry added previously with the CREATE command.


.. _Alter_Table:

Alter Table
--------------------

Changes in the schema, adding and dropping columns can be handled using **ALTER TABLE** statement. This statement would be applied on a currrently available table.


