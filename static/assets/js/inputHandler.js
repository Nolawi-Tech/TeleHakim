function handleInput(input) {
    if (!isValidInput(input)) {
      // Set response code for invalid input
      return {
        statusCode: 400, // Bad Request
        message: 'Invalid input provided.'
      };
    }
  
    // Process valid input
    // ...
  
    // Set response code for successful processing
    return {
      statusCode: 200, // OK
      message: 'Input processed successfully.'
    };
  }
  
  // Function to validate input
  function isValidInput(input) {
    // Add your input validation logic here
    // Return true if the input is valid, otherwise false
  }
  
  // Example usage
  const userInput = 'abc';
  const response = handleInput(userInput);
  console.log(response.statusCode); // Output: 400
  console.log(response.message); // Output: Invalid input provided.
  