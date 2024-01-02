from flask import Flask, render_template, request, redirect, url_for, send_file,session
import requests
import json
import pdfkit
from roboflow import Roboflow
import os
from PIL import Image
import easyocr
import cv2
import pandas as pd
import re
from matplotlib import pyplot as plt
import subprocess
from ultralytics import YOLO
import warnings
warnings.filterwarnings('ignore')
import pytesseract
from io import StringIO
import sys



pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nirma\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


reader = easyocr.Reader(['en'])

app = Flask(__name__)
def image_proc(image_path,pred_json):
    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
        # load the image
    img = cv2.imread(image_path)
    im=Image.open(image_path)
    # Initialize an empty dataframe to store the results
    df = pd.DataFrame(columns=['name', 'text'])
    

    # Process each prediction from RCNN
    for pred in pred_json['predictions']:
        # Crop the image based on the object coordinates
        x, y, w, h = float(pred['x']), float(pred['y']), float(pred['width']), float(pred['height'])
        #print(x,y,w,h)
        #cropped_img = img[y:h+y, x:w+x]
    #     img_res = im.crop((x, y, x+w, y+h)) 
    #     img_res.show() 
        roi_x = int(x - w / 2)
        roi_y = int(y - h / 2)
        roi_width = int(w)+50
        roi_height = int(h)
        cropped_img = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
        # plt.imshow(cropped_img)
        # plt.axis("off")
        # plt.show()
        #cv2.imshow('ImageWindow', cropped_img)
        #cv2.waitKey(0)
        
        # Perform OCR using Tesseract on the cropped image
        if pred['class'] in ['name', 'sex']:
            output = reader.readtext(cropped_img,detail=0)
            print("out",output)
            text=str(output[0])
        else:
            output = reader.readtext(cropped_img,detail=0)

        # Extract numeric information for classes other than 'name' and 'sex'
        if pred['class'] not in ['name', 'sex','age']:
            numeric_values = [value for value in output if is_numeric(value)]
            #text = ' '.join(numeric_values)
            print(numeric_values)
            text=numeric_values[0]
        if pred['class'] in ['age']:
            numeric_values = [extract_numeric_info(value) for value in output]
            text = ' '.join(numeric_values)

        # Add the name and extracted text to the dataframe
        df2=pd.DataFrame({'name': [pred['class']], 'text': [text]})
        df=pd.concat([df,df2],ignore_index=True)
        #df = df.append({'name': pred['class'], 'text': text}, ignore_index=True)
        #df.loc[len(df)] = {'name': pred['class'], 'text': text}
        #print(output)
       
        # and return the output
    print(df)
    return df
# Function to pass the image to the Roboflow API
def pass_to_roboflow(image_path):
    # Implement the logic to pass the image to the Roboflow API
    rf = Roboflow(api_key="DWr88H9uUstVlVubbYIQ")
    project = rf.workspace().project("medi-9sqs7")
    model = project.version(1).model
    pred_json=model.predict(image_path, confidence=40, overlap=30).json()
        # visualize your prediction
    model.predict(image_path, confidence=40, overlap=30).save("static/prediction.jpg")
    return pred_json
    

def pass_to_yolo(image_path):
    # Run the YOLO detection command
    print("going inside yolo")
    command = command = f"yolo task=detect mode=predict model=best.pt conf=0.3 source={image_path} project=static save=True"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check if the command was executed successfully
    if result.returncode == 0:
        output = result.stdout
        print("running sucessfully!")
        return output
    else:
        print("Error running YOLO detection command.")
        return None
    
def extract_numeric_info(text):
    return re.sub(r'[^\d.]+', '', text)

# Function to check if a string is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function for report generation
def generate_report(df):
    # Implement the logic for report generation based on the output
    #item.loc[len(item.index)] = ['Mr. Neeraj Ohja',"Male",27,4.20,5.79,50.3,39.6,245.0,12] 
    report=""
    new_df = pd.DataFrame(data=df.iloc[:, 1].values.reshape(1, -1), columns=df.iloc[:, 0].values)
    print(new_df)
    item=new_df
    new_column_order = ["name","sex","age","wbc","rbc","lymp","neutro","plate","hb"]
    item=item.reindex(columns=new_column_order)
    print(item)

    #item=pd.DataFrame(columns=["name","sex","age","wbc","rbc","lymp","neutro","plate","hb"])
    #item.loc[len(item.index)] =['Mr. Neeraj Ohja',"Male",27,4.20,5.79,50.3,39.6,245.0,12]
#     item.loc[len(item.index)] = [
#         df.loc[df['name'] == "name", 'text'].iloc[0],
#         df.loc[df['name'] == "sex", 'text'].iloc[0],
#         df.loc[df['name'] == "wbc", 'text'].iloc[0],
#         df.loc[df['name'] == "rbc", 'text'].iloc[0],
#         df.loc[df['name'] == "lymp", 'text'].iloc[0],
#         df.loc[df['name'] == "neutro", 'text'].iloc[0],
#         df.loc[df['name'] == "plate", 'text'].iloc[0],
#         df.loc[df['name'] == "hb", 'text'].iloc[0],
#         df.loc[df['name'] == "age", 'text'].iloc[0]
# ]

    cols=["name","sex","age","wbc","rbc","lymp","neutro","plate","hb"]
    cols_dict={"name":"Name","sex":"Sex","age":"Age","wbc":"WBC","rbc":"RBC","lymp":"Lymphocyte","neutro":"Neutrophil","plate":"Platelet","hb":"Haemoglobin"}

    report = report + "\n" +("----------------------------------------------------------------------Generated Report----------------------------------------------------------------------\n\n")
    report = report + "\n" +("------------------------------------------------------------------------------------------------------------------------------------------------------------\nGENERAL INFORMATION\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    report = report + "\n" +("Name: "+item['name'][0])
    report = report + "\n" +("Sex: "+item['sex'][0])
    report = report + "\n" +("Age: "+str(item['age'][0]))
    #report = report + "\n" +(ord(item['age'][0]))

    #------- UNIT CORRECTIONS ----- !!!!!!!!
    if(float(item['wbc'][0])>900):
        item['wbc'][0]=float(item['wbc'][0])/1000
    if(float(item['plate'][0])<15):
        item['plate'][0]=float(item['plate'][0])*100
    if(float(item['plate'][0])>50000):
        item['plate'][0]=float(item['plate'][0])/1000
    #-------------------------- !!!!!!!!!!!!!!!!!!

    if(int(item['age'][0])>=0 and int(item['age'][0])<=10):
        n=pd.read_excel("report_generation/normal_1.xlsx")
        report = report + "\n" +("Age Group: Child (0-10 years old)\n")
    elif(int(item['age'][0])>10 and int(item['age'][0])<=18):
        n=pd.read_excel("report_generation/normal_2.xlsx")
        report = report + "\n" +("Age Group: Adolescent (10-18 years old)\n")
        if(str(item["sex"][0])==str("Male")):
            n['hb'][0]=18
            n['hb'][1]=14
            n['rbc'][0]=5.9
            n['rbc'][1]=4
        if(str(item["sex"][0])==str("Female")):
            n['hb'][0]=16
            n['hb'][1]=12
            n['rbc'][0]=5.2
            n['rbc'][1]=3.8
    elif(int(item['age'][0])>18 and int(item['age'][0])<=50):
        n=pd.read_excel("report_generation/normal_3.xlsx")
        report = report + "\n" +("Age Group: Adult (18-50 years old)\n")
        if(str(item["sex"][0])==str("Male")):
            n['hb'][0]=18
            n['hb'][1]=14
            n['rbc'][0]=5.9
            n['rbc'][1]=4
        if(str(item["sex"][0])==str("Female")):
            n['hb'][0]=16
            n['hb'][1]=12
            n['rbc'][0]=5.2
            n['rbc'][1]=3.8
    elif(int(item['age'][0])>50):
        n=pd.read_excel("report_generation/normal_4.xlsx")
        report = report + "\n" +("Age Group: Elderly (50+ years old)\n")




    report = report + "\n" +("------------------------------------------------------------------------------------------------------------------------------------------------------------\nALL RESULTS\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    count = 0
    for i in cols[3:]:
        if float(item[str(i)][0]) > n[str(i)][0]:
            report = report + "\n" + ((str(cols_dict.get(i))).upper() + " Level: "+ "HIGH")
        elif float(item[str(i)][0]) <= n[str(i)][0] and float(item[str(i)][0]) >= n[str(i)][1]:
            report = report + "\n" + ((str(cols_dict.get(i))).upper() + " Level: Normal")
        elif float(item[str(i)][0]) < n[str(i)][1]:
            report = report + "\n" + ((str(cols_dict.get(i))).upper() + " Level: "+ "LOW")

    report = report + "\n" + (
        "\n------------------------------------------------------------------------------------------------------------------------------------------------------------\nDETAILED REPORT OF ABNORMAL RESULTS\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    count = 1

    for i in cols[3:]:
        if float(item[str(i)][0]) > n[str(i)][0]:
            report = report + "\n" + (str(count) + ". ")
            count = count + 1
            perc = str(round(((float(item[str(i)][0]) - n[str(i)][0]) / n[str(i)][0]) * 100, 2))
            report = report + "\n" + (
                str(cols_dict.get(i)).upper() + " Level:\n - " + perc + " % HIGHER than normal")
            if float(perc) <= 10:
                report = report + "\n" + (" - MILD deviation from normal range")
            elif float(perc) > 10:
                report = report + "\n" + (" - !! Significant deviation from normal range")
            report = report + "\n" + ( "\nPotential Causes: (Common causes are listed first)\n" +   n[str(i)][2] + "\n")
            report = report + "\n" + ( "\nSuggestions:\n" +   n[str(i)][4] + "\n------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        elif float(item[str(i)][0]) < n[str(i)][1]:
            report = report + "\n" + (str(count) + ".")
            count = count + 1
            perc = str(round(((n[str(i)][1] - float(item[str(i)][0])) / n[str(i)][1]) * 100, 2))
            report = report + "\n" + (
                str(cols_dict.get(i)).upper() + " Level:\n - " + perc + " % LOWER than normal")
            if float(perc) <= 10:
                report = report + "\n" + (" - MILD deviation from normal range")
            elif float(perc) > 10:
                report = report + "\n" + (" - !! Significant deviation from normal range")
            report = report + "\n" + ( "\nPotential Causes: (Common causes are listed first)\n" +   n[str(i)][3] + "\n")
            report = report + "\n"


    buffer = StringIO()
    sys.stdout = buffer
    print(report)
    print_output = buffer.getvalue()
    
    return print_output

# Function for PDF creation
def create_pdf(report):
    # Set up the options for PDF generation
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    # Generate a temporary HTML file with the text content
    html = f'<html><body><pre>{report}</pre></body></html>'
    temp_html_file = 'tmp/temp_html_file.html'
    with open(temp_html_file, 'w') as file:
        file.write(html)

    # Generate the PDF using the temporary HTML file
    pdf_path = 'tmp/report.pdf'
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    pdfkit.from_file(temp_html_file, pdf_path, options=options, configuration=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf))

    return pdf_path
    # Implement the logic to create a PDF based on the report

def get_latest_image_path():
    filesz=os.listdir("static")
    m=-1
    
    for file in filesz:
        if not os.path.isdir(f"static/{file}"):
            continue
        a,b=file.split("predict")

        if b=='':
            continue
        else:
            m=max(int(b),m)
    return f"predict{m}/uploaded_image.jpg"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded image file from the request
        image_file = request.files['image']
        
        # Save the image file to a temporary location
        image_path = 'tmp/uploaded_image.jpg'
        image_file.save(image_path)

        # Pass the image to the Roboflow API
        output = pass_to_roboflow(image_path)

        yolo = get_latest_image_path()#saves the latest path were predicted images will be saved
        output_yolo= pass_to_yolo(image_path)

        ocr_output=image_proc(image_path,output)

        # # Add an extra column to the dataframe
        # ocr_output['unit'] = ''

        # # Convert the dataframe to JSON for easier handling in JavaScript
        # df_json = ocr_output.to_json(orient='records')

        # # Pass the dataframe JSON to the template for rendering
        # return render_template('edit_table.html', data=df_json)
        # # Pass the dataframe to the template for rendering
        # return render_template('edit_table.html', data=ocr_output.to_html(index=False))    

        # Generate report
        report = generate_report(ocr_output)

        # Create a PDF
        pdf_path = create_pdf(report)


        # Render the result page with the PDF path
        return render_template('result.html', pdf_path=pdf_path, image_path=image_path,yolo=yolo)

    return render_template('index.html')

@app.route('/image/<path:filename>')
def get_image(filename):
    return send_file('/tmp/' + filename, mimetype='image/jpg')


@app.route('/save', methods=['POST'])
def save():
    # Retrieve the edited dataframe from the form submission
    edited_data = {}
    for key, value in request.form.items():
        edited_data[int(key)] = value

    # Create a new dataframe to store the edited values
    edited_df =pd.DataFrame(columns=['name', 'text','unit'])

    # Update the new dataframe with the edited values
    for index, value in edited_data.items():
        edited_df.iloc[index] = value
    
    image_path = 'tmp/uploaded_image.jpg'
    # # Retrieve the edited dataframe from the form submission
    # edited_data = request.form.to_dict(flat=False)

    # # Convert the edited data back to a dataframe
    # edited_df = pd.DataFrame.from_dict(edited_data)

    # # Update the values of the new column
    # edited_df['unit'] = request.form.getlist('unit')

    # # Perform any necessary data cleaning or validation here

    # # Save the edited dataframe back to the original CSV file
    # edited_df.to_csv('your_dataframe.csv', index=False)


    # Generate report
    report = generate_report(edited_df)

    # Create a PDF
    pdf_path = create_pdf(report)

    # Render the result page with the PDF path
    return render_template('result.html', pdf_path=pdf_path, image_path=image_path)

@app.route('/download_pdf')
def download_pdf():
    pdf_path = request.args.get('pdf_path')
    return send_file(pdf_path, as_attachment=True)



if __name__ == '__main__':
    app.run()