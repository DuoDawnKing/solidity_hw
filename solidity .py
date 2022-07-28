

pragma solidity ^0.5.0;

// Define a new contract named `JointSavings`
contract JointSavings {

    address payable accountOne;
    address payable accountTwo; 
    address public lastToWithdraw;
    uint public contractBalance;
    uint public lastWithdrawAmount;

    /*
    Inside the new contract define the following variables:
    - Two variables of type `address payable` named `accountOne` and `accountTwo`
    
    - A variable of type `address public` named `lastToWithdraw`
    - Two variables of type `uint public` named `lastWithdrawAmount` and `contractBalance`.
    */
    // YOUR CODE HERE!

    /*
    Define a function named **withdraw** that will accept two arguments.
    - A `uint` variable named `amount`
    - A `payable address` named `recipient`
    */
    function withdraw(uint amount, address payable recipient) public {

        /*
        Define a `require` statement that checks if the `recipient` is equal to either `accountOne` or `accountTwo`. The `requiere` statement returns the text `"You don't own this account!"` if it does not.
        */
        // YOUR CODE HERE!
        require(recipient == accountOne || recipient == accountTwo, "You do not own either account");
        require(address(this).balance >= amount, "You have insufficent funds for this account" );
        if (lastToWithdraw != recipient) {
            lastToWithdraw = recipient;
        }
        lastWithdrawAmount = amount; 
        contractBalance = address(this).balance;
         return msg.sender.transfer(amount); 
        // Call the `transfer` function of the `recipient` and pass it the `amount` to transfer as an argument.
        // YOUR CODE HERE!
       


        

        // Call the `contractBalance` variable and set it equal to the balance of the contract by using `address(this).balance` to reflect the new balance of the contract.
        // YOUR CODE HERE!
        

        contractBalance = address(this).balance;
    }

    // Define a `public payable` function named `deposit`.
    function deposit() public payable {

        /*
        Call the `contractBalance` variable and set it equal to the balance of the contract by using `address(this).balance`.
        */
        // YOUR CODE HERE!
        contractBalance = address(this).balance;
    }

    /*
    Define a `public` function named `setAccounts` that receive two `address payable` arguments named `account1` and `account2`.
    */
    function setAccounts(address payable account1, address payable account2) public{

        // Set the values of `accountOne` and `accountTwo` to `account1` and `account2` respectively.
        // YOUR CODE HERE!

        accountOne = account1;
        accountTwo = account2; 
    }

    /*
    Finally, add the **default fallback function** so that your contract can store Ether sent from outside the deposit function.
    */
    // YOUR CODE HERE!
    function() external payable {
  }


}