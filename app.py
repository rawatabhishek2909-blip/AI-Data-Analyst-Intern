import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("AI Data Analyst Intern")

st.write("Upload a CSV dataset and the AI will analyze it automatically.")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # -------------------------
    # DATASET OVERVIEW
    # -------------------------

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Column Names")
    st.write(df.columns)

    st.subheader("Data Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    # -------------------------
    # AUTOMATED INSIGHTS
    # -------------------------

    st.subheader("Automated Insights")

    st.write(
        f"The dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**."
    )

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) > 0:
        st.write("Columns with missing values:")
        st.write(missing)
    else:
        st.write("No missing values detected.")

    # -------------------------
    # SMART VISUALIZATIONS
    # -------------------------

    st.subheader("Smart Visualizations")

    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    # Numeric distributions
    if len(numeric_columns) > 0:

        st.write("### Numeric Data Distribution")

        for col in numeric_columns:

            fig, ax = plt.subplots()

            sns.histplot(df[col], kde=True, ax=ax)

            ax.set_title(f"Distribution of {col}")

            st.pyplot(fig)

    # Categorical distributions
    if len(categorical_columns) > 0:

        st.write("### Categorical Data Distribution")

        for col in categorical_columns:

            value_counts = df[col].value_counts()

            fig, ax = plt.subplots()

            if len(value_counts) <= 5:

                ax.pie(
                    value_counts,
                    labels=value_counts.index,
                    autopct='%1.1f%%'
                )

                ax.set_title(f"{col} Distribution (Pie Chart)")

            else:

                value_counts.plot(kind="bar", ax=ax)

                ax.set_title(f"{col} Distribution (Bar Chart)")

            st.pyplot(fig)

    # Scatter plot
    if len(numeric_columns) >= 2:

        st.write("### Relationship Between Numeric Variables")

        col1 = numeric_columns[0]
        col2 = numeric_columns[1]

        fig, ax = plt.subplots()

        sns.scatterplot(
            x=df[col1],
            y=df[col2],
            ax=ax
        )

        ax.set_title(f"{col1} vs {col2}")

        st.pyplot(fig)

    # Correlation heatmap
    if len(numeric_columns) > 1:

        st.write("### Correlation Heatmap")

        corr = df[numeric_columns].corr()

        fig, ax = plt.subplots()

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)

    # -------------------------
    # CATEGORICAL COLUMN ANALYSIS
    # -------------------------

    st.subheader("Categorical Column Analysis")

    if len(categorical_columns) > 0:

        selected_cat = st.selectbox(
            "Select categorical column",
            categorical_columns
        )

        value_counts = df[selected_cat].value_counts()

        st.write("Value Counts:")
        st.write(value_counts)

        fig, ax = plt.subplots()

        value_counts.plot(kind="bar", ax=ax)

        st.pyplot(fig)

    else:

        st.write("No categorical columns found.")

    # -------------------------
    # DATA CLEANING SUGGESTIONS
    # -------------------------

    st.subheader("Data Cleaning Suggestions")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) > 0:

        st.write("⚠ Columns with missing values detected:")

        for col in missing.index:

            st.write(f"- **{col}** has {missing[col]} missing values.")

            if df[col].dtype in ['int64', 'float64']:

                st.write(
                    "Suggestion: Fill missing values using **mean or median**."
                )

            else:

                st.write(
                    "Suggestion: Fill missing values using **mode or 'Unknown'**."
                )

    else:

        st.write("✅ No missing values detected.")

    duplicates = df.duplicated().sum()

    if duplicates > 0:

        st.write(f"⚠ The dataset contains **{duplicates} duplicate rows**.")

        st.write(
            "Suggestion: Consider removing duplicates using `drop_duplicates()`."
        )

    else:

        st.write("✅ No duplicate rows found.")

    for col in categorical_columns:

        unique_values = df[col].nunique()

        if unique_values > 20:

            st.write(
                f"⚠ Column **{col}** has high cardinality ({unique_values} unique values)."
            )

            st.write(
                "Suggestion: Consider grouping rare categories."
            )

    for col in numeric_columns:

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        if len(outliers) > 0:

            st.write(
                f"⚠ Column **{col}** may contain outliers ({len(outliers)} detected)."
            )

            st.write(
                "Suggestion: Consider outlier treatment."
            )

    # -------------------------
    # AI GENERATED REPORT
    # -------------------------

    st.subheader("AI Generated Data Analysis Report")

    report = []

    report.append(
        f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
    )

    missing_cols = df.columns[df.isnull().any()]

    if len(missing_cols) > 0:

        report.append(
            "The following columns contain missing values: "
            + ", ".join(missing_cols)
            + "."
        )

    else:

        report.append(
            "No missing values were detected in the dataset."
        )

    duplicates = df.duplicated().sum()

    if duplicates > 0:

        report.append(
            f"The dataset contains {duplicates} duplicate rows."
        )

    if len(numeric_columns) > 1:

        corr_matrix = df[numeric_columns].corr()

        corr_pairs = corr_matrix.unstack()

        corr_pairs = corr_pairs[corr_pairs != 1]

        strongest_corr = corr_pairs.abs().idxmax()

        corr_value = corr_pairs[strongest_corr]

        report.append(
            f"The strongest relationship exists between {strongest_corr[0]} "
            f"and {strongest_corr[1]} with correlation value {corr_value:.2f}."
        )

    if len(categorical_columns) > 0:

        col = categorical_columns[0]

        top_category = df[col].value_counts().idxmax()

        report.append(
            f"The most frequent value in column '{col}' is '{top_category}'."
        )

    report_text = ""

    for line in report:

        formatted_line = "• " + line

        st.write(formatted_line)

        report_text += formatted_line + "\n"

    st.download_button(
        label="Download AI Analysis Report",
        data=report_text,
        file_name="ai_data_analysis_report.txt",
        mime="text/plain"
    )