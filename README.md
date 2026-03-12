# AI-Data-Analyst-Intern
AI powered automated data analysis tool that performs EDA, visualization, data quality checks and generates automated insights.
# 🤖 AI Data Analyst Intern

An **AI-powered automated data analysis tool** built using **Python and Streamlit** that performs exploratory data analysis (EDA), generates smart visualizations, detects data quality issues, and produces automated insights from uploaded datasets.

This project simulates the work of a **Data Analyst Intern**, helping users quickly understand their datasets without manually writing analysis code.

---

# 🚀 Features

### 📊 Automated Dataset Analysis

* Displays dataset preview
* Shows dataset shape and column names
* Detects data types
* Identifies missing values
* Generates statistical summaries

### 📈 Smart Visualization Engine

The application automatically decides the **best chart type** depending on the dataset.

Examples:

* **Histogram** for numeric distributions
* **Pie charts** for small categorical distributions
* **Bar charts** for larger categorical datasets
* **Scatter plots** for relationships between numeric variables
* **Correlation heatmap** for understanding feature relationships

This removes the need for the user to manually choose visualization types.

---

### 🧹 Data Cleaning Suggestions

The tool automatically detects common data quality issues such as:

* Missing values
* Duplicate rows
* High-cardinality categorical columns
* Potential outliers

It also provides **recommended cleaning methods** such as:

* Mean / median imputation
* Mode replacement
* Removing duplicates
* Treating outliers

---

### 🤖 Automated AI Insights

The system generates **automated insights** about the dataset, including:

* Dataset size summary
* Missing value observations
* Duplicate detection
* Strongest feature correlations
* Most frequent categorical values

---

### 📄 Downloadable Analysis Report

Users can download a **text-based AI-generated analysis report** summarizing the dataset findings.

---

### 📂 Large Dataset Support

The application supports **large dataset uploads up to 500MB+** by modifying the Streamlit configuration.

This allows the tool to analyze significantly larger datasets than the default Streamlit limit.

---

# 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Matplotlib**
* **Seaborn**

---

# 📁 Project Structure

```
AI-Data-Analyst-Intern
│
├── app.py
├── requirements.txt
├── .gitignore
└── .streamlit
```

---

# ⚙️ Installation & Running the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/rawatabhishek2909-blip/AI-Data-Analyst-Intern.git
```

### 2️⃣ Navigate into the project

```
cd AI-Data-Analyst-Intern
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
streamlit run app.py
```

The app will open in your browser.

---

# 🎯 Use Cases

* Quick dataset exploration
* Automated exploratory data analysis (EDA)
* Data cleaning guidance
* Data visualization automation
* Beginner-friendly AI data analysis assistant

---

# 📌 Future Improvements

Possible future upgrades include:

* Natural language dataset queries
* LLM-powered insights generation
* Automated feature importance detection
* Interactive dashboard analytics
* Cloud deployment

---

# 👨‍💻 Author

**Abhishek Rawat**

Aspiring **Data Analyst** interested in building AI-powered data tools and analytics systems.

---

## 🌐 Live Application

Try the live application here:

https://ai-data-analyst-intern.streamlit.app/

----

# ⭐ If you like this project

Consider giving it a **star ⭐ on GitHub**.
