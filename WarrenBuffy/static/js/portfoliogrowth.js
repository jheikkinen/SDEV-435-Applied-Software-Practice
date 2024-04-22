document.addEventListener('DOMContentLoaded', function() {
    // Wait for the DOM content to be fully loaded

    // Get a reference to the calculate button
    let calculateButton = document.getElementById("calculate-button");

    // Get a reference to the container where the results will be displayed
    let resultsContainer = document.getElementById('portfolio-growth-container');

    // Add an event listener to the calculate button
    calculateButton.addEventListener("click", function(event){
        // Prevent the default form submission behavior
        event.preventDefault();

        try {
            // Get the values entered by the user
            let portfolioAmount = parseFloat(document.getElementById('portfolioAmount').value);
            let numberYears = parseFloat(document.getElementById('yearsGrowth').value);
            let monthlyContribution = parseFloat(document.getElementById('monthlyContribution').value);
            let annualInterest = parseFloat(document.getElementById('annualInterest').value);

            // Validate the input
            if (portfolioAmount < 0 || numberYears <= 0 || monthlyContribution < 0 || annualInterest <= 0 || isNaN(portfolioAmount) || isNaN(numberYears) || isNaN(monthlyContribution) || isNaN(annualInterest)) {
                throw new Error("Invalid input: Needs to be a positive number");
            }

            // Perform the calculations
            let yearlyContribution = monthlyContribution * 12;
            let annualInterestRate = (annualInterest / 100) + 1;
            let yearlyPortfolioIncrease = portfolioAmount;

            let growthResults = ""; // Variable to store the growth results

            for (let i = 1; i <= numberYears; i++) {
                yearlyPortfolioIncrease = (yearlyPortfolioIncrease + yearlyContribution) * annualInterestRate;

                // Concatenate the result for each year
                growthResults += `<p>Year ${i}: $${yearlyPortfolioIncrease.toFixed(2)}</p>`;
            }

            // Update the results container with the calculated values
            resultsContainer.innerHTML = `
                <p>Total Portfolio Growth Calculated: $${yearlyPortfolioIncrease.toFixed(2)}</p>
                ${growthResults} 
            `;

        } catch(error) {
            // Handle any errors that occur during calculation
            console.error("Error: ", error.message);
            resultsContainer.innerHTML = "Error: " + error.message;
        }
    });
});