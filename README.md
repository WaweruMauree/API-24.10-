# Simple REST API for Product Management

## Overview
This project is a simple REST API built with Flask to manage products. Each product has a name, description, and price.

## Requirements
- Python 3.x
- Flask
- Requests 

## Setup Instructions

1. **Clone the repository** (if applicable):
    ```bash
    git clone [your-repo-url]
    cd [repository-name]
    ```

2. **Install Flask**:
    ```bash
    pip install Flask
    ```

3. **Run the API server**:
    ```bash
    python app.py
    ```
   The server should now be running on `http://127.0.0.1:5000`.

## Testing the API

You can test the API using the provided `client.py` script. 

1. **Install Requests**:
    ```bash
    pip install requests
    ```

2. **Run the client script**:
    ```bash
    python client.py
    ```
   
This will add sample products and retrieve the product list.