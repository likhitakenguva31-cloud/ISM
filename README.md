# 📊 Income Dashboard

A Streamlit-based dashboard for analyzing income patterns and trends.

## Features
- ✅ Automatic CSV file loading
- 📈 Data visualization and statistics
- 📋 Dataset preview and exploration
- 📊 Summary statistics display
- ❌ Missing values detection

## Setup

### Local Development
```bash
# Clone the repository
git clone https://github.com/likhitakenguva31-cloud/ISM.git
cd ISM

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

### Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select:
   - Repository: `likhitakenguva31-cloud/ISM`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
4. Click Deploy

## Project Structure
```
ISM/
├── streamlit_app.py       # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/                 # CSV files (add your datasets here)
│   └── Train.csv
└── beginning.ipynb       # Original Jupyter notebook
```

## Adding Data
Place your CSV files in the `data/` folder. The app will automatically load and display them.

## Requirements
- Python 3.8+
- Streamlit
- Pandas

See `requirements.txt` for exact versions.

## License
MIT
