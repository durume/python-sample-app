from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data (same as before)
orders = [
    {"id": 1, "fruit": "Apple", "quantity": 10, "date": "2025-01-01", "amount": 20.0},
    {"id": 2, "fruit": "Banana", "quantity": 5,  "date": "2025-01-02", "amount": 15.0},
    {"id": 3, "fruit": "Cherry", "quantity": 12, "date": "2025-01-01", "amount": 30.0},
    {"id": 4, "fruit": "Strawberry", "quantity": 8, "date": "2025-01-02", "amount": 24.0},
    {"id": 5, "fruit": "Orange", "quantity": 7, "date": "2025-01-01", "amount": 14.0},
    {"id": 6, "fruit": "Grapes", "quantity": 15, "date": "2025-01-03", "amount": 45.0},
    {"id": 7, "fruit": "Watermelon", "quantity": 2, "date": "2025-01-02", "amount": 12.0},
    {"id": 8, "fruit": "Blueberry", "quantity": 25, "date": "2025-01-01", "amount": 50.0},
    {"id": 9, "fruit": "Pineapple", "quantity": 3, "date": "2025-01-03", "amount": 18.0},
    {"id": 10, "fruit": "Mango", "quantity": 20, "date": "2025-01-03", "amount": 60.0}
]

@app.route('/')
def home():
    """
    Front page with welcoming text
    """
    return render_template('index.html')

@app.route('/orders_view')
def orders_view():
    """
    Orders page in a table format
    """
    return render_template('orders.html', orders=orders)

@app.route('/order_by_id', methods=['GET', 'POST'])
def order_by_id():
    """
    Page with an input box to query specific order by ID
    - On POST, shows 'what you asked' and 'retrieved data'
    """
    retrieved_order = None
    asked_id = None

    if request.method == 'POST':
        # Get the order ID from form input
        asked_id = request.form.get('order_id')
        if asked_id and asked_id.isdigit():
            order_id = int(asked_id)
            retrieved_order = next((o for o in orders if o["id"] == order_id), None)

    return render_template('order_by_id.html',
                           asked_id=asked_id,
                           retrieved_order=retrieved_order)

@app.route('/sales_by_date', methods=['GET', 'POST'])
def sales_by_date():
    """
    Page with a date input and a button to retrieve corresponding sales data
    """
    asked_date = None
    total_sales = None

    if request.method == 'POST':
        asked_date = request.form.get('sales_date')
        if asked_date:
            total_sales = sum(o["amount"] for o in orders if o["date"] == asked_date)

    return render_template('sales_by_date.html',
                           asked_date=asked_date,
                           total_sales=total_sales)

if __name__ == '__main__':
    app.run(debug=True)
