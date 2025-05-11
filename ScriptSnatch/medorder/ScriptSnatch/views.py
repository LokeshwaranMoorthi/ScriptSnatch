from django.shortcuts import render
from django.conf import settings
import os

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Load the OCR model only once
ocr_model = ocr_predictor(pretrained=True)

def extract_text_doctr(image_path):
    """Extract text using Doctr OCR."""
    doc = DocumentFile.from_images(image_path)
    result = ocr_model(doc)
    return result.export()["pages"][0]["blocks"]

def parse_medicines_from_blocks(blocks):
    all_medicines = {
        'paracetamol': {'price': 1.5, 'in_stock': True},
        'dolo': {'price': 2.0, 'in_stock': True},
        'crocin': {'price': 3.0, 'in_stock': True},
        'okacet': {'price': 2.5, 'in_stock': True}
    }

    detected_text = ' '.join(
        word['value']
        for block in blocks
        for line in block['lines']
        for word in line['words']
    ).lower()

    # Filtering only available medicines
    available_medicines = {
        med: details for med, details in all_medicines.items()
        if med in detected_text and details['in_stock']
    }

    return available_medicines

def index(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        file = request.FILES['prescription_image']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)

        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        blocks = extract_text_doctr(file_path)
        order = parse_medicines_from_blocks(blocks)

        return render(request, 'ScriptSnatch/results.html', {
            'patient_name': patient_name,
            'order': order
        })

    return render(request, 'ScriptSnatch/index.html')
