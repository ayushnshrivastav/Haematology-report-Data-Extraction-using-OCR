Blood Report Analysis Application

This repository contains the source code for a web application designed to analyze blood reports uploaded by users. The application utilizes OCR (Optical Character Recognition) technology to extract relevant information from the reports, such as name, age, sex, and various blood parameters. Subsequently, a rule-based algorithm assesses the extracted values to determine if they fall within normal ranges. If any values are found to be abnormal, the algorithm provides insights into the extent of deviation, potential causes, and suggestions for normalization.

Features:
OCR Integration: Utilizes OCR technology, including Roboflow, YoloV8, easyOCR, and pytesseract, to extract information from blood reports.
Rule-based Analysis: Analyzes extracted values to determine if they are within normal ranges.
Abnormality Detection: Identifies and reports abnormalities in blood parameters.
Detailed Insights: Provides percentage deviation, potential causes, and suggestions for abnormal values.
Sensitive Data Handling: Ensures confidentiality and security by processing sensitive data within the application.
Installation:
Clone the repository:
bash
Copy code
git clone <repository-url>
Install dependencies:
Copy code
pip install -r requirements.txt
Run the Flask application:
arduino
Copy code
flask run
Usage:
Upload Blood Report: Users can upload their blood reports via the web interface.
Report Analysis: The application automatically extracts relevant information from the report and analyzes the blood parameters.
Abnormality Detection: If any values are found to be abnormal, the application provides detailed insights into the deviation and potential causes.
Suggestions for Normalization: Users receive suggestions on how to normalize abnormal blood parameters.
Required Links:
Roboflow Project: Roboflow Project
YoloV8 Model: YoloV8 Model
Flask Documentation: Flask Documentation
LabelImg Tool: LabelImg Tool
Images:
Images of blood reports might be required for testing purposes. These images are not included in the repository due to privacy concerns.

Disclaimer:
Please note that this application is for educational and informational purposes only. It is not intended to provide medical advice or diagnosis. Users should consult with qualified healthcare professionals for any medical concerns or conditions.
