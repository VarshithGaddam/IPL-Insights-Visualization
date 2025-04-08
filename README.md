# 🏏 IPL Insights Visualization Dashboard

Welcome to **IPL Insights Visualization** — an interactive dashboard that brings IPL data to life with advanced analytics and beautiful visuals. Built using **Apache Spark**, **Streamlit**, and **Plotly**, this app provides insights into player performances, venues, win probabilities, and more.

![App Preview](https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22Screenshot%202025-04-08%20183253.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-04-07T13%3A07%3A05.813Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F1ff0e3fe5cb649df%2FScreenshot%25202025-04-08%2520183253.png%3FExpires%3D1838725626%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DtvnmwHj8y3KrQlOp6TkexAe-vxC~cCwDNOk3bftgJtoFjaSLXgvG26Vit7nr-pVDCdPT-1aKzex5ual7OWjIU9m4flF1mftovHQdYLyjwZgJtsJ8DSjERz8bIt6o3VJzRA1HQvknXZf6vn~etQJLoWufeiXH6i7sX2RT0MWDcqta5yltBJLy1V4mahSp7rfw5smN4Veo6guBXS99QUTBpGCHhBaMxfsRFkiDJLEREHl2X4fzg9rRWy~Hx6ZRfbQSe95kAeLQk3l4AdZZ~VWuwVr4ta~MQ9TfmVeWJXmohFjPa5OBGi3vEqEWFHnIR~yIvwPdQ0jh6zaQag2RjMe2-Q__%22%7D)



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
