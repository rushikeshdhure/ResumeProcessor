from pyresparser import ResumeParser
import spacy

# Load spacy model
spacy.load('en_core_web_sm')

def extract_resume_details(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return {
        'first_name': data.get('name', '').split()[0] if data.get('name') else '',
        'email': data.get('email', ''),
        'mobile_number': data.get('mobile_number', '')
    }
