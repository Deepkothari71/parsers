from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json
from parsers.bank_parsers import detect_bank_and_parse

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/parse', methods=['POST'])
def parse_statement():
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check if file is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Parse the PDF
            print(f"\n{'='*50}")
            print(f"📄 Processing file: {filename}")
            print(f"{'='*50}")
            
            result = detect_bank_and_parse(filepath)
            
            if result is None:
                print("❌ Parsing failed - no data extracted")
                return jsonify({'error': 'Could not parse the statement. The PDF may be scanned/image-based or format is not recognized. Please try a different statement.'}), 400
            
            print(f"\n✅ Successfully parsed statement!")
            print(f"Bank: {result.get('Bank', 'Unknown')}")
            print(f"{'='*50}\n")
            
            return jsonify(result), 200
            
        except Exception as e:
            return jsonify({'error': f'Error parsing PDF: {str(e)}'}), 500
        
        finally:
            # Clean up - delete the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/download/<format>', methods=['POST'])
def download_data(format):
    try:
        data = request.json
        
        if format == 'json':
            return jsonify(data), 200
        
        elif format == 'csv':
            import pandas as pd
            df = pd.DataFrame([data])
            csv_data = df.to_csv(index=False)
            return csv_data, 200, {
                'Content-Type': 'text/csv',
                'Content-Disposition': 'attachment; filename=statement_data.csv'
            }
        
        else:
            return jsonify({'error': 'Invalid format'}), 400
            
    except Exception as e:
        return jsonify({'error': f'Download error: {str(e)}'}), 500

@app.errorhandler(413)
def file_too_large(e):
    return jsonify({'error': 'File size exceeds 5MB limit'}), 413

if __name__ == '__main__':
    print("🚀 Credit Card Statement Parser Server")
    print("📍 Server running at: http://localhost:5000")
    print("📄 Open http://localhost:5000 in your browser")
    print("-" * 50)
    app.run(debug=True, port=5000)