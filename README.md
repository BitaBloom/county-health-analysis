# 📊 Analysis of 2018 County Health Rankings Data

## Overview
This project analyzes the 2018 County Health Rankings dataset to uncover significant factors influencing health outcomes across various counties in the United States. Using machine learning (linear regression), the project highlights relationships between health factors and outcomes.

Key outputs:
- Correlation heatmap of health-related factors.
- Pairwise relationship visualizations (pairplot).
- Prediction of health outcomes using a trained regression model.

---

## 📁 Project Structure
```
county-health-analysis/
🔸
├── code/                    # Code files for the project
│   └── code.py              # Main Python script
│
├── data/                    # Dataset files
│   └── data.xlsx  # Source data
│
├── reports/                 # Project documentation
│   └── report.pdf           # Detailed project report
│
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and instructions
```

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- **Python** (v3.8 or higher). Download from [python.org](https://www.python.org/downloads/).

### 2. Virtual Environment
Set up a virtual environment to manage dependencies:
- **Windows**:
  ```bash
  python -m venv myenv
  myenv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Program
1. Place the dataset file (`2018 County Health Rankings Data.xlsx`) in the `data/` folder.
2. Execute the `code.py` script:
```bash
python code/code.py
```

---

## 🖋️ Results
- **Correlation Heatmap**: Visualizes relationships between health-related factors.
- **Pairplot**: Pairwise feature relationships.
- **Actual vs Predicted Scatter Plot**: Evaluates regression model performance.
- **Mean Squared Error (MSE)**: Reflects model accuracy.

---

## 📝 Documentation
- **Report**: See the detailed project report in the `reports/` folder.

---

## 🛠️ Troubleshooting
- Ensure all required files are in the correct folders (`code/`, `data/`, etc.).
- Missing dependencies? Run:
```bash
pip install -r requirements.txt
```
- Issues with the dataset? Ensure it's named correctly: `data.xlsx`.

---

## 💡 Future Work
- Experiment with advanced machine learning models.
- Incorporate additional datasets for a comprehensive analysis.

---

## 👩‍💻 Author
**Bita Nasserfarahmand**  
- [Email](mailto:bita.nf@gmail.com)  
- [LinkedIn](https://linkedin.com/in/bita-farahmand-58363a232/)

Feel free to contribute or reach out with questions!
