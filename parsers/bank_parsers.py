import re
from parsers.base_parser import BaseParser

class HDFCParser(BaseParser):
    """Parser for HDFC Bank credit card statements"""
    
    def parse(self):
        data = {
            "Bank": "HDFC Bank",
            "Cardholder": self.extract_with_regex(r"(?:Name|Cardholder)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*Period|Billing\s*Cycle|Statement\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|Payment\s*Due)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|By)|Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class ICICIParser(BaseParser):
    """Parser for ICICI Bank credit card statements"""
    
    def parse(self):
        data = {
            "Bank": "ICICI Bank",
            "Cardholder": self.extract_with_regex(r"(?:Name|Customer\s*Name)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*Period|Bill\s*Period)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|Minimum\s*Amount\s*Due)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|on)|Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class SBIParser(BaseParser):
    """Parser for SBI Card statements"""
    
    def parse(self):
        data = {
            "Bank": "SBI Card",
            "Cardholder": self.extract_with_regex(r"(?:Name|Card\s*Member)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*Period|Billing\s*Period)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|Outstanding)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|By)|Due\s*(?:Date|on))[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class AxisParser(BaseParser):
    """Parser for Axis Bank credit card statements"""
    
    def parse(self):
        data = {
            "Bank": "Axis Bank",
            "Cardholder": self.extract_with_regex(r"(?:Name|Primary\s*Card\s*Member)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*(?:Period|Date)|Billing\s*Cycle)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|Amount\s*Payable)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|By)|Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class AmexParser(BaseParser):
    """Parser for American Express credit card statements"""
    
    def parse(self):
        data = {
            "Bank": "American Express",
            "Cardholder": self.extract_with_regex(r"(?:Name|Card\s*Member)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4,5})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*(?:Period|Closing\s*Date)|Billing\s*Period)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|New\s*Balance|Payment\s*Due)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|By)|Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class PNBParser(BaseParser):
    """Parser for Punjab National Bank credit card statements"""
    
    def parse(self):
        data = {
            "Bank": "Punjab National Bank",
            "Cardholder": self.extract_with_regex(r"(?:Name|Card\s*Holder|Customer\s*Name)[:\s]+([^\r\n]+)"),
            "Card Last 4 Digits": self.extract_with_regex(r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})"),
            "Billing Cycle": self.extract_with_regex(r"(?:Statement\s*(?:Period|Date)|Billing\s*(?:Period|Cycle))[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"),
            "Total Due": self.extract_amount(r"(?:Total\s*(?:Amount\s*)?Due|Outstanding|Amount\s*Payable)[:\s]*(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)"),
            "Payment Due Date": self.extract_date(r"(?:Payment\s*Due\s*(?:Date|By)|Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})")
        }
        return data

class GenericParser(BaseParser):
    """Generic parser for any credit card statement"""
    
    def parse(self):
        # Try to detect bank name from the PDF
        bank_name = self.detect_bank_name()
        
        data = {
            "Bank": bank_name,
            "Cardholder": self.extract_cardholder(),
            "Card Last 4 Digits": self.extract_card_number(),
            "Billing Cycle": self.extract_billing_cycle(),
            "Total Due": self.extract_total_due(),
            "Payment Due Date": self.extract_due_date()
        }
        return data
    
    def detect_bank_name(self):
        """Try to detect bank name from common patterns"""
        # Extended bank patterns
        bank_patterns = [
            (r'(HDFC\s*Bank)', 'HDFC Bank'),
            (r'(ICICI\s*Bank)', 'ICICI Bank'),
            (r'(SBI\s*Card)', 'SBI Card'),
            (r'(State\s*Bank)', 'State Bank of India'),
            (r'(Axis\s*Bank)', 'Axis Bank'),
            (r'(American\s*Express|AMEX)', 'American Express'),
            (r'(Punjab\s*National\s*Bank|PNB)', 'Punjab National Bank'),
            (r'(Kotak\s*Mahindra)', 'Kotak Mahindra Bank'),
            (r'(Yes\s*Bank)', 'Yes Bank'),
            (r'(IndusInd\s*Bank)', 'IndusInd Bank'),
            (r'(Citibank|Citi)', 'Citibank'),
            (r'(Standard\s*Chartered)', 'Standard Chartered'),
            (r'(HSBC)', 'HSBC'),
            (r'(RBL\s*Bank)', 'RBL Bank'),
            (r'(Bank\s*of\s*Baroda|BOB)', 'Bank of Baroda'),
            (r'(Canara\s*Bank)', 'Canara Bank'),
            (r'(Union\s*Bank)', 'Union Bank of India'),
            (r'(IDFC\s*First)', 'IDFC FIRST Bank'),
        ]
        
        text_upper = self.text.upper()
        
        for pattern, bank_name in bank_patterns:
            if re.search(pattern, text_upper, re.IGNORECASE):
                return bank_name
        
        return "Unknown Bank"
    
    def extract_cardholder(self):
        """Try multiple patterns to find cardholder name"""
        patterns = [
            # Label and value on the same line
            r"(?:Name|Card\s*Holder|Customer\s*Name|Primary\s*Card\s*Member|Card\s*Member)[:\s]+([^\r\n]+)",
            # Label on one line and value on next line
            r"(?:Name|Card\s*Holder|Customer\s*Name|Primary\s*Card\s*Member|Card\s*Member)\s*[:]*\s*\r?\n\s*([^\r\n]+)",
            # Greetings line
            r"(?:Dear|Mr\.?|Mrs\.?|Ms\.?)\s+([^\r\n]+)",
            # Fallback two-or-three word capitalized name
            r"([A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)"
        ]
        
        for pattern in patterns:
            result = self.extract_with_regex(pattern)
            if result != "Not Found" and len(result) > 3:
                return result
        
        return "Not Found"
    
    def extract_card_number(self):
        """Try multiple patterns to find card last 4 digits"""
        patterns = [
            r"(?:Card\s*(?:Number|No\.?|#)|ending\s*(?:in|with)|xxxx)[:\s]*[xX*\s\-]*?(\d{4})",
            r"[xX*]{4,12}[\s\-]?(\d{4})",
            r"(?:Card|A\/C)[:\s]*[xX*\s\-]*?(\d{4})"
        ]
        
        for pattern in patterns:
            result = self.extract_with_regex(pattern)
            if result != "Not Found" and result.isdigit() and len(result) == 4:
                return result
        
        return "Not Found"
    
    def extract_billing_cycle(self):
        """Try multiple patterns to find billing cycle"""
        patterns = [
            r"(?:Statement\s*(?:Period|Date)|Billing\s*(?:Period|Cycle|From))[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3,9}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\w{3,9}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})",
            r"(?:From|Period)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\s*(?:to|-|–)\s*\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
            r"(\d{1,2}\s+\w{3,9}\s+\d{4}\s*(?:to|-|–)\s*\d{1,2}\s+\w{3,9}\s+\d{4})"
        ]
        
        for pattern in patterns:
            result = self.extract_with_regex(pattern)
            if result != "Not Found":
                return result
        
        return "Not Found"
    
    def extract_total_due(self):
        """Try multiple patterns to find total due amount"""
        patterns = [
            # Core labels excluding date contexts (Payment Due Date / Due Date)
            r"(?:Total\s*(?:Amount\s*)?Due|Amount\s*Payable|Outstanding|New\s*Balance|Payment\s*Due(?!\s*Date))[^\d\r\n]{0,20}(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)",
            # 'Total' followed by amount (avoid generic 'Due' to prevent 'Due Date' collisions)
            r"Total[^\d\r\n]{0,20}(?:\n\s*)?(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)",
            # Currency first patterns
            r"(?:Rs\.?|INR|₹)\s*([\d,]+\.?\d*)\s*(?:Due|Payable)"
        ]
        
        for pattern in patterns:
            result = self.extract_amount(pattern)
            if result != "₹0.00":
                return result
        
        # Fallback: scan lines near 'Total Due' and pick the first valid amount on the same or next two lines
        try:
            lines = self.text.splitlines()
            for i, line in enumerate(lines):
                if re.search(r"total\s*(amount\s*)?due", line, re.IGNORECASE):
                    neighborhood = "\n".join(lines[i:i+3])
                    m = re.search(r"([\d]{1,3}(?:[, ]\d{2,3})+(?:\.\d{1,2})?|\d+\.\d{1,2}|\d{4,})", neighborhood)
                    if m:
                        amt = re.sub(r"\s+", "", m.group(1))
                        if not amt.startswith('₹'):
                            amt = '₹' + amt
                        return amt
        except Exception:
            pass
        
        return "₹0.00"
    
    def extract_due_date(self):
        """Try multiple patterns to find payment due date"""
        patterns = [
            r"(?:Payment\s*Due\s*(?:Date|By|On)|Due\s*(?:Date|By|On)|Pay\s*By)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\w{3,9}[/-]\d{2,4}|\d{1,2}\s+\w{3,9}\s+\d{4})",
            r"(?:Due\s*Date)[:\s]*(?:\n\s*)?(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})",
            r"(?:Pay\s*By|Due)[:\s]*(?:\n\s*)?(\d{1,2}\s+\w{3,9}\s+\d{4})"
        ]
        
        for pattern in patterns:
            result = self.extract_date(pattern)
            if result != "Not Found":
                return result
        
        return "Not Found"


def detect_bank_and_parse(pdf_path):
    """
    Detect which bank issued the statement and parse accordingly
    """
    # UNIVERSAL MODE: always use GenericParser for broader compatibility
    # Note: keeping the bank-specific detection and dispatch below for reference.
    return GenericParser(pdf_path).parse()

    # --- Previous bank-specific flow (kept for reference) ---
    # parser = BaseParser(pdf_path)
    # text = parser.text.lower()
    # bank_patterns = {
    #     'hdfc': ['hdfc', 'hdfc bank'],
    #     'icici': ['icici', 'icici bank'],
    #     'sbi': ['sbi card', 'state bank'],
    #     'axis': ['axis bank', 'axis'],
    #     'amex': ['american express', 'amex']
    # }
    # detected_bank = None
    # for bank, patterns in bank_patterns.items():
    #     for pattern in patterns:
    #         if pattern in text:
    #             detected_bank = bank
    #             break
    #     if detected_bank:
    #         break
    # if detected_bank == 'hdfc':
    #     return HDFCParser(pdf_path).parse()
    # elif detected_bank == 'icici':
    #     return ICICIParser(pdf_path).parse()
    # elif detected_bank == 'sbi':
    #     return SBIParser(pdf_path).parse()
    # elif detected_bank == 'axis':
    #     return AxisParser(pdf_path).parse()
    # elif detected_bank == 'amex':
    #     return AmexParser(pdf_path).parse()
    # else:
    #     parsers = [HDFCParser(pdf_path), ICICIParser(pdf_path), SBIParser(pdf_path), AxisParser(pdf_path), AmexParser(pdf_path)]
    #     best_result = None
    #     best_score = 0
    #     for parser in parsers:
    #         result = parser.parse()
    #         score = sum(1 for v in result.values() if v != "Not Found" and v != "₹0.00")
    #         if score > best_score:
    #             best_score = score
    #             best_result = result
    #     return best_result if best_score > 2 else None