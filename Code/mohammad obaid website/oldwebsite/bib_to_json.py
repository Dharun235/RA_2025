import bibtexparser
import latex
import json

def latex_to_unicode(latex_str):
    """Convert LaTeX escape sequences to Unicode characters using latex package."""
    return latex.build(latex_str)

def process_bibtex_entry(entry):
    """Process each BibTeX entry to convert LaTeX escapes in the relevant fields."""
    # Convert LaTeX escapes in fields such as author, title, booktitle, etc.
    entry['author'] = latex_to_unicode(entry.get('author', ''))
    entry['title'] = latex_to_unicode(entry.get('title', ''))
    entry['booktitle'] = latex_to_unicode(entry.get('booktitle', ''))
    entry['journal'] = latex_to_unicode(entry.get('journal', ''))
    entry['publisher'] = latex_to_unicode(entry.get('publisher', ''))
    # Add more fields as necessary

    return entry

def convert_bibtex_to_json(bibtex_file, json_file):
    """Convert a BibTeX file to a JSON file."""
    # Read the BibTeX file
    with open(bibtex_file, 'r') as bibtex_f:
        bibtex_data = bibtexparser.load(bibtex_f)

    # Process each BibTeX entry
    processed_entries = []
    for entry in bibtex_data.entries:
        processed_entry = process_bibtex_entry(entry)
        processed_entries.append(processed_entry)

    # Write the processed entries to a JSON file
    with open(json_file, 'w') as json_f:
        json.dump(processed_entries, json_f, indent=4)

# Example usage
convert_bibtex_to_json('publications.bib', 'publications.json')
