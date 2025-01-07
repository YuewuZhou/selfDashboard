# selfDashboard

# setup (from plain terminal Ubuntu)
sudo apt-get update && upgrade
sudo apt install python3.10-venv
python3 -m venv selfdash

# activate env
source selfdash/bin/activate

# install pip packages
pip install streamlit openai pandas

# run app
streamlit run src/main.py