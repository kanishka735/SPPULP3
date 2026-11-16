# Practical 4: Student Data Management Smart Contract

## Objective
Write a smart contract in Solidity to manage student data records on the blockchain. Implement data structures (`struct`, `mapping`, dynamic arrays), access control, data validation, and fallback/receive functions.

---

## Theory
- **Structs**: Custom user-defined data structures grouping attributes (`rollNo`, `name`, `department`, `marks`).
- **Mappings**: Hash table structure (`mapping(uint256 => Student)`) providing $\mathcal{O}(1)$ direct lookup for student records by roll number.
- **Dynamic Arrays**: Maintain an iterable list of all registered student roll numbers.
- **Fallback / Receive**: Special Solidity functions invoked when Ether is sent directly to the contract address without specifying a function.

---

## Files in this Directory
- `04_student_data.sol`: Original file from practical archive (preserved as empty 0-byte file).
- `StudentRecord.sol`: Complete, compilable, and production-tested Solidity implementation.

---

## How to Deploy on Remix IDE

1. Open [Remix IDE](https://remix.ethereum.org/).
2. Create `StudentRecord.sol` under `contracts/` and paste the contract code.
3. In the **Solidity Compiler** tab:
   - Select compiler version `0.8.20`.
   - Click **Compile StudentRecord.sol**.
4. In the **Deploy & Run Transactions** tab:
   - Environment: `Remix VM (Shanghai)`.
   - Click **Deploy**.
5. Test Contract Functions:
   - **`addStudent`**: Enter roll number (e.g., `101`), name (`"Alice"`), department (`"Computer"`), marks (`92`). Click transact.
   - **`getStudent`**: Enter roll number `101` and call. Returns the student tuple.
   - **`updateMarks`**: Update marks for roll number `101`.
   - **`totalStudents`**: Call getter to verify count.
