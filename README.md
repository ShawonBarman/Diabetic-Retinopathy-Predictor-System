# Diabetic-Retinopathy-Predictor-System

<p>Diabetic Retinopathy Predictor System is Django-based web application designed to assist users in predicting the likelihood of developing diabetes-related complications, specifically the presence of diabetic retinopathy (damage to the eyes due to diabetes). The project utilizes machine learning techniques to make predictions based on user-provided health and lifestyle information. Here's an overview of the project:</p>

<ol>
  <li><strong>Data Source:</strong>
    <ul>
      <li>The project collects diabetes-related data from the <a href="https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Questionnaire&Cycle=2017-2020">CDC NHANES website</a>. This data serves as the basis for training the machine learning model.</li>
    </ul>
  </li>
  <li><strong>Project Structure:</strong>
    <ul>
      <li>The project is organized into three main folders and two files:
        <ul>
          <li>'dataset_and_machine_learning_files': Contains the dataset ('data.csv') and machine learning code ('Diabetes_affected_eyes_had_retinopathy.ipynb').</li>
          <li>'healthFitness' (Main App): Contains the Django application's settings, URLs, and other configurations.</li>
          <li>'myApp' (Another App): Contains models, views, URLs, and other components for handling user interactions and predictions.</li>
          <li>'db.sqlite3': The SQLite database used by the Django application.</li>
          <li>'manage.py': Django management script.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><strong>Machine Learning Model:</strong>
    <ul>
      <li>The heart of the system is a machine learning model for diabetes prediction. The model is trained using the provided dataset and is loaded into the Django application using joblib.</li>
    </ul>
  </li>
  <li><strong>User Interface:</strong>
    <ul>
      <li>The web interface is designed using HTML templates extended from a base template ('base.html') that includes Bootstrap for styling.</li>
      <li>The main user interface ('index.html') offers a form where users can input various health and lifestyle-related parameters.</li>
    </ul>
  </li>
  <li><strong>Prediction Process:</strong>
    <ul>
      <li>Users provide information such as alcohol consumption, smoking habits, BMI, sleep patterns, and more via the form.</li>
      <li>When the user submits the form, the data is sent to the Django backend for processing.</li>
      <li>The input data is converted into a feature vector and passed to the machine learning model.</li>
      <li>The model makes predictions about whether the user is likely to have diabetic retinopathy based on the provided information.</li>
      <li>The prediction result is displayed on the web page.</li>
    </ul>
  </li>
  <li><strong>Result Presentation:</strong>
    <ul>
      <li>The prediction result is presented as a message indicating whether the user is predicted to be at risk for diabetic retinopathy.</li>
    </ul>
  </li>
  <li><strong>Project Workflow:</strong>
    <ul>
      <li>The user accesses the application's home page, where they find a form for inputting health-related data.</li>
      <li>After submitting the form, the user receives an instant prediction regarding diabetic retinopathy risk.</li>
    </ul>
  </li>
  <li><strong>Technology Stack:</strong>
    <ul>
      <li>Django: A Python web framework for building web applications.</li>
      <li>Joblib: Used to load the pre-trained machine learning model.</li>
      <li>HTML/CSS: For creating the user interface.</li>
      <li>Bootstrap: For styling the web pages.</li>
    </ul>
  </li>
  <li><strong>Use Case:</strong>
    <ul>
      <li>This project can be valuable for individuals interested in assessing their risk of developing diabetic retinopathy based on their health and lifestyle choices. It can serve as an early warning system, encouraging users to adopt healthier habits and consult healthcare professionals if necessary.</li>
    </ul>
  </li>
</ol>

<p>The Diabetic Retinopathy Predictor System with Django offers a user-friendly platform for individuals to gain insights into their diabetes-related health risks and make informed decisions about their well-being. It showcases the integration of machine learning into a web application for predictive healthcare analysis.</p>

<h3> Here are step-by-step instructions on how to run this Django-based Diabetic Retinopathy Predictor System in a user-friendly way:</h3>

<ol>
  <li><strong>Download the Project from GitHub and Unzip:</strong> Look for a "Code" button on this GitHub page. Click on it and select "Download ZIP" to download the project as a ZIP archive. And then locate the downloaded ZIP file on your computer (usually in your "Downloads" folder). After that right-click the ZIP file and select "Extract" or "Extract All" (the exact option may vary depending on your operating system). Then choose a destination folder where you want to extract the project files.</li>
  <li><strong>Navigate to Project Directory:</strong> Open the command prompt or terminal in this project root directory directly. Or open the command prompt or terminal on your computer and then use the 'cd' command to navigate to the root directory of this Django project. For example:
  <ul>
    <li>cd path/to/this/project</li>
  </ul>
  </li>
  <li><strong>Create a Virtual Environment:</strong> Create a virtual environment to isolate this project dependencies. This helps manage package versions.
  <ul>
    <li>python -m venv myenv</li>
  </ul>
  </li>
  <li><strong>Activate the Virtual Environment:</strong> Activate the virtual environment you just created. This ensures that the project uses the isolated environment.
  <ul>
    <li>myenv\Scripts\activate   (Windows)</li>
    <li>source myenv/bin/activate   (macOS/Linux)</li>
  </ul>
  </li>
  <li><strong>Upgrade Pip:</strong> Upgrade the 'pip' tool to the latest version to ensure you have the most recent package manager.
  <ul>
    <li>python.exe -m pip install --upgrade pip</li>
  </ul>
  </li>
  <li><strong>Install Django and Required Packages:</strong> Install Django and the necessary Python packages for this project.
  <ul>
    <li>pip install django</li>
    <li>pip install numpy</li>
    <li>pip install pandas</li>
    <li>pip install joblib</li>
    <li>pip install scikit-learn==1.2.2</li>
  </ul>
  </li>
  <li><strong>Database Setup:</strong> Run the following commands to set up the database for this Django project:
  <ul>
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
  </ul>
  </li>
  <li><strong>Run the Development Server:</strong> Start the Django development server to run this project locally:
  <ul>
    <li>python manage.py runserver</li>
  </ul>
  </li>
  <li><strong>Access This Project:</strong> After launching the server, simply open your web browser and navigate to 'http://localhost:8000/'. This will take you to the home page of our Diabetes Risk Predictor.</li>
<li><strong>Interact with the Prediction System:</strong> On the home page, you can enter your health and lifestyle information, and upon clicking the "Predict" button, you'll receive an instant assessment of your risk for diabetic retinopathy based on the provided data.</li>
</ol>
