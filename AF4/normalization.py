import pandas as pd

def normalize_data(df):
    """
    Normalizes the Amazon dataset into separate tables (3NF):
    - Categories
    - Products
    - Users
    - Sales / Reviews
    """
    print("\n📊 Normalizing data...")

    # Table: Categories
    categories = pd.DataFrame(df['category'].unique(), columns=['category_name'])
    categories['category_id'] = categories.index + 1

    # Table: Products
    products = df[['product_id', 'product_name', 'category', 'discounted_price', 'actual_price']].drop_duplicates()
    products = products.merge(categories, left_on='category', right_on='category_name')
    products = products[['product_id', 'product_name', 'category_id', 'discounted_price', 'actual_price']]

    # Table: Users
    users = df[['user_id', 'user_name']].drop_duplicates().reset_index(drop=True)

    # Table: Sales / Reviews
    sales = df[['user_id', 'product_id', 'rating', 'review_title', 'review_content']].drop_duplicates().reset_index(drop=True)

    print("✅ Normalization completed successfully.")
    return {
        "categories": categories,
        "products": products,
        "users": users,
        "sales": sales
    }
