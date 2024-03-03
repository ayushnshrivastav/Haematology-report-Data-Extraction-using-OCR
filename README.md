**Blood Report Analysis Application**

This repository contains the source code for a web application designed to analyze blood reports uploaded by users. The application utilizes OCR (Optical Character Recognition) technology to extract relevant information from the reports, such as name, age, sex, and various blood parameters. Subsequently, a rule-based algorithm assesses the extracted values to determine if they fall within normal ranges. If any values are found to be abnormal, the algorithm provides insights into the extent of deviation, potential causes, and suggestions for normalization.



**Features**:

  1. OCR Integration: Utilizes OCR technology, including Roboflow, YoloV8, easyOCR, and pytesseract, to extract information from blood reports.
  2. Rule-based Analysis: Analyzes extracted values to determine if they are within normal ranges.
  3. Abnormality Detection: Identifies and reports abnormalities in blood parameters.
  4. Detailed Insights: Provides percentage deviation, potential causes, and suggestions for abnormal values.
  5. Sensitive Data Handling: Ensures confidentiality and security by processing sensitive data within the application.



**Installation**:

1.Clone the repository:

  git clone (https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR.git)
  
2. Install dependencies:

  pip install -r requirements.txt

3. Run the Flask application:

  flask run


  
**Usage**:

  1. Upload Blood Report: Users can upload their blood reports via the web interface.
  2. Report Analysis: The application automatically extracts relevant information from the report and analyzes the blood parameters.
  3. Abnormality Detection: If any values are found to be abnormal, the application provides detailed insights into the deviation and potential causes.
  4. Suggestions for Normalization: Users receive suggestions on how to normalize abnormal blood parameters.



**Required Links:**

- Roboflow Project: Roboflow Project
- YoloV8 Model: [YoloV8 Model](https://github.com/ultralytics/ultralytics.git)
- Flask Documentation: [Flask Documentation](https://github.com/topics/flask)
- LabelImg Tool: [LabelImg Tool](https://github.com/topics/labelimg)


  
**Images:**

Images of blood reports might be required for testing purposes.



**Disclaimer:**

Please note that this application is for educational and informational purposes only. It is not intended to provide medical advice or diagnosis. Users should consult with qualified healthcare professionals for any medical concerns or conditions.
