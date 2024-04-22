document.addEventListener('DOMContentLoaded', function() {
    // Wait for the DOM content to be fully loaded

    // Get a reference to the calculate button
    let calculateButton = document.getElementById("calculate-button");

    // Get a reference to the container where the results will be displayed
    let resultsContainer = document.getElementById('investment-risk-container');

    // Add an event listener to the calculate button
    calculateButton.addEventListener("click", function(event){
        // Prevent the default form submission behavior
        event.preventDefault();

        try {
            // Get the values entered by the user
            let portfolioAmount = parseFloat(document.getElementById('portfolioAmount').value);
            let purchasePrice = parseFloat(document.getElementById('purchasePrice').value);
            let stopPrice = parseFloat(document.getElementById('stopPrice').value);
            let riskPercentage = parseFloat(document.getElementById('riskPercentage').value);

            // Validate the input
            if (portfolioAmount <= 0 || purchasePrice <= 0 || stopPrice <= 0 || riskPercentage <= 0 || isNaN(portfolioAmount) || isNaN(purchasePrice) || isNaN(stopPrice) || isNaN(riskPercentage)) {
                throw new Error("Invalid input: Needs to be a positive number");
            }

            // Perform the calculations
            let riskAmount = portfolioAmount * (riskPercentage / 100);
            let priceDifference = purchasePrice - stopPrice;
            let percentPurchasePrice = priceDifference / purchasePrice;
            let totalAmountToRisk = riskAmount / percentPurchasePrice;
            let totalUnitsToPurchase = totalAmountToRisk / purchasePrice;

            // Update the results container with the calculated values
            resultsContainer.innerHTML = `
                <p>Total Amount to risk: $${totalAmountToRisk.toFixed(2)}</p>
                <p>Total Amount of Units to Purchase: ${totalUnitsToPurchase.toFixed(2)}</p>
            `;

        } catch(error) {
            // Handle any errors that occur during calculation
            console.error("Error: ", error.message);
            resultsContainer.innerHTML = "Error: " + error.message;
        }
    });
});