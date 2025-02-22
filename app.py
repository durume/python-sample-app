from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
orders = [
    {"id": 1, "fruit": "Apple",  "quantity": 10, "date": "2025-01-01", "amount": 20.0},
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

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

@app.route('/sales', methods=['GET'])
def get_sales_by_date():
    date = request.args.get('date')
    if not date:
        return jsonify({"error": "Date parameter required"}), 400
    total_sales = sum(o["amount"] for o in orders if o["date"] == date)
    return jsonify({"date": date, "total_sales": total_sales})

if __name__ == '__main__':
    app.run(debug=True)
