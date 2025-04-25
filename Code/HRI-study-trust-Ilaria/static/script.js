let round = 1;
let money = 100;
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
    window.location.href = "/invest_page";
}

// Handle investment submission
function submitInvestment() {
    if (isProcessing) return;
    
    const investmentInput = document.getElementById('investment');
    const investment = parseInt(investmentInput.value);
    
    if (isNaN(investment)) {
        showError("Please enter a valid number");
        investmentInput.focus();
        return;
    }
    
    if (investment < 0 || investment > money) {
        showError(`Please enter an amount between 0 and ${money}`);
        investmentInput.focus();
        return;
    }
    
    currentInvestment = investment;
    isProcessing = true;
    
    // Update progress bar
    updateProgressBar();
    
    // Show thinking page with flag to indicate we're coming from invest
    window.location.href = `/thinking_page?from_invest=true&investment=${investment}&round=${round}`;
}

function processInvestment() {
    fetch('/invest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            person_id: personId, 
            round: round, 
            investment: currentInvestment 
        })
    })
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(data => {
        if (data.error) throw new Error(data.error);
        
        // Update global variables
        round = data.round || round;
        money = data.money || money;
        bank = data.bank || bank;
        
        // Redirect to results page with all data
        window.location.href = `/results_page?investment=${data.investment}&returned=${data.returned}&classification=${data.classification}&money=${money}&bank=${bank}&round=${round}`;
    })
    .catch(error => {
        console.error("Error:", error);
        showError("Error processing your investment. Please try again.");
        window.location.href = "/invest_page";
    })
    .finally(() => {
        isProcessing = false;
    });
    console.log("Calling processInvestment with round:", round, "investment:", currentInvestment);

}

function nextRound() {
    if (round >= 20) {
        // Experiment complete - go to completion page
        window.location.href = `/completion_page?bank=${bank}`;
        return;
    }
    
    round++;
    window.location.href = "/invest_page";
}

function updateProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    if (progressBar) {
        const progress = (round / 20) * 100;
        progressBar.style.width = `${progress}%`;
    }
}

// Initialize page based on current URL
function initPage() {
    const path = window.location.pathname;
    const params = new URLSearchParams(window.location.search);
    
    if (path === "/") {
        document.getElementById('startButton').addEventListener('click', startExperiment);
    }
    else if (path === "/invest_page") {
        // Initialize round and money displays
        if (params.has('round')) round = parseInt(params.get('round'));
        if (params.has('money')) money = parseInt(params.get('money'));
        
        document.getElementById('round').textContent = round;
        document.getElementById('money').textContent = money;
        document.getElementById('investButton').addEventListener('click', submitInvestment);
        updateProgressBar();
        
        // Add progress bar if it doesn't exist
        if (!document.getElementById('progress-container')) {
            const progressHTML = `
                <div class="progress-container" id="progress-container">
                    <div class="progress-bar" id="progress-bar"></div>
                </div>
                <p class="progress-text">Round ${round} of 20</p>
            `;
            document.querySelector('.container').insertAdjacentHTML('afterbegin', progressHTML);
        }
        
        // Focus on input field
        document.getElementById('investment').focus();
    } 
    else if (path === "/thinking_page") {
        // If we have investment data, process it after delay
        if (params.has('from_invest')) {
            setTimeout(processInvestment, 2500);
        }
    }
    else if (path === "/results_page") {
        // Update all displayed values from URL parameters
        if (params.has('round')) round = parseInt(params.get('round'));
        if (params.has('money')) money = parseInt(params.get('money'));
        if (params.has('bank')) bank = parseInt(params.get('bank'));
        
        document.getElementById('round').textContent = round;
        document.getElementById('investment').textContent = params.get('investment') || 0;
        document.getElementById('returned').textContent = params.get('returned') || 0;
        
        const classification = params.get('classification');
        document.getElementById('classification').textContent = classification || "-";
        
        // Add icon based on classification
        const classificationElement = document.getElementById('classification');
        if (classification === "Trustful") {
            classificationElement.innerHTML = '<i class="fas fa-smile"></i> Trustful';
            document.querySelector('.container').style.borderTop = '5px solid var(--secondary-color)';
        } else {
            classificationElement.innerHTML = '<i class="fas fa-frown"></i> Untrustful';
            document.querySelector('.container').style.borderTop = '5px solid var(--accent-color)';
        }
        
        document.getElementById('money').textContent = money;
        document.getElementById('bank').textContent = bank;
        document.getElementById('nextButton').addEventListener('click', nextRound);
    }
    else if (path === "/completion_page") {
        if (params.has('bank')) bank = parseInt(params.get('bank'));
        document.getElementById('final-bank').textContent = bank;
    }
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
    // Check if we're coming from a page transition
    const params = new URLSearchParams(window.location.search);
    if (params.has('from_invest')) {
        // Remove the flag from URL
        params.delete('from_invest');
        window.history.replaceState({}, '', `${window.location.pathname}?${params.toString()}`);
    }
    
    initPage();
});

document.addEventListener("DOMContentLoaded", initPage);
console.log("initPage called");
console.log("from_invest:", params.get('from_invest'));
