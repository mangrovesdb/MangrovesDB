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
- 2 CPUs or more
- 2GB of free memory
- 20GB of free disk space
- Internet connection


.. _Installation:

Installation
-----------------
There are some requirements before installing MGDB. 


.. tabs::

   .. tab:: Linux

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: Binary download

                        To install the latest mangroves stable release on x86-64 Linux using binary download:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
                            sudo install minikube-linux-amd64 /usr/local/bin/minikube

                     .. tab:: sqlite SDK

                        To install the latest mangroves stable release on x86-64 Linux for sqlite compatible sdk:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
                            sudo dpkg -i minikube_latest_amd64.deb

             .. tab:: ARM64

                 .. tabs::

                     .. tab:: Binary download

                        To install the latest minikube stable release on ARM64 Linux using binary download:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
                            sudo install minikube-linux-arm64 /usr/local/bin/minikube


                     .. tab:: sqlite SDK

                        To install the latest mangroves stable release on ARM64 Linux for sqlite compatible sdk:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_arm64.deb
                            sudo dpkg -i minikube_latest_arm64.deb

   .. tab:: macOS

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: Binary download

                        To install the latest mangroves stable release on x86-64 macOS using binary download:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
                            sudo install minikube-darwin-amd64 /usr/local/bin/minikube

                     .. tab:: sqlite SDK

                        To install the latest mangroves stable release on x86-64 macOS for sqlite compatible sdk:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
                            sudo install minikube-darwin-amd64 /usr/local/bin/minikube
 
             .. tab:: ARM64

                 .. tabs::

                     .. tab:: Binary download

                        To install the latest mangroves stable release on ARM64 macOS using binary download:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
                            sudo install minikube-darwin-arm64 /usr/local/bin/minikube


                     .. tab:: sqlite SDK

                        To install the latest mangroves stable release on ARM64 macOS for sqlite compatible sdk:

                        .. code-block:: bash

                            curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
                            sudo install minikube-darwin-arm64 /usr/local/bin/minikube

   .. tab:: Windows

         .. tabs::

             .. tab:: x86-64

                 .. tabs::

                     .. tab:: .exe download

                        Download and run the installer for the latest release. Or if using PowerShell, use this command:

                        .. code-block:: bash

                            New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
                            Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing


                     .. tab:: sqlite SDK

                        Download and run the installer for the latest release sqlite compatible sdk. Or if using PowerShell, use this command: 

                        .. code-block:: bash

                            New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
                            Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing




.. _QuTut:

Quickstart Tutorial
----------------------

You can simply use mangroves CLI to query dat on the public blockchain, e.g., Ethereum. You can also test the mangroves compatible library with sqlite SDK. In what follows there are some examples of how to test each of these services:


MangrovesDB CLI
+++++++++++++++++

- **1. Running mangroves CLI** 

From a terminal, run:

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

    The url can be any available Ethereum gateway. Mangroves can handle all nodes, in different netowrk layers. You can also try yur custome full node.

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


   - Query the :ref:`Block Table <blocks>`:

      .. code-block:: SQL

            select number, hash, parent_hash from blocks where number=15368213;


   - You can expect a result like this:

   .. image:: /images/sampQueBlocks1.png


Verify the results in underlying blockchain networks and available blockchain explorer platforms. For the abovve query you can chack this `page <https://etherscan.io/block/15368213>`_.

.. Note:: 

    You can run other queries and extract other data related to :ref:`Block Table <blocks>`, :ref:`Transactions Table <transactions>`, :ref:`Contracts Table <contracts>`, :ref:`Logs Table <logs>`, :ref:`Token Transfers Table <token_transfers>`, :ref:`Tokens Table <tokens>`. Here are some samples: 
         
    .. code-block:: SQL

       select number, hash, nonce, gas_limit, min_gas_price, gas_used from blocks where number<20 order by number desc limit 5;



.. admonition:: Caution

    Do not forget to add **;** at the end of your query. This will enable the Mangroves CLI that your query statement is finished.

.. Attention::

    Find what you can query from the :ref:`Block Table <blocksRef>`.


.. DANGER::

    If you are using public Ethereum gateways, please do not use the mangroves CLI to extract huge portion of data from blockchain |:stop_sign:|. Such queries will last too long or failed. You can try mangroves sqlite sdk comaptible.


MangrovesDB sqlite library
++++++++++++++++++++++++++++

Leveraging MangrovesDb Library you can use the sqlite powerful tools and write simple queries in any programming langiages of your choice in any platform. 
You can see some examples about how mangroves in intergradted with sqlite SDK to perform queries.

.. tabs::

   .. code-tab:: c

         int main(const int argc, const char **argv) {
         return 0;
         }

   .. code-tab:: c++

         int main(const int argc, const char **argv) {
         return 0;
         }

   .. code-tab:: py

         def main():
            return

   .. code-tab:: java

         class Main {
            public static void main(String[] args) {
            }
         }

   .. code-tab:: julia

         function main()
         end

   .. code-tab:: fortran

         PROGRAM main
         END PROGRAM main

   .. code-tab:: r R

         main <- function() {
            return(0)
         }