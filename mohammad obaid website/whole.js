// Show all publications
function showAll() {
    const publications = document.querySelectorAll('.publication');
    publications.forEach(publication => publication.classList.remove('hidden'));
}

// Filter by journal papers
function showJournal() {
    filterPublications('journal');
}

// Filter by conference papers
function showConference() {
    filterPublications('conference');
}

// Filter by magazine articles
function showMagazine() {
    filterPublications('magazine');
}

// Filter by book chapters
function showBook() {
    filterPublications('book');
}

// Filter by awarded papers
function showAwarded() {
    filterPublications('awarded');
}

// Filter by white papers
function showWhite() {
    filterPublications('white');
}

// General filter function
function filterPublications(type) {
    const publications = document.querySelectorAll('.publication');
    publications.forEach(publication => {
        if (publication.classList.contains(type)) {
            publication.classList.remove('hidden');
        } else {
            publication.classList.add('hidden');
        }
    });
}
