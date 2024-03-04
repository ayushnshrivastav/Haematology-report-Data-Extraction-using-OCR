**Blood Report Analysis Application**

This repository contains the source code for a web application designed to analyze blood reports uploaded by users. The application utilizes OCR (Optical Character Recognition) technology to extract relevant information from the reports, such as name, age, sex, and various blood parameters. Subsequently, a rule-based algorithm assesses the extracted values to determine if they fall within normal ranges. If any values are found to be abnormal, the algorithm provides insights into the extent of deviation, potential causes, and suggestions for normalization.



**Features**:

  1. OCR Integration: Utilizes OCR technology, including Roboflow, YoloV8, easyOCR, and pytesseract, to extract information from blood reports.
  2. Rule-based Analysis: Analyzes extracted values to determine if they are within normal ranges.
  3. Abnormality Detection: Identifies and reports abnormalities in blood parameters.
  4. Detailed Insights: Provides percentage deviation, potential causes, and suggestions for abnormal values.
  5. Sensitive Data Handling: Ensures confidentiality and security by processing sensitive data within the application.


**System Design:**

Roles:
1. Developer:
   a.Data Gathering: Acquiring relevant datasets for training and testing the OCR and machine learning models. This involves collecting blood report samples from various sources, including the internet and
     local hospitals.
   b. Data Processing and Annotatio: Preprocessing the collected data to ensure consistency, cleanliness, and compatibility with the training pipeline. This step involves tasks such as data cleaning, data              augmentation  and data annotation to enhance the quality and diversity of the dataset.
   c. Model Training: Developing and training machine learning models, including YoloV8, easyOCR, pytesseract, Roboflow and rule based algorithm to perform tasks such as object detection and classification of          blood parameters.
   d. Model Evaluation: Assessing the performance of trained models using appropriate metrics and validation techniques. This involves testing the models on unseen data to measure their accuracy, precision,            recall, and other relevant metrics.
3. User: The user interacts with the application through the web interface to upload their blood reports and obtain insights into their health status.
   a. Uploads the Report: The user uploads their blood report via the web application, providing the necessary input data for analysis.
    UI: ![image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/255eaf67-4b59-44d1-b859-ed5d3674d548)
    Report: ![uploaded_image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/73d22742-9ac3-4e71-bb01-f1054cb27bac)
  
   b. Views Predicted Probabilities of Diseases: After the analysis is performed, the user can view the predicted probabilities of diseases or abnormalities detected in their blood report. This information 
      helps the user understand their health condition and potential risks.
      OCR results: ![uploaded_image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/8935b51a-9581-404c-800e-3808c84e75a1)
      Generated report for User:![image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/3159f762-f02b-4bce-8052-e7afe35109e7)
       ![image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/0920df11-385a-403a-b991-a6ab08cd6e6d)  
       

   c. Consumes Suggestions: Based on the analysis results, the user receives personalized suggestions or recommendations for maintaining or improving their health. These suggestions includes lifestyle changes,         dietary modifications, or medical interventions to address any identified health issues.
       ![image](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/8e1c5620-5057-4689-b69d-a16bdefa6986)

Use case diagram 
![capstone use case](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/ece075a7-7017-4d1b-adc3-e2f32873cb19)

Process Flow:

1. Model Training:

    a. Report Collection: Collecting reports from the internet and local hospitals.
    b. Report Selection: Selecting the most consistent report format.
    c. Data Augmentation: Augmenting data to improve model performance.
    d. Annotation for OCR: Annotating data for OCR (Optical Character Recognition).
    e. Training CNN Model: Training Convolutional Neural Network model.
    f. Testing Model: Evaluating model performance.
    g. Saving and Using Best Performance Model: Saving the best-performing model for deployment.

2. Data Extraction:

    1. Object Detection: Detecting required texts in the reports.
    b. Image Processing: Segmenting images of separate objects.
    c. OCR: Extracting text from segments using OCR techniques.

3. User Interface: Web Application:

    a. Uploading of Blood Report: User uploads blood report via the web application.
    b. Hematological Report Generation: Generated hematological report is downloadable.

4. Report Generated:

  a. Calculations: Identifying abnormal values and calculating deviations considering age and sex.
  b. Cause and Solutions/Suggestions: Research-based likely causes and suggestions provided for abnormal values.

Process flow Diagram:
![uml_capstone-BlockDiagram (1)](https://github.com/ayushnshrivastav/Haematology-report-Data-Extraction-using-OCR/assets/71760784/7b1399d9-46ed-4e24-8039-e525cd41d972)


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
