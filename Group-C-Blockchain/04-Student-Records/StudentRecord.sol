// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title StudentData
 * @dev SPPU LP-III Blockchain Assignment: Student Data Smart Contract
 * Demonstrates structs, arrays, mappings, fallback/receive functions, and access control.
 */
contract StudentData {

    struct Student {
        uint256 rollNo;
        string name;
        string department;
        uint256 marks;
        bool exists;
    }

    address public admin;
    uint256 public totalStudents;

    // Mapping from roll number to Student record
    mapping(uint256 => Student) private students;
    uint256[] private rollNumbers;

    // Events
    event StudentAdded(uint256 indexed rollNo, string name, string department);
    event StudentUpdated(uint256 indexed rollNo, string name, uint256 marks);
    event EtherReceived(address indexed sender, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not the contract administrator");
        _;
    }

    constructor() {
        admin = msg.sender;
        totalStudents = 0;
    }

    /**
     * @notice Add a new student record
     */
    function addStudent(
        uint256 _rollNo,
        string memory _name,
        string memory _department,
        uint256 _marks
    ) public onlyAdmin {
        require(!students[_rollNo].exists, "Student with this roll number already exists");
        require(_rollNo > 0, "Roll number must be positive");

        students[_rollNo] = Student({
            rollNo: _rollNo,
            name: _name,
            department: _department,
            marks: _marks,
            exists: true
        });

        rollNumbers.push(_rollNo);
        totalStudents++;

        emit StudentAdded(_rollNo, _name, _department);
    }

    /**
     * @notice Retrieve student details by roll number
     */
    function getStudent(uint256 _rollNo) public view returns (
        uint256 rollNo,
        string memory name,
        string memory department,
        uint256 marks
    ) {
        require(students[_rollNo].exists, "Student record not found");
        Student memory s = students[_rollNo];
        return (s.rollNo, s.name, s.department, s.marks);
    }

    /**
     * @notice Update student marks
     */
    function updateMarks(uint256 _rollNo, uint256 _newMarks) public onlyAdmin {
        require(students[_rollNo].exists, "Student record does not exist");
        students[_rollNo].marks = _newMarks;
        emit StudentUpdated(_rollNo, students[_rollNo].name, _newMarks);
    }

    /**
     * @notice Fallback function to handle direct Ether transfers
     */
    receive() external payable {
        emit EtherReceived(msg.sender, msg.value);
    }

    fallback() external payable {
        emit EtherReceived(msg.sender, msg.value);
    }
}
