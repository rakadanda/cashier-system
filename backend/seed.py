from app import create_app
from app.models import db, User, Product

app = create_app()

with app.app_context():
    db.create_all()
    
    # Create admin user
    if not User.query.filter_by(email='admin@example.com').first():
        admin = User(email='admin@example.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
    
    # Create cashier user
    if not User.query.filter_by(email='cashier@example.com').first():
        cashier = User(email='cashier@example.com', role='cashier')
        cashier.set_password('cashier123')
        db.session.add(cashier)
    
    # Sample products
    sample_products = [
        {'sku': 'PROD001', 'name': 'Mineral Water', 'price': 5.0, 'stock': 50, 'barcode': '123456789012'},
        {'sku': 'PROD002', 'name': 'Bread', 'price': 10.0, 'stock': 30, 'barcode': '234567890123'},
        {'sku': 'PROD003', 'name': 'Milk', 'price': 15.0, 'stock': 20, 'barcode': '345678901234'},
        {'sku': 'PROD004', 'name': 'Eggs', 'price': 20.0, 'stock': 40, 'barcode': '456789012345'},
        {'sku': 'PROD005', 'name': 'Rice', 'price': 25.0, 'stock': 15, 'barcode': '567890123456'},
        {'sku': 'PROD006', 'name': 'Sugar', 'price': 12.0, 'stock': 25, 'barcode': '678901234567'},
        {'sku': 'PROD007', 'name': 'Coffee', 'price': 30.0, 'stock': 10, 'barcode': '789012345678'},
        {'sku': 'PROD008', 'name': 'Tea', 'price': 18.0, 'stock': 20, 'barcode': '890123456789'},
        {'sku': 'PROD009', 'name': 'Biscuits', 'price': 8.0, 'stock': 35, 'barcode': '901234567890'},
        {'sku': 'PROD010', 'name': 'Chocolate', 'price': 7.0, 'stock': 45, 'barcode': '012345678901'}
    ]
    
    for prod in sample_products:
        if not Product.query.filter_by(sku=prod['sku']).first():
            product = Product(**prod)
            db.session.add(product)
    
    db.session.commit()
    print("Database seeded successfully!")
