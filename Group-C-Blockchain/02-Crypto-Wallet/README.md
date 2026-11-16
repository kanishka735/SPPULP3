# Practical 2: Creating and Managing a Cryptocurrency Wallet

## Objective
Study, create, and understand the internal architecture of cryptocurrency wallets: asymmetric public-key cryptography (ECDSA secp256k1), mnemonic seed phrase generation (BIP-39), hierarchical deterministic wallets (BIP-32 / BIP-44), and address derivation.

---

## Theory & Key Concepts

### 1. Asymmetric Cryptography
- **Private Key**: A randomly generated 256-bit number. It must be kept strictly secret and is used to sign transactions.
- **Public Key**: Derived mathematically from the private key using Elliptic Curve Cryptography (secp256k1 curve):
  $$K = k \cdot G$$
  *(where $k$ is private key, $G$ is generator point, and $K$ is public key).*
- **Public Address**: Keccak-256 hash of the uncompressed public key (taking the last 20 bytes and prefixing with `0x`).

### 2. BIP-39 Mnemonic Standards
- Instead of memorizing 64 hexadecimal characters, a 12- or 24-word human-readable phrase is generated from high-entropy randomness with a checksum.

### 3. Hot Wallets vs. Cold Wallets
| Feature | Hot Wallet (Software / Browser) | Cold Wallet (Hardware / Paper) |
| :--- | :--- | :--- |
| **Internet Connection** | Always connected | Strictly offline |
| **Convenience** | High (instant transactions) | Moderate |
| **Security Risk** | Susceptible to malware/phishing | Immune to remote online hacks |

---

## Practical Implementation Steps
1. **Wallet Initialization**: Choose a wallet client (MetaMask, Trust Wallet, or Python `web3.py`/`eth-account`).
2. **Key Generation**: Generate entropy, derive root seed phrase, and generate account private/public keypair.
3. **Address Verification**: Confirm public address format matching Ethereum EIP-55 checksum encoding.
4. **Backup & Recovery**: Test wallet restoration using the 12-word recovery phrase on an isolated test environment.

---

## Files in this Directory
- `02_creating_own_wallet.txt`: Original submission file from archive (preserved as empty 0-byte file).
- `README.md`: In-depth study guide, cryptographic derivation workflow, and security guidelines.
