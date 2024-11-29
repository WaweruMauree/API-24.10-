import requests

API_URL = 'http://127.0.0.1:5000/products'

# Function to add a new product
def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(API_URL, json=product_data)
    print(f'Response: {response.status_code} - {response.json()}')

# Function to get all products
def get_products():
    response = requests.get(API_URL)
    print(f'Response: {response.status_code} - {response.json()}')

# Example usage
if __name__ == '__main__':
    add_product('Product 1', 'Description for product 1', 19.99)
    add_product('Product 2', 'Description for product 2', 29.99)
    get_products() 