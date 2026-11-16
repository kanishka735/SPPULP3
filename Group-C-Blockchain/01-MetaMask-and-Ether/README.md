# Practical 1: MetaMask Installation & Ether Transactions

## Objective
Install the MetaMask cryptocurrency wallet browser extension, configure an Ethereum test network (Sepolia / Holesky / Local Testnet), fund the account with test Ether via a faucet, and perform peer-to-peer Ether transfer transactions.

---

## What is MetaMask?
MetaMask is a self-custodial software cryptocurrency wallet and browser extension (Chrome, Firefox, Brave, Edge) that allows users to interact with the Ethereum blockchain, manage Ethereum private keys, and interact with decentralized applications (dApps).

---

## Step-by-Step Practical Procedure

### Step 1: Install MetaMask
1. Visit the official website: [https://metamask.io/](https://metamask.io/)
2. Download and install the extension for your browser.
3. Click **Create a new wallet**.
4. Set a strong password for local access.

### Step 2: Secure Your Secret Recovery Phrase (Seed Phrase)
> [!WARNING]
> Never share your 12-word Secret Recovery Phrase with anyone. Anyone with this phrase has full access to your funds.

1. Write down the 12-word seed phrase on paper and store it offline.
2. Confirm the words in sequence to finalize setup.

### Step 3: Enable Test Networks
1. Open MetaMask and click the network selector at the top-left.
2. Toggle **Show test networks**.
3. Select **Sepolia** test network.

### Step 4: Obtain Test Ether from a Faucet
1. Copy your wallet public address (`0x...`).
2. Visit an official Sepolia faucet (e.g., [Google Cloud Web3 Sepolia Faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia) or [Sepolia PoW Faucet](https://sepolia-faucet.pk910.de/)).
3. Paste your wallet address and request test ETH.
4. Verify that your balance reflects the received test ETH in MetaMask.

### Step 5: Perform an Ether Transaction
1. Obtain a recipient testnet wallet address.
2. Click **Send** in MetaMask.
3. Enter the recipient address and the amount of Ether (e.g., `0.01 SepoliaETH`).
4. Review Gas fees and click **Confirm**.
5. Once mined, click the transaction to view its receipt on [Sepolia Etherscan](https://sepolia.etherscan.io/).

---

## Files in this Directory
- `01_metamaskinstallation nd ether transaction.txt`: Original submission file from archive (preserved as empty 0-byte file).
- `README.md`: Complete theoretical notes, execution procedure, and verification steps.
