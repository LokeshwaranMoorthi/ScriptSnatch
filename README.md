# ScriptSnatch

The idea came from noticing how handwritten prescriptions often lead to delays or errors in pharmacies. So, I built a Django web app that lets users upload prescription images. I integrated Doctr OCR to extract text, filtered out medicine names, and matched them against an inventory stored in memory. The system then automatically generated an order summary for the patient.

**ScriptSnatch** is a web application designed to process handwritten prescription images using OCR (Optical Character Recognition) technology. The app extracts prescription data, matches the extracted medicines against an in-memory inventory, and generates an order for the patient. It leverages **Django**, **Python**, **DOCTR** for OCR, **HTML5**, **CSS**, and **JavaScript** to create a seamless, interactive user experience.

---

## Features

- **Prescription Image Upload**: Users can upload prescription images in various formats (e.g., PNG, JPEG).
- **OCR Data Extraction**: The uploaded image is processed using **DOCTR** (a Python OCR tool) to extract relevant prescription information.
- **Inventory Matching**: Extracted medicines are matched against an in-memory inventory to check availability.
- **Order Generation**: After matching, the system generates an order summary for the patient.
- **Real-Time Updates**: Using JavaScript and AJAX, the order details and prescription data are dynamically updated on the page without reloading.

---

## Tech Stacks

- **Backend**: Django, Python
- **OCR**: DOCTR
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: MySQL (for storing prescription and inventory data)
- **Version Control**: Git, GitHub

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/LokeshwaranMoorthi/ScriptSnatch.git
cd ScriptSnatch

Install Dependencies:

Python: Make sure you have Python installed.

Install required Python packages:
pip install -r requirements.txt

Database Setup: Set up MySQL and configure the database. Update the DATABASES settings in settings.py as per your configuration.

Run Migrations:
python manage.py migrate

Running the Application

To run the application locally:
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to access the app.
