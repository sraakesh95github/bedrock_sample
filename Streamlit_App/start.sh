#!/bin/bash
cd app

# Define your AWS Creds

# Run aws configure to set up the default profile

echo "AWS CLI default profile configured successfully."

# uvicorn sb_neural_net_ui:app --host 0.0.0.0 --port 8000 &
streamlit run fb_interface_2.py --server.port=8501 --server.address=0.0.0.0
