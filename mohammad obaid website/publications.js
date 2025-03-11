async function loadPublications() {
    try {
        const response = await fetch("publications.json");
        if (!response.ok) {
            throw new Error("Failed to load JSON file.");
        }
        const publications = await response.json();
        
        console.log("Loaded Publications:", publications); // Debugging

        // Classify publications as conference or journal
        publications.forEach(pub => {
            if (pub.ID.startsWith("DBLP:conf/")) {
                pub.type = "conf";  
            } else if (pub.ID.startsWith("DBLP:journals/")) {
                pub.type = "journal";
            } else {
                pub.type = "other";
            }
        });

        // Group publications by year
        const publicationsByYear = groupBy(publications, "year");

        displayPublications(publicationsByYear);
        setupFilterButtons();
    } catch (error) {
        console.error("Error fetching publications:", error);
        document.getElementById("publication-list").textContent = "Error loading publications.";
    }
}

// Grouping function
function groupBy(array, key) {
    return array.reduce((result, obj) => {
        const groupKey = obj[key] || "Unknown";
        if (!result[groupKey]) {
            result[groupKey] = [];
        }
        result[groupKey].push(obj);
        return result;
    }, {});
}

// Display Publications
function displayPublications(publicationsByYear) {
    const container = document.getElementById("publication-list");
    container.innerHTML = ""; 

    const sortedYears = Object.keys(publicationsByYear).sort((a, b) => b - a);

    sortedYears.forEach(year => {
        const yearSection = document.createElement("h2");
        yearSection.textContent = year;
        container.appendChild(yearSection);

        publicationsByYear[year].forEach(pub => {
            const pubElement = document.createElement("div");
            pubElement.classList.add("publication");
            pubElement.setAttribute("data-type", pub.type);

            pubElement.innerHTML = `
                <div class="publication-info">
                    <p>
                        ${pub.author ? escapeHtml(pub.author) : "Unknown Authors"}.
                        <strong>${pub.title ? escapeHtml(pub.title) : "No Title"}</strong>
                        <br>
                        <em>${pub.booktitle ? escapeHtml(pub.booktitle) : pub.journal ? escapeHtml(pub.journal) : "No Source"}</em>.
                    </p>
                </div>
                <div class="publication-details">
                    <div class="buttons">
                        ${pub.url ? `<a href="${pub.url}" class="btn btn-primary" target="_blank">Link to Publication</a>` : ""}
                        ${pub.doi ? `<a href="https://doi.org/${pub.doi}" class="btn btn-success" target="_blank">DOI (link)</a>` : ""}
                        ${pub.biburl ? `<a href="${pub.biburl}" class="btn btn-secondary" target="_blank">BibTeX</a>` : ""}
                        ${pub.award ? `<span class="award">${escapeHtml(pub.award)}</span>` : ""}
                    </div>
                </div>
                <hr>
            `;

            container.appendChild(pubElement);
        });
    });
}

// Safe HTML escaping
function escapeHtml(str) {
    return str.replace(/[&<>"']/g, match => {
        const escapeMap = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return escapeMap[match];
    });
}

// Filter Setup
function setupFilterButtons() {
    document.getElementById("filter-all").addEventListener("click", () => filterPublications("all"));
    document.getElementById("filter-conf").addEventListener("click", () => filterPublications("conf"));
    document.getElementById("filter-journal").addEventListener("click", () => filterPublications("journal"));
}

// Filter Publications
function filterPublications(filterType) {
    console.log("Applying filters...");
    console.log("Filtering for:", filterType);

    const publications = document.querySelectorAll(".publication");

    publications.forEach(pub => {
        if (filterType === "all" || pub.getAttribute("data-type") === filterType) {
            pub.style.display = "block";
        } else {
            pub.style.display = "none";
        }
    });
}

// Load Data on Page Load
window.addEventListener("DOMContentLoaded", loadPublications);
