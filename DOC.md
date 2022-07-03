# MangrovesDB - Blockchain Technical Review

## Blockchain Use-Cases and DeFi Specification

### Problems with centralized finance
Five problems
    • **Centralized control**:
        • Centralized banking system is highly concentrated
        • National central banks control currency
        • Non-financial centralization of tech giants, e.g., Amazon-retail, Facebook/Google-digital advertising
    • **Limited access**:
        • 1.7 billion unbanked
        • Billions underbanked
        • Many entrepreneurs use credit cards to finance their businesses, since banks won’t lend to them because they are small (negative impact on growth)
    • **Inefficiency**:
        • 3% for a credit card swipe
        • 5-7% for a wire transfer
        • 2 days settlement time for a stock transaction
        • Slow transfers of funds
        • Fraud, chargebacks, insecurity
        • No micro transactions
        • Difficult to get paid
    • **Lack of interoperability**:
        • Siloed institutions
        • Difficult to move money from one banking institution to another
        • Difficult to move money from a bank to a non-bank
        • Note: Visa attempted acquisition of fintech company Plaid
    • **Opacity**:
        • Very little transparency
        • Bank customers do not know the health of the bank
        • Must rely on costly regulation and the promise of bailouts


## Bitcoin and cryptocurrency
• Stuart Haber and Scott Stornetta (1991) invent the blockchain idea to keep track of time stamping of documents
• Adam Back (2002) invents the Proof of Work idea. It is based on a key paper by Cynthia Dwork and Moni Naor (1992) that was aimed at eliminating junk mail (require the sender to do a computational task to send the email to you, while this is easy to do once – it is infeasible to do for millions of recipients)
• Satoshi Nakamoto (2008) put these ideas together to introduce bitcoin
• Bitcoin eliminated the key problem with digital currencies in the past (you can make a perfect digital copy and “double spend”)
• Every transaction would be kept in an immutable ledger (censorship resistant blockchain) and the ledger would be distributed across many different computers
• Cryptographic scarcity was enforced by a limit of 21 million bitcoins
• User sovereignty (only owner determines how to spend)
• Portability in that you can send or receive anywhere quickly and cheaply


## Bitcoin vs. fiat
• Scarcity and self-sovereignty create the potential for store of value
• While untested, there is no direct link to economic activity or inflation, so there could be some hedging
• Bitcoin was originally intended to be a peer-to-peer currency. However, its deflationary characteristics and flat fees discourage its use in small transactions.


## Ethereum history
• Began in 2015 with Vitalik Buterin
• Allows for running of computer programs. So Ethereum is a distributed computational platform offering functionality via offering a “smart contract platform”
• Smart contracts control assets and data, and define interactions between assets, data, and network participants.

## dApps
• Decentralized applications allow peers to interact directly and remove the need for a central clearing house for app interactions
• DeFi is fundamentally a competitive marketplace of financial dApps that function as various financial “primitives” such as exchange, lend, tokenize, and so forth.
• These dApps benefit from the network effects of combining and recombining DeFi products, and attracting increasingly more market share from the traditional financial ecosystem.

## What is blockchain?
• Blockchains are fundamentally software protocols that allow multiple parties to operate under shared assumptions and data without trusting each other
• These data can be anything, such as location and destination information of items in a supply chain or account balances of a token
• Updates are packaged into “blocks” and are “chained” together cryptographically to allow an audit of the prior history, hence the name.

## Hashing --> Blockchain
SHA-256 (Secure Hashing Algorithm)
https://emn178.github.io/online-tools/sha256.html
• Hashing is a one-way function.
• Hashing is not “encryption” because you can’t decrypt.
• For example, passwords are routinely stored on websites in hashed form.
• The output of a SHA-256 is 256 bits no matter how big the input
• Represented in hexadecimal form 0-9,1-f. Hence, 64 characters long.

## Blockchain Use-Cases
Solves many problems
• Verification of ownership (quickly check the immutable history recorded on a blockchain to see if someone owns something)
• Efficient exchange of ownership (direct transactions without middle person, everybody treated the same whether customer, retailer or banker).

## Why are blockchains special?
• Blockchains have consensus protocols (a set of rules that determine what kinds of blocks can become part of the chain and become the “truth”.)
• Once in a blockchain, the data remains there forever. This is the immutability property.
• These consensus protocols are designed to be resistant to malicious tampering up to a certain security bound.

## Proof of work
• Ethereum currently relies on Proof of Work (PoW) consensus protocol, which relies on a computational lottery to determine which block to add.
The participants agree that the longest chain of blocks is the truth.
• An attacker needs to amass 51% of the network computational power (this is the boundary of PoW security).
• Given the massive computational power of the Ethereum and Bitcoin networks, it is extremely unlikely that a malicious actor (or even an entire country) can attack these networks. This is not true for other less popular networks.

## Mining
• The computational lottery involves cryptographic hashing.
• Miners group transactions together, make sure they are valid, and add a small piece of metadata called a nonce. They run a hashing function (SHA-256 in Bitcoin and Keccak-256 in Ethereum) and try to get a very small value of the hash by cycling through different nonces.
• This task is computationally burdensome. However, when a miner wins it is very fast to verify that the transactions + nonce = winning hash. When verified, a new block is added.
• Proof of work is both a strength and a weakness of blockchain technology
• Strength because of unprecedented security
• Weakness because the electricity cost of mining is enormous
• Ethereum will move to a different, less energy inefficient, consensus technology
• Bitcoin is likely stuck with proof of work

## What is cryptocurrency?
• Cryptocurrency is a digital token that is cryptographically secured and transferred.
• Asymmetric key cryptography is a crucial component. Owners of cryptocurrency have a private key which is essentially a long random number.
• A public key is mathematically derived from the private key. This is a one way operation (you cannot – using today’s technology) derive the private key from the public key)
• Public addresses are derived from the public key
• If currency is transferred, the sender uses a digital signature algorithm to sign the token over to someone else’s address. The signature mathematically reveals that the sender has the private key associated with the senders public address.
• The token will now reside with the receiver and it can be transferred again using the receivers digital signature based on the receiver’s private key and a new party’s address.


## Smart Contracts

### Enhanced capabilities
• Bitcoin is a payments technology.
• Ethereum is the primary example of a smart contract platform.
• A smart contract is code that can create and transform arbitrary data or tokens on top of the blockchain of which it is a part.
• The concept is powerful because it allows the user to trustlessly encode rules for any type of transaction and even create scarce assets with specialized functionality.


### Trustless
• Many standard business contracts can be algorithmically encoded and algorithmically enforced
• These contracts run on the Ethereum blockchain and are run on every node.
• This is useful for in many use-cases like finance, supply chains, IoT, etc.

### Gas
• Users of smart contracts need to pay a fee, called gas.
• The gas price depends on the complexity of the calculation (think of a fee for using a cloud computing platform)
• Gas fees also help protect attacks on the system that cause an infinite loop of code (known as a halting problem)

### Turing complete
• Gas plays a very important role. A malicious attack would be prohibitively expensive.
• Ethereum is Turing complete – Bitcoin is not.

### Gas, Gas Price, and Gas Limit
• Every operation on the Ethereum blockchain requires gas
• A transfer ETH from one address to another requires 21,000 gas
• Each unit of gas has a gas price, which is denoted in gwei. 1 gwei = 1 billionth of an ETH. Gas prices increase as users outbid one another during times of higher network congestion
• If your gas price is much lower than the average gas price, your transaction will likely not be accepted
• The gas limit is the maximum amount of gas a user is willing to use for a transaction. A transaction can include multiple operations.

- Example
    • Assume the average gas price is 150 gwei and we call a function in a smart contract that transfers ETH, checks the balance of an account, and loads 2 bytes of memory from storage
    • The total amount of gas required is 21,000 + 400 + 200 = 21,600
    • The total cost of this transaction is 21,600*150*(1*10-9) = .00324 ETH
    • If we set our gas limit to 25,000, then we will be refunded the excess gas of 3,400
    • If we set our gas limit to 18,000, the miners will be unable to execute the entire transaction. However, we will not be refunded any gas since we still must pay for the computation

### Problems with Gas Prices
• Gas prices vary from 50 gwei to up to 700 gwei in times of high network congestion
• A gas price of 700 gwei and a transaction that requires 21,000 gas will result in $0.0013*21000=$27.3 to transfer money
• Ethereum’s first price auction mechanism allows miners to select transactions with the highest gas fees. This results in users overpaying in gas fees, sometimes by more than 5x.


### EIP 1599
• EIP 1559 is a hard fork that addresses the inefficiencies of the current gas fee mechanisms by instituting a base fee that transactions are required to pay and increasing the gas limit of a block
• The base fee is adjusted depending on network congestion and is burned after the transaction is approved
• Users still have the option to add a tip transaction that goes to a miner. This is useful in times of high congestion when users want to speed up a transaction.

#### Base Fee
• The base fee is adjusted on the amount of gas included in a single block. If the amount of gas in a block is over 12.5 million, then the base fee will increase and vice versa.
• To accommodate the base fee, the current gas limit in a block will be increased to a hard cap of 25 million. The average target is 12.5 million gas
• Burning the base fee puts downward pressure on the supply of ETH. If the ETH Issue: Burn ratio is below 1, then the supply of ETH is decreasing
• Miners/Validators will earn money from proposing blocks and transaction tips. Their expected returns are lower and a few ETH mining pools oppose the update.


### ERC
• ```Ethereum Request for Comment``` or ERC refer to standard interfaces for different types of functionality
• Most popular is ERC-20 which defines an interface for tokens whose units are identical in utility and functionality. It includes behavior such as transferring units and approving operators for using a certain portion of a user’s balance.

### Important ERCs
• **ERC-20** is a ```fungible token```. Traditional examples in fiat are $1 bills all have equal value (though different serial numbers) and 10 $1 bills are equal to a $10 bill
• **ERC-721** are ```non-fungible```. Each token is associated with a particular asset (for example, a loan).
• The benefit of these standards is that application developers can code for one interface, and support every possible token that implements that interface.

### What are oracles?
• Ethereum blockchain only knows what happens on the Ethereum blockchain. What is information is needed from outside the Ethereum blockchain? An ```oracle``` solves this problem.
• An **oracle, in the context of smart contract platforms, is any data source for reporting information external to the blockchain**.
• How can we create an oracle that can authoritatively speak about off-chain information in a trust-minimized way? This is known as the oracle problem.

### Oracle implementations
• An application might host its own oracle. This does not solve the trust problem.
• One '''Ethereum-based''' platform known as [Chainlink](https://chain.link/) is designed to solve the oracle problem by using an aggregation of data sources. The Chainlink whitepaper includes a reputation-based system that is decentralized.



# Use Cases - Full Review Each Section

## DeFi Solves Inefficiency Problem
### Keepers
• Keepers are external participants directly incentivized to provide a service to DeFi protocols, such as monitoring positions to safeguard that they are
sufficiently collateralized or triggering state updates for various functions.
• To ensure that a dApp’s benefits and services are optimally priced, keeper rewards are often structured as an auction.
• Pure, open competition provides value to DeFi platforms by guaranteeing users pay the market price for the services they need.

### Forking
• A fork, in the context of open source code, is a copy and reuse of the code with upgrades or enhancements layered on top.
• A common fork of blockchain protocols is to reference them in two parallel currencies and chains.
• Doing so creates competition at the protocol level and creates the best possible smart contract platform.

### dApps forkable
• Not only is the code of the entire Ethereum blockchain public and forkable, but each DeFi dApp built on top of Ethereum is as well.
• Should inefficient or suboptimal DeFi applications exist, the code can be easily copied, improved, and redeployed through forking.
• Forking and its benefits arise from the open nature of DeFi and blockchains.


### Vampirism
• Vampirism is an exact or near-exact copy of a DeFi platform designed to poach liquidity or users by offering larger incentives than the platform it is
copying.
• The larger incentives usually take the form of inflationary rewards offered at a far higher rate than the original platform offers.
• Users might be attracted to the higher potential reward for the same functionality, which would cause a reduction in usage and liquidity on the initial platform.


### Vampirism risks
• If the inflationary rewards are flawed, over long-term use the clone could perhaps collapse after a large asset bubble.
• The clones could also select closer to optimal models and replace the original platform.
• Vampirism is not an inherent risk or flaw, but rather a complicating factor arising from the pure competition and openness of DeFi.
• The selection process will eventually give rise to more robust financial infrastructure with optimal efficiency.


## DeFi Solves Limited Access Problem
• DeFi gives large underserved groups, such as the global population of the unbanked as well as small businesses that employ substantial portions of
the workforce (for example, nearly 50% in the United States) direct access to financial services.
• The resulting impact on the entire global economy should be positive.