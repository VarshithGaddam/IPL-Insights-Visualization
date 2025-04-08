# 🏏 IPL Insights Visualization Dashboard

Welcome to **IPL Insights Visualization** — an interactive dashboard that brings IPL data to life with advanced analytics and beautiful visuals. Built using **Apache Spark**, **Streamlit**, and **Plotly**, this app provides insights into player performances, venues, win probabilities, and more.

![App Preview](https://ibb.co/qM9sBXL0)



## 🔥 Features

- 📈 Interactive dashboards powered by Plotly
- 🧠 Machine Learning-based Win Probability Predictor
- 🏆 Top Performers Leaderboard (Runs, Wickets)
- 🏟️ Venue-based Statistics
- ⏱️ Dynamic Scoreboard Visualizer
- 🌙 Built-in Dark Mode

---

## 🛠️ Tech Stack

- Python 3.10+
- Apache Spark (PySpark)
- Pandas, Numpy, Scikit-learn
- Plotly, Matplotlib, Seaborn
- Streamlit

---

## 📁 Folder Structure

📦 IPL-Insights-Visualization ├── app.py # Main Streamlit application ├── spark_ipl_analysis.py # Spark-based data processing ├── visuals/ │ ├── scoreboard.py │ ├── venue_analysis.py │ └── win_probability.py ├── data/ # Match & delivery CSV files ├── requirements.txt └── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started (Local)

### 1. Clone the repository
git clone https://github.com/VarshithGaddam/IPL-Insights-Visualization.git
cd IPL-Insights-Visualization
2. Install dependencies
pip install -r requirements.txt
3. Run the application

streamlit run app.py
### 🌍 Deploying to Streamlit Cloud
Note: Streamlit Cloud does not support Apache Spark (PySpark). Consider converting your data processing to use pandas instead.

Push this project to GitHub

Visit streamlit.io/cloud

Click New App → Connect your GitHub repository

Choose app.py as the main file

Click Deploy

### 🖼️ How to Add Images
Place your image inside .streamlit/images/

Use the following code to load it:


from PIL import Image
import streamlit as st

st.image(Image.open(".streamlit/images/ipl-dashboard-preview.png"), use_column_width=True)
🧠 Future Work
Deep learning model for advanced match prediction

Real-time data streaming using Kafka + Spark Streaming

Geo-mapped stadium visualizations

Mobile app packaging (PWA / React Native)

### 📄 License
This project is licensed under the MIT License.

### 🙌 Acknowledgments
IPL Datasets: Kaggle

Streamlit Team for awesome deployment

Open-source contributors who made this possible

Made with ❤️ by Varshith Gaddam
