let round = 1;
let money = 10;
let bank = 0;
let currentInvestment = 0;
let personId = "";
let isProcessing = false;

// Start the experiment
function startExperiment() {
    personId = document.getElementById('person_id').value.trim();
    if (personId === "") {
        showError("Please enter a Person ID");
        return;
    }
    // Reset all values when starting new experiment
    round = 1;
    money = 10;
    bank = 0;
    window.location.href = `/invest_page?person_id=${encodeURIComponent(personId)}`;
}

function submitInvestment() {
    if (isProcessing) return;
    
    const investment = parseInt(document.getElementById('investment').value);
    
    if (isNaN(investment)) {
        showError("Please enter a valid number");
        return;
    }
    
    if (investment < 0 || investment > money) {
        showError(`Please enter an amount between 0 and ${money}`);
        return;
    }
    
    currentInvestment = investment;
    isProcessing = true;
    
    // Redirect to thinking page with all current state
    window.location.href = `/thinking_page?person_id=${encodeURIComponent(personId)}&round=${round}&investment=${investment}&money=${money}`;
}

function processInvestment() {
    const params = new URLSearchParams(window.location.search);
    const person_id = params.get('person_id');
    const round_num = params.get('round');
    const investment = params.get('investment');
    
    fetch('/invest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            person_id: person_id,
            round: round_num,
            investment: investment
        })
    })
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(data => {
        if (data.error) throw new Error(data.error);
        
        // Update global variables
        round = parseInt(data.round);
        money = parseInt(data.money);
        bank = parseInt(data.bank);
        
        // Redirect to results page with all data
        window.location.href = `/results_page?person_id=${encodeURIComponent(person_id)}&round=${round}&investment=${data.investment}&returned=${data.returned}&classification=${data.classification}&money=${money}&bank=${bank}`;
    })
    .catch(error => {
        console.error("Error:", error);
        showError("Error processing investment. Please try again.");
        window.location.href = `/invest_page?person_id=${encodeURIComponent(person_id)}&round=${round}&money=${money}`;
    });
}

function nextRound() {
    if (round >= 10) {
        window.location.href = `/completion_page?bank=${bank}`;
        return;
    }
    
    round++;
    window.location.href = `/invest_page?person_id=${encodeURIComponent(personId)}&round=${round}&money=${money}`;
}

function updateProgressBar() {
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    
    // Calculate the percentage
    const percentage = Math.round((round / 10) * 100);
    
    // Update the progress bar value and text
    progressBar.value = percentage;
    progressText.textContent = `Round ${round} of 10 - ${percentage}%`;
}


// Initialize page based on current URL
function initPage() {
    const params = new URLSearchParams(window.location.search);
    
    // Always update global state from URL parameters
    personId = params.get('person_id') || personId;
    round = parseInt(params.get('round')) || round;
    money = parseInt(params.get('money')) || money;
    bank = parseInt(params.get('bank')) || bank;

    const path = window.location.pathname;
    
    if (path === "/") {
        document.getElementById('startButton').addEventListener('click', startExperiment);
    }
    else if (path === "/invest_page") {
        document.getElementById('round').textContent = round;
        document.getElementById('money').textContent = money;
        document.getElementById('investButton').addEventListener('click', submitInvestment);
    }
    else if (path === "/thinking_page") {
        // Automatically process investment after short delay
        setTimeout(processInvestment, 2500);
    }
    else if (path === "/results_page") {
    document.getElementById('round').textContent = round;
    document.getElementById('investment').textContent = params.get('investment') || 0;
    document.getElementById('returned').textContent = params.get('returned') || 0;
    
    // Remove classification update since it's not displayed anymore
    
    // Remove money update since it's no longer displayed
    document.getElementById('bank').textContent = bank;
    document.getElementById('nextButton').addEventListener('click', nextRound);
    updateProgressBar();  
    }

    else if (path === "/completion_page") {
        document.getElementById('final-bank').textContent = bank;
    }
}

document.addEventListener("DOMContentLoaded", initPage);