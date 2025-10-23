import fitz  # PyMuPDF
from pdfminer.high_level import extract_text
import re

class BaseParser:
    """Base class for all bank-specific parsers"""
    
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self.extract_text()
    
    def extract_text(self):
        """Extract text from PDF using PyMuPDF (faster)"""
        try:
            doc = fitz.open(self.pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except Exception as e:
            print(f"PyMuPDF failed, trying pdfminer: {e}")
            # Fallback to pdfminer
            try:
                return extract_text(self.pdf_path)
            except Exception as e2:
                print(f"pdfminer also failed: {e2}")
                return ""
    
    def extract_with_regex(self, pattern, default="Not Found"):
        """Extract data using regex pattern"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
        return default
    
    def extract_amount(self, pattern, default="₹0.00"):
        """Extract amount and format it"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            amount = match.group(1).strip()
            # Clean up amount (remove extra spaces, commas)
            amount = re.sub(r'\s+', '', amount)
            # Ensure it has rupee symbol
            if not amount.startswith('₹'):
                amount = '₹' + amount
            return amount
        return default
    
    def extract_date(self, pattern, default="Not Found"):
        """Extract date from text"""
        match = re.search(pattern, self.text, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
        return default
    
    def parse(self):
        """Override this method in child classes"""
        raise NotImplementedError("Each parser must implement parse()")
