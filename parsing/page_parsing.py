import requests

# constructor contains product data
class ProductInfo:
    def __init__(self, category, price, title, discount, rating, total_sales, prod_id):
        self.category = category
        self.price = price
        self.title = title
        self.discount = discount
        self.total_sales = total_sales
        self.rating = rating
        self.prod_id = prod_id

    # method to count number of products
    def count(self):
        return len(self.prod_id)
    
# Function to get product data using API
def get_product_data(page):
    url = f'https://tiki.vn/api/v2/products?limit=20&page={page}&category=8322'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors

    data = response.json()
    product_list = []

# Function to process page data using API
def process_page(website_path, link, i):
    # Extract the category ID from the link (e.g., "/nha-sach-tiki/c8322" -> "8322")
    category_id = link.split('/c')[-1]  # Assuming category ID is always after 'c' in the URL path

    # Construct the API URL using the provided parameters
    url = f'{website_path}/api/v2/products?limit=20&page={i}&category={category_id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors

    data = response.json()
    product_list = []

    for product in data.get('data', []):
        category = link  # This can be derived dynamically if needed
        title = product.get('name', 'N/A')
        price = product.get('price', 0)
        discount = product.get('discount_rate', 0)
        rating = product.get('rating_average', 0)
        total_sales = product.get('quantity_sold', {}).get('value', 0)
        prod_id = product.get('id', 'N/A')

        # Store the data into ProductInfo object    
        product_info = ProductInfo(
            category=category,
            price=price,
            title=title,
            discount=f"{discount}%",
            rating=rating,
            total_sales=total_sales,
            prod_id=prod_id
        )

        # Create a tuple with the required data
        product_tuple = (
            product_info.prod_id,
            product_info.category,
            product_info.price,
            product_info.title,
            product_info.discount,
            product_info.rating,
            'N/A',  # Placeholder for image URL (can be populated if needed)
            f"{website_path}/p/{product_info.prod_id}",  # Construct product URL
            f"{category}?page={i}"
        )

        product_list.append(product_tuple)

    return product_list
