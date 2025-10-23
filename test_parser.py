"""
Test script to debug PDF parsing
Usage: python test_parser.py path/to/your/statement.pdf
"""

import sys
from parsers.bank_parsers import detect_bank_and_parse
from parsers.base_parser import BaseParser

def test_pdf(pdf_path):
    print(f"\n{'='*60}")
    print(f"🧪 Testing PDF Parser")
    print(f"{'='*60}")
    print(f"📄 File: {pdf_path}\n")
    
    # Step 1: Extract text
    print("Step 1: Extracting text from PDF...")
    try:
        parser = BaseParser(pdf_path)
        text = parser.text
        print(f"✅ Extracted {len(text)} characters")
        
        # Show first 500 characters
        print(f"\n📝 First 500 characters of extracted text:")
        print("-" * 60)
        print(text[:500])
        print("-" * 60)
        
        # Check if text extraction worked
        if len(text) < 100:
            print("\n⚠️  WARNING: Very little text extracted!")
            print("   This PDF might be:")
            print("   - Image-based (scanned document)")
            print("   - Password protected")
            print("   - Corrupted")
            print("\n   Consider using OCR (Tesseract) for scanned PDFs")
            return
        
    except Exception as e:
        print(f"❌ Error extracting text: {e}")
        return
    
    # Step 2: Detect bank
    print(f"\nStep 2: Detecting bank...")
    text_lower = text.lower()
    
    banks_found = []
    bank_keywords = {
        'HDFC': ['hdfc'],
        'ICICI': ['icici'],
        'SBI': ['sbi card', 'state bank'],
        'Axis': ['axis bank'],
        'AmEx': ['american express', 'amex'],
        'PNB': ['punjab national', 'pnb'],
        'Kotak': ['kotak'],
        'Yes Bank': ['yes bank'],
        'IndusInd': ['indusind'],
        'Citibank': ['citibank', 'citi'],
        'Standard Chartered': ['standard chartered'],
        'HSBC': ['hsbc'],
        'RBL': ['rbl bank']
    }
    
    for bank, keywords in bank_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                banks_found.append(bank)
                print(f"✅ Found keyword '{keyword}' → {bank}")
                break
    
    if not banks_found:
        print("⚠️  No known bank detected - will use generic parser")
    
    # Step 3: Parse data
    print(f"\nStep 3: Parsing statement data...")
    try:
        result = detect_bank_and_parse(pdf_path)
        
        if result:
            print(f"\n{'='*60}")
            print("✅ PARSING SUCCESSFUL!")
            print(f"{'='*60}")
            for key, value in result.items():
                status = "✅" if value not in ["Not Found", "₹0.00", "Unknown Bank"] else "❌"
                print(f"{status} {key:20s}: {value}")
            print(f"{'='*60}\n")
        else:
            print("\n❌ PARSING FAILED - No data could be extracted")
            print("\nPossible reasons:")
            print("  1. PDF is image-based (needs OCR)")
            print("  2. Statement format is very different")
            print("  3. Text extraction failed")
            print("\nTry:")
            print("  - Use a different statement")
            print("  - Check if PDF is text-based (try copy-paste text from PDF)")
            
    except Exception as e:
        print(f"❌ Error during parsing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_parser.py <path_to_pdf>")
        print("Example: python test_parser.py statement.pdf")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    test_pdf(pdf_file)
