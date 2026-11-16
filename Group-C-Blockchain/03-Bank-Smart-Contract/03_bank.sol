/*
====================================================
PRACTICAL 3: BANK ACCOUNT SMART CONTRACT
====================================================

AIM:
To create a smart contract for banking operations
such as Deposit Money, Withdraw Money and Show Balance.

PROBLEM STATEMENT:
Create a Solidity smart contract that allows users
to deposit money, allows only the owner to withdraw
money and displays the current balance.

THEORY:
1. Solidity is used to write smart contracts.
2. Ethereum is a blockchain platform.
3. Smart contracts execute predefined instructions.
4. Payable allows a function to receive Ether.
5. Gas is the computational cost of execution.

REQUIREMENTS:
1. Remix IDE
2. Solidity Compiler 0.8.20
3. Ethereum Remix VM

ALGORITHM:
1. Start.
2. Deploy the BankAccount contract.
3. Store the deployer's address as owner.
4. Deposit Ether using deposit().
5. Check balance using showBalance().
6. Withdraw Ether using withdraw().
7. Display updated balance.
8. Stop.

SAMPLE INPUT:
Deposit = 2 ETH
Deposit = 1 ETH
Withdraw = 1 ETH

EXPECTED OUTPUT:
After first deposit = 2 ETH
After second deposit = 3 ETH
After withdrawal = 2 ETH

EXECUTION STEPS:
1. Open https://remix.ethereum.org/
2. Create BankAccount.sol.
3. Paste the program.
4. Compile the contract.
5. Select Remix VM.
6. Deploy the contract.
7. Enter Ether in VALUE field.
8. Click deposit.
9. Click showBalance.
10. Enter withdrawal amount in Wei.
11. Click withdraw.
12. Check updated balance.

RESULT:
Successfully implemented Bank Account Smart Contract.

====================================================
*/

 // ACTUAL SOLIDITY PROGRAM STARTS HERE

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    // Stores the address of contract owner.
    address public owner;

    // Stores the current contract balance.
    uint256 public balance;

    // Event generated when money is deposited.
    event Deposited(address indexed from, uint256 amount);

    // Event generated when money is withdrawn.
    event Withdrawn(address indexed to, uint256 amount);

    // Constructor executes only once during deployment.
    constructor() {
        owner = msg.sender;
    }

    // DEPOSIT FUNCTION
    // payable allows the function to receive Ether.
    function deposit() external payable {

        // Deposit amount must be greater than zero.
        require(msg.value > 0, "Deposit must be greater than zero");

        // Add deposited Ether to balance.
        balance += msg.value;

        // Generate deposit event.
        emit Deposited(msg.sender, msg.value);
    }

    // WITHDRAW FUNCTION
    function withdraw(uint256 amount) external {

        // Only owner can withdraw money.
        require(msg.sender == owner, "Only owner can withdraw");

        // Check whether withdrawal amount is valid.
        require(amount > 0 && amount <= balance, "Invalid amount");

        // Deduct amount from balance.
        balance -= amount;

        // Transfer Ether to owner.
        (bool success, ) = payable(owner).call{value: amount}("");

        // Check whether transfer succeeded.
        require(success, "Transfer failed");

        // Generate withdrawal event.
        emit Withdrawn(owner, amount);
    }

    // SHOW BALANCE FUNCTION
    // view means blockchain data is only read.
    function showBalance() external view returns (uint256) {

        // Return current balance.
        return balance;
    }
}

/*
====================================================
VIVA QUESTIONS AND ANSWERS
====================================================

Q1. What is Solidity?
Ans. Solidity is a programming language used to
     develop smart contracts.

Q2. What is a Smart Contract?
Ans. A self-executing program stored on blockchain.

Q3. What is msg.sender?
Ans. Address of the account calling the function.

Q4. What is msg.value?
Ans. Amount of Ether sent with a transaction.

Q5. What is payable?
Ans. It allows a function to receive Ether.

Q6. What is constructor?
Ans. A special function executed once during deployment.

Q7. What is require()?
Ans. It checks conditions and reverts if false.

Q8. What is Gas?
Ans. Unit used to measure computational work.

Q9. What is an Event?
Ans. It records information in transaction logs.

Q10. What is the use of view?
Ans. It allows reading data without modifying state.

====================================================
*/