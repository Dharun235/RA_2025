# Mohammad Obaid Website (`mywebsite/`)

This folder contains the source code and data for the personal and research website of Mohammad Obaid. The site is static and can be hosted on any standard web server.

## 📁 Folder Contents

- **index.html**  
  Main landing page with profile, vision, opportunities, social links, and latest updates.

- **NEWS.html**  
  News and updates about research, teaching, and other activities.

- **publications.html**  
  Displays the list of publications. Populated dynamically using `publications.js` and `publications.json`.

- **publications.js**  
  JavaScript to load and render publications from `publications.json`.

- **publications.json**  
  Machine-readable list of publications, generated from `publications.bib`.

- **publications.bib**  
  BibTeX file containing all publication entries. Used as the source for generating `publications.json`.

- **bib_to_json.py**  
  Python script to convert `publications.bib` to `publications.json`.

- **student_supervision.html**  
  Lists current and past students, interns, and research assistants.

- **contact.html**  
  Contact information, including protected email and phone number.

- **style.css**  
  Main stylesheet for the website.

- **.htaccess**  
  (If present) Used for server configuration, e.g., URL rewriting or access control.

## 🛠️ Usage

1. **Viewing the Website**  
   Open `index.html` in a browser, or upload all files to your web server.

2. **Updating Publications**  
   - Edit `publications.bib` to add or update entries  or download a new bibtex file and name it as `publications.bib`.
   - Run `bib_to_json.py` to regenerate `publications.json`.
   - Refresh `publications.html` in your browser to see updates.

3. **Customizing Content**  
   - Edit the respective HTML files for news, supervision, or contact details.
   - Update `style.css` for design changes.

## ⚠️ Notes

- **Images** (e.g., profile photos, logos) are referenced in the HTML but not described here.
- All dynamic content is handled client-side with JavaScript; no backend is required.
- For any server-specific configuration, refer to `.htaccess` if used.
