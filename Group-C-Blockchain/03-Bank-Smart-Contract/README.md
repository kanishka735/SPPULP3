# Practical 3: Bank Account Smart Contract in Solidity

## Objective
Design, write, compile, and deploy an Ethereum smart contract in Solidity for basic banking operations:
- Depositing Ether (`deposit`)
- Withdrawing Ether (`withdraw`, restricted to owner)
- Querying account balance (`showBalance`)
- Tracking transactions with events (`Deposit`, `Withdrawal`)

---

## Theory
- **Smart Contract**: Immutable, self-executing computer program deployed to the Ethereum Virtual Machine (EVM).
- **`payable` modifier**: Allows functions or addresses to receive Ether.
- **Access Control (`modifier onlyOwner`)**: Restricts sensitive actions (e.g. withdrawal) to the deployer's address (`msg.sender`).
- **State Variables**: Persist permanently in the contract's blockchain storage.
- **Events**: Emit logs written into Ethereum transaction receipts, allowing dApp frontends and off-chain indexers to listen for changes.

---

## Contract Code: `Bank.sol` / `03_bank.sol`
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {
    address public owner;

    event Deposit(address indexed accountHolder, uint256 amount);
    event Withdrawal(address indexed accountHolder, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the account owner can perform this action");
        _;
    }

    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
        emit Withdrawal(owner, amount);
    }

    function showBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
```

---

## How to Deploy on Remix IDE

1. Open [Remix Ethereum IDE](https://remix.ethereum.org/).
2. In the File Explorer, create a new file `Bank.sol` and paste the code from `Bank.sol`.
3. In the **Solidity Compiler** tab:
   - Select Compiler version `0.8.20` or higher.
   - Click **Compile Bank.sol**.
4. In the **Deploy & Run Transactions** tab:
   - Environment: Select **Remix VM (Shanghai)** or **Injected Provider - MetaMask**.
   - Click **Deploy**.
5. Interacting with the deployed contract:
   - **deposit()**: Enter a Value in the Value box (e.g., `1` Ether) and click `deposit`.
   - **showBalance()**: Click `showBalance` to view the updated contract balance (in Wei).
   - **withdraw()**: Specify amount in Wei and click `withdraw`.
