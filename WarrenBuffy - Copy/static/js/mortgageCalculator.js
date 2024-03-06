document.addEventListener('DOMContentLoaded', function() {
    // Wait for the DOM content to be fully loaded

    // Get a reference to the calculate button
    let calculateButton = document.getElementById("calculate-button");

    // Get a reference to the container where the results will be displayed
    let resultsContainer = document.getElementById('mortgage-payment-container');

    // Add an event listener to the calculate button
    calculateButton.addEventListener("click", function(event){
        // Prevent the default form submission behavior
        event.preventDefault();

        try {

        let propertyValue = document.getElementById('propertyValue').value;
        let propertyTax = document.getElementById('propertyTax').value;
        let homeInsurance = document.getElementById('homeInsurance').value;
        let downPayment = document.getElementById('downPayment').value;
        let interestRate = document.getElementById('interestRate').value;
        let mortgageLength = document.getElementsByName('mortgageLength');

        let selectedValue = null; // Initialize value for storing the checked radio button

        // Find the user's selection
        for (let i = 0; i < mortgageLength.length; i++) {
            if (mortgageLength[i].checked) {
                // Store selected value 
                selectedValue = mortgageLength[i].value;
                break;
            }
        }    

        // Validate the input
            if (isNaN(propertyValue) || isNaN(propertyTax) || isNaN(homeInsurance) || isNaN(downPayment) || isNaN(interestRate)) {
                    throw new Error("Invalid input: Not a number");
                }


                // Perform the calculations
                // Mortgage payment formula - M = P * (r(1 + r)^n / (1 + r)^n - 1)
                // r = annual interest rate / 12

                let monthlyInterest = (interestRate/100) / 12;
                let monthlyInterestPlusOne = 1 + monthlyInterest;
                let numberPayments = selectedValue * 12;
                let interestMortLengthExp = Math.pow(monthlyInterestPlusOne, numberPayments);

                downPayment = (downPayment - 100) / -100; // Calculates the percentage of property value after downpayment
                propertyValue = propertyValue * downPayment; // Calculates property value dollar amount
                propertyTax = propertyTax / 12; // Divide by monthly
                homeInsurance = homeInsurance / 12; // Divide by monthly

                // Finalize the mortgage payment calculation.
                let mortgageLoanPayment = propertyValue * ((monthlyInterest * interestMortLengthExp) 
                / (interestMortLengthExp - 1)) ;
                let mortgagePayment = mortgageLoanPayment + propertyTax + homeInsurance;

                


    
                // Update the results container with the calculated values
                resultsContainer.innerHTML = `
                    <p>Your Mortgage Payment is: $${mortgagePayment.toFixed(2)}</p>
                    <br/>
                    <p>Month   Interest     Principal      Balance</p>
                `;

                let paymentResults = ""; // Variable to store the mortgage payment results
                let balanceLeft = propertyValue;

                for (let i = 1; i <= numberPayments; i++) {
                    
                    let interestPayment = balanceLeft * monthlyInterest; 
                    let principalPayment = mortgageLoanPayment - interestPayment;
                    balanceLeft -= principalPayment;
    
                    // Concatenate the result for each month
                    paymentResults += `<p>Month ${i}: 
                    Interest: $${interestPayment.toFixed(2)}, 
                    Principal: $${(mortgageLoanPayment - interestPayment).toFixed(2)}, 
                    Balance: $${balanceLeft.toFixed(2)}</p>`;
                                            
                }
    
                resultsContainer.innerHTML += paymentResults;

            } catch(error) {
                // Handle any errors that occur during calculation
                console.error("Error: ", error.message);
                resultsContainer.innerHTML = "Error: " + error.message;
            }
    });
});
