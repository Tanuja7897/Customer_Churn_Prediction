<div align="center">
 <img src="https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Visualizing_Data_Growth_Animation1-ezgif.com-video-to-gif-converter.gif" height="200" width="450">
</div>

![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)  ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)  ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)  ![Numpy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)  ![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)  ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge) 

---

## 📊 Customer Churn Prediction
This project focuses on predicting customer churn — determining whether a customer is likely to stay with the company or leave. Churn prediction is a critical business challenge, as retaining customers is often more cost-effective than acquiring new ones.

This solution is built using Python, Scikit-learn, and Pandas, and follows an industry-standard machine learning project structure. 
It covers the entire lifecycle of an ML project, from 📈Exploratory Data Analysis and data preprocessing to model training and evaluation.

By automating churn prediction, this project provides organizations with actionable insights to improve customer retention, optimize marketing strategies, and reduce revenue loss.

---

## 📚 Contents
 
- [Project Overview](#-Customer-Churn-Prediction)
- [Project Objective](#-Project-Objective)
- [Project Workflow](#-Project-Workflow)
- [Tech Stack](#-Tech-Stack)  
- [Project Structure](#-Repository-Structure)  
- [Dataset](#-DataSet)  
- [Installation](#️-Installation)  
- [Usage](#-Usage)  
  - [Train Model](#-Train-Model)  
  - [Predict on New Data](#Predict-New-Data)  
- [Example Output](#-Sample-output)  
- [Configuration](#-Configuration)
- [Future Improvements](#-Future-Improvements)  
- [Author](#-author)  

---


## 🎯 Project Objective

This project's objective is to build a robust, **end-to-end machine learning solution** for customer churn prediction. By leveraging comprehensive data analysis and a structured workflow, the goal is to provide a predictive tool that enables businesses to:

• Proactively engage with at-risk customers.

• Optimize marketing and retention campaigns for maximum effectiveness.

• Reduce churn rates and ensure long-term business growth.

<p align="right">
  <a href="#-Customer-Churn-Prediction">
    (back to top)
  </a>
</p>                                                                                                                           

                                                                                                                         
---



## 📈 Project Workflow

This flowchart illustrates the end-to-end process of the churn prediction pipeline, from raw data ingestion to result Prediction.

<div>
  <img src="https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Pipeline.png" alt="Project Pipeline Flowchart" height="600" width="450">
</div>

<p align="right">
  <a href="#-Project-Objective">
    (back to top)
  </a>
</p>


---


## 🛠️ Tech Stack

This project is built using a modern data science tech stack, following a modular and reproducible approach.

- ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white) for all scripting and model development
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)  ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) for efficient data manipulation and numerical operations
- ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) is used for building, training, and evaluating machine learning models
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-5D6B8C?style=for-the-badge&logo=matplotlib&logoColor=white)  ![Seaborn](https://img.shields.io/badge/Seaborn-466A90?style=for-the-badge&logo=seaborn&logoColor=white) for exploratory data analysis (EDA) and generating insightful plots
- ![Pipeline](https://img.shields.io/badge/Scikit--learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ensures that the workflow is easily configurable and scalable

<p align="right">
  <a href="#-Project-Objective">
    (back to top)
  </a>
</p>                                                                                                                         

---                                                                                                                          
## 📁 Repository Structure

```
Churn_Prediction/
│
├── data/                        # Raw dataset(s)
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/                      # Saved ML models
│   └── churn_model.pkl
│
├── src/                         # Source code
│   ├── preprocessing.py         # Preprocessing pipeline
│   ├── pipeline.py              # ML pipeline
│   ├── train.py                 # Train & validate
│   ├── evaluation.py            # Evaluation metrics
│   ├── model.py                 # Save/load model utils
│   └── predict.py               # Predict on new data
│
├── config.yaml                  # Config file
├── run_pipeline.py              # Entry point
├── requirements.txt             # Dependencies
└── README.md                    # Documentation
```
<p align="right">
  <a href="#-Tech-Stack">
    (back to top)
  </a>
</p> 

---

## 🛢️ DataSet

The project uses the Telco Customer Churn Dataset from Kaggle, which provides comprehensive information on a telecom company's customers.

* **Dataset:** Telco Customer Churn (IBM)
* **Source:** [🔗 Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Dimensions:** 7,043 rows and 21 features

👁️ Preview 
<div>
 <img src="https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Dataset.png" height="600" width="750">
</div>
<p align="right">
  <a href="#-Repository-Structure">
    (back to top)
  </a>
</p>


---

## ⚙ Installation
```
git clone https://github.com/Tanuja7897/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
```
<p align="right">
  <a href="#-DataSet">
    (back to top)
  </a>
</p>

---

## ⚡ Usage

🔹 Train Model

```
python run_pipeline.py
```
🔹 Predict New Data
```
from src.predict import predict_new_data
import pandas as pd

new_customer = pd.DataFrame([{
    "gender": "Female",
    "tenure": 5,
    "Contract": "Month-to-month",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 350.5
    #And All other Features
}])

print(predict_new_data(new_customer))
```
<p align="right">
  <a href="#-Installation">
    (back to top)
  </a>
</p>

---


## 💻 Sample Output

After running the pipeline, you will see the Classification Report and a Confusion Matrix of the model's predictions.

| Classification Reprot | Confusion Matrix |
| :--- | :--- |
| ![Model Evaluation Report](https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Repot.png) | ![Predictions Sample Output](https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Output.png) |


<p align="right">
  <a href="#-Usage">
    (back to top)
  </a>
</p>

---
## ⚙️ Configuration
The config.yaml file allows you to easily adjust project parameters without changing the code. You can FineTune parameters and Model for better Performance. 

<div>
 <img src="https://github.com/Tanuja7897/Customer_Churn_Prediction/blob/main/assets/Yml.png" height="250" width="750">
</div>

<p align="right">
  <a href="#-Sample-Output">
    (back to top)
  </a>
</p>

---
🔮 Future Improvements

* **Hyperparameter Tuning:** Implement automated hyperparameter optimization using tools like Optuna or GridSearch to further improve model performance.
* **Version Control:** Integrate MLflow or DVC to manage and track different versions of the model and data, ensuring reproducibility.
* **CI/CD Pipeline:** Set up GitHub Actions for a continuous integration and continuous deployment pipeline to automate testing and deployment workflows.

<p align="right">
  <a href="#-Configuration">
    (back to top)
  </a>
</p>

---

👨‍💻 Author
* Tanuja Vishwakarma
* [GitHub](https://github.com/Tanuja7897)
* [LinkedIn](https://www.linkedin.com/in/tanuja-vishwakarma-463579253/)

<p align="right">
  <a href="#-Customer-Churn-Prediction">
    (back to top)
  </a>
</p>
