from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps 
from flask_cors import CORS
import random
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = 'supersecretkey'  # Secret key for session management
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app) 

CORS(app)
     

# Example Inventory Data (Modify as Needed)
inventory_data = [
    {"name": "Retail Solutions", "url": "/solutions"},
    {"name": "Wholesale Solutions", "url": "/solutions"},
    {"name": "Pricing Plans", "url": "/pricing"},
    {"name": "Customer Stories", "url": "/customers"},
    {"name": "Integrations", "url": "/integrations"},
    {"name": "Resources & Guides", "url": "/resources"},
    {"name": "Our Team", "url": "/team"},
    {"name": "Contact Us", "url": "/contact"},
    {"name": "Webinar Registration", "url": "/webinar-registration"},
    {"name": "Item Grouping", "url": "/item-grouping"},
    {"name": "Multi-Warehouse", "url": "/multi-warehouse"},
    {"name": "Serial Tracking", "url": "/serial-tracking"},
    {"name": "Sales Order", "url": "/sales-order"},
    {"name": "Invoicing", "url": "/invoicing"},
    {"name": "Packing & Shipping", "url": "/packing-shipping"},
    {"name": "Sales Return", "url": "/sales-return"},
    {"name": "Reporting & Analytics", "url": "/reporting-analytics"},
    {"name": "SKU Generator", "url": "/sku-generator"},
    {"name": "Recorder Points", "url": "/recorder-points"},
    {"name": "Package Geometry", "url": "/package-geometry"},
    {"name": "Barcode Scanning", "url": "/barcodes"},
    {"name": "Warehouse Management", "url": "/warehouse-management"},
    {"name": "Inventory Tracking", "url": "/inventory"},
    {"name": "Order Management", "url": "/order_management"},
    {"name": "Cookies", "url": "/cookie_policy"},
    {"name": "Security", "url": "/security"},
    {"name": "terms of service", "url": "/terms_of_service"},
    {"name": "reports", "url": "/reports"},
    {"name": "privacy policy", "url": "/privacy_policy"},
    {"name": "login", "url": "/login"},
    {"name": "signup", "url": "/signup"},
    {"name": "explore", "url": "/integrations2"},
]

testimonials = [
    {
        "name": "Venkateswara Rao",
        "designation": "Managing Director, Azole Chem Pvt. Ltd.",
        "image": "",
        "feedback": "We manage all our inventory, sales, and purchases using Zoho Inventory."
    },
    {
        "name": "Rahul Sharma",
        "designation": "CEO, Tech Solutions",
        "image": "",
        "feedback": "Zoho Inventory has streamlined our process. The integration with Zoho Books is seamless and top-notch."
    },
    {
        "name": "Pooja Mehta",
        "designation": "Operations Head, FreshMart",
        "image": "",
        "feedback": "The automation features in Zoho Inventory have saved us countless hours. Highly recommend it!"
    },
    {
        "name": "Ankit Verma",
        "designation": "Founder, Quick Logistics",
        "image": "",
        "feedback": "Inventory tracking has never been easier. Zoho Inventory has truly transformed our workflow."
    },
    {
        "name": "Sneha Kapoor",
        "designation": "Manager, Fashion Trends",
        "image": "",
        "feedback": "From purchase orders to delivery, Zoho Inventory handles it all efficiently."
    },
    {
        "name": "Mohit Choudhary",
        "designation": "Director, BuildSmart Solutions",
        "image": "",
        "feedback": "Customer support is outstanding, and the software is incredibly intuitive!"
    }
]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:  # If no user is logged in
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/signup2', methods=['GET'])
def signup2():
    plan = request.args.get('plan')
    return render_template('signup2.html', plan=plan)

@app.route('/signup2-post', methods=['POST'])
def signup2_post():
    name = request.form['company_name']
    email = request.form['email']
    password = request.form['password']
    plan = request.args.get('plan')

    if email in User:
        return render_template('signup2.html', error="User already exists!", plan=plan)

    # Hash the password before saving it
    password_hash = generate_password_hash(password)
    User[email] = {"name": name, "password": password_hash, "history": []}
    session["user"] = User[email]
    return redirect(url_for('login'))  # Redirect to login page after signup


@app.route('/pricing-details')
def pricing_details():
    return render_template('pricing_page.html')

@app.route('/payment')
def payment():
    plan = request.args.get('plan')
    return render_template('payment.html', plan=plan)

# Processing Payments
@app.route('/process-payment', methods=['POST'])
def process_payment():
    plan = request.form.get("plan")
    payment_method = request.form.get("payment_method")

    if payment_method == "razorpay":
        return redirect("https://razorpay.com/payment-link")  # Replace with actual link

    elif payment_method == "stripe":
        return redirect("https://stripe.com/pay")  # Replace with actual link

    elif payment_method == "paypal":
        return redirect("https://paypal.com/payment")  # Replace with actual link

    elif payment_method == "googlepay":
        return redirect("https://pay.google.com/")  # Replace with actual link

    return redirect(url_for("payment", plan=plan))

@app.route('/search')
def search():
    query = request.args.get("query", "").strip().lower()  # Get search term
    if not query:
        return render_template("search_results.html", results=[], query="")  # No query case

    # Filter results based on query
    results = [item for item in inventory_data if query in item["name"].lower()]

    return render_template("search_results.html", results=results, query=query)

@app.route('/')
def home():
    user = session.get("user")
    return render_template('home.html', user=user, testimonials=testimonials)

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/integrations')
def integrations():
    return render_template('integrations.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/team')
def team():
    return render_template('team.html')

#  database for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    inventory_items = db.relationship('InventoryItem', backref='user', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)  # Add this line

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_dict = session.get("user")
        if not user_dict:
            flash("You must be logged in to access this page.", "danger")
            return redirect(url_for('login'))

        user = User.query.get(user_dict['id'])
        if not user or not user.is_admin:
            flash("Only admins can access this page.", "danger")
            return redirect(url_for('home'))  # Adjust this if needed

        return f(*args, **kwargs)
    return decorated_function



# for CRUD application: using update and delete buttons

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    item_category = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost_per_unit = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    supplier_name = db.Column(db.String(100), nullable=False)
    supplier_email = db.Column(db.String(100), nullable=False)
    supplier_phone = db.Column(db.String(100), nullable=False)
    order_status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    barcode_number = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"InventoryItem('{self.item_id}', '{self.item_name}', '{self.item_category}', '{self.quantity}', '{self.cost_per_unit}', '{self.total_cost}', '{self.supplier_name}', '{self.supplier_email}', '{self.supplier_phone}', '{self.order_status}', '{self.notes}', '{self.barcode_number}')"
    def to_dict(self):
       return {
        "item_id": self.item_id,
        "item_name": self.item_name,
        "item_category": self.item_category,
        "quantity": self.quantity,
        "cost_per_unit": self.cost_per_unit,
        "total_cost": self.total_cost,
        "supplier_name": self.supplier_name,
        "supplier_email": self.supplier_email,
        "supplier_phone": self.supplier_phone,
        "order_status": self.order_status,
        "notes": self.notes,
        "barcode_number": self.barcode_number,
        "user_id": self.user_id
    }
    
class Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    from_location = db.Column(db.String(200), nullable=False)
    to = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)

    def _repr_(self):
        return f"Movement('{self.id}', '{self.product_name}', '{self.quantity}', '{self.from_location}', '{self.to}', '{self.date}', '{self.time}')"

with app.app_context():
    db.create_all()

# route to add new items in the warehouse


@app.route('/order_management', methods=["GET", "POST"])
@login_required
def order_management():
    if request.method == "POST":
        item_id = request.form.get("item_id")
        item_name = request.form.get("item_name")
        item_category = request.form.get("item_category")
        quantity = request.form.get("quantity")
        cost_per_unit = request.form.get("cost_per_unit")
        total_cost = request.form.get("total_cost")
        supplier_name = request.form.get("supplier_name")
        supplier_email = request.form.get("supplier_email")
        supplier_phone = request.form.get("supplier_phone")
        order_status = request.form.get("order_status")
        notes = request.form.get("notes")
        barcode_number = generate_barcode()
        
        user = session.get("user")
        if user and 'id' in user:
            new_item = InventoryItem(
               item_id=item_id,
               item_name=item_name,
               item_category=item_category,
               quantity=quantity,
               cost_per_unit=cost_per_unit,
               total_cost=total_cost,
               supplier_name=supplier_name,
               supplier_email=supplier_email,
               supplier_phone=supplier_phone,
               order_status=order_status,
               notes=notes,
               barcode_number=barcode_number,
               user_id=user['id'] 
            )
        
            db.session.add(new_item)
            db.session.commit()

            return redirect(url_for('inventory'))
        else:
            flash("User not logged in.", "error")
            return redirect(url_for('login'))
    
    return render_template('order-management.html')

# Route to view all inventory items
@app.route('/inventory')
def inventory():
    user_dict = session.get("user")  # Get the dictionary from the session
    if user_dict:
        user = User.query.get(user_dict['id'])  # Fetch the actual User object!!!
        if user: # Check if the user exists in the database
            items = user.inventory_items # Now you can access inventory_items
            return render_template('inventory-tracking.html', items=items)
        else:
            flash("User not found in database.", "danger")
            return redirect(url_for('logout')) # or handle appropriately
    else:
        flash("You must be logged in to view inventory.", "danger")
        return redirect(url_for('login'))

# route to update form record

# Route to update an inventory item
@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required 
def update_item(id):
    item = InventoryItem.query.get_or_404(id)
    
    if request.method == "POST":
        item.item_id = request.form.get("item_id")
        item.item_name = request.form.get("item_name")
        item.item_category = request.form.get("item_category")
        item.quantity = request.form.get("quantity")
        item.cost_per_unit = request.form.get("cost_per_unit")
        item.total_cost = request.form.get("total_cost")
        item.supplier_name = request.form.get("supplier_name")
        item.supplier_email = request.form.get("supplier_email")
        item.supplier_phone = request.form.get("supplier_phone")
        item.order_status = request.form.get("order_status")
        item.notes = request.form.get("notes")

        db.session.commit()
        return redirect(url_for('inventory'))
    
    return render_template('update_order.html', item=item)

# Route to delete an inventory item
@app.route('/delete/<int:id>')
@login_required
def delete_item(id):
    item = InventoryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('inventory'))



def generate_barcode():
    return str(random.randint(1000000000, 9999999999))

@app.route('/barcodes')
@login_required
@admin_required
def barcodes():
    # Only admins can access this page
    user_dict = session.get("user")
    if user_dict:
        # If admin, fetch all users' inventory items
        if user_dict.get('is_admin') == 1:  # Check if the logged-in user is an admin
            items = InventoryItem.query.all()  # Fetch inventory items for all users
            return render_template('barcode-scanning.html', items=items)
        else:
            flash("You don't have permission to view this page.", "danger")
            return redirect(url_for('home'))  # Or any other appropriate page if not admin
    else:
        flash("You must be logged in to view barcodes.", "danger")
        return redirect(url_for('login'))



@app.route('/warehouse-management', methods=['GET', 'POST'])
@login_required
def warehouse_management():
    if request.method == "POST":
        id = request.form.get("id")
        product_name = request.form.get("product_name")
        quantity = request.form.get("quantity")
        from_location = request.form.get("from_location")
        to = request.form.get("to")
        date = request.form.get("date")
        time = request.form.get("time")

        

        # Create a new movement record in the database
        new_movement = Movement(
            id=id,
            product_name=product_name,
            quantity=int(quantity),
            from_location=from_location,
            to=to,
            date=date,
            time=time,
        )

        # Add the new movement to the database session and commit
        db.session.add(new_movement)
        db.session.commit()

    movements = Movement.query.all()
    return render_template('warehouse-management.html', movements=movements)

@app.route("/update_movement/<int:id>",methods=['GET' ,'POST'])
def update_movement(id):
    movement = Movement.query.get_or_404(id)
    if request.method=='POST':
        movement.product_name = request.form.get("product_name")
        movement.quantity = int(request.form.get("quantity"))
        movement.from_location = request.form.get("from_location")
        movement.to = request.form.get("to")
        movement.date = request.form.get("date")
        movement.time = request.form.get("time") 

        db.session.commit()
        return redirect(url_for('warehouse_management'))

    return render_template('update_movement.html',movement=movement)


@app.route('/delete_movement/<int:id>')
def delete_movement(id):
    movement=db.session.get(Movement, id)
    db.session.delete(movement)
    db.session.commit()
    return redirect(url_for('warehouse_management'))

@app.route('/integrations2')
def integrations2():
    return render_template('integrations2.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         user = User.query.filter_by(email=email).first()
#         if user and user.check_password(password):  # Check if the password is correct
#             session["user"] = {
#                 "id": user.id,
#                 "name": user.username,
#                 "is_admin": user.is_admin  # Store admin status
#             }
#             return redirect(url_for('home'))  # Redirect to home page after successful login
#         else:
#             flash("Invalid credentials. Try again!", "danger")  # Flash an error message
#             return redirect(url_for('login'))  # Redirect back to login page
#     return render_template('login.html')



# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # Check if the user is already signed in (i.e., user session exists)
#     if 'user' in session:
#         return '''<script type="text/javascript">
#                     alert("You are already signed in.");
#                     window.location.href = "/";
#                   </script>'''

#     if request.method == 'POST':
#         # Get user inputs from the signup form
#         company_name = request.form['company_name']
#         email = request.form['email']
#         password = request.form['password']
#         phone_number = request.form['phone_number']
#         username = request.form['username']
#         country = request.form['country']
#         state = request.form['state']
#         is_admin = True if request.form.get('is_admin') else False  # Get checkbox value

#         # Check if the email already exists in users dictionary
#         existing_user = User.query.filter_by(email=email).first()
#         if existing_user:
#             return render_template('signup.html', error="User  already exists!")
        
#         # Create a new user
#         new_user = User(
#             company_name=company_name,
#             email=email,
#             phone_number=phone_number,
#             username=username,
#             country=country,
#             state=state,
#             is_admin=is_admin  # Set admin status to True if checkbox is checked, otherwise False
#         )
#         new_user.set_password(password)  # Hash the password
#         db.session.add(new_user)
#         db.session.commit()
 
#         # # Hash the password before saving it
#         # password_hash = generate_password_hash(password)
#         # users[email] = {"name": name, "password": password_hash, "history": []}
        
#         # Store user info in session
#         session["user"] = {
#             "id": new_user.id,
#             "name": new_user.username
#         }
        
#         # Redirect to home page (or a dashboard page) after successful signup
#         return redirect(url_for('home'))

#     return render_template('signup.html')

# @app.route('/logout')
# def logout():
#     session.pop("user", None)  # Remove user from session
#     return redirect(url_for('home'))  # Redirect to the home page after logout

@app.route('/profile')
def profile():
    user = session.get("user")
    if not user:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('profile.html', user=user)

@app.route('/security')
def security():
    return render_template('security.html')  # Create security.html

@app.route('/terms_of_service')
def terms_of_service():
    return render_template('terms_of_service.html')  # Create terms_of_service.html

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')  # Create privacy_policy.html

@app.route('/cookie_policy')
def cookie_policy():
    return render_template('cookie_policy.html')  # Create cookie_policy.html

@app.route('/item-grouping')
@login_required
def item_grouping():
    return render_template('item-grouping.html')

@app.route('/multi-warehouse')
@login_required
def multi_warehouse():
    return render_template('multi-warehouse.html')

@app.route('/serial-tracking')
@login_required
def serial_tracking():
    return render_template('serial-tracking.html')

@app.route('/sales-order')
@login_required
def sales_order():
    return render_template('sales-order.html')

@app.route('/invoicing')
@login_required
def invoicing():
    return render_template('invoicing.html')

@app.route('/packing-shipping')
@login_required
def packing_shipping():
    return render_template('packing-shipping.html')

@app.route('/sales-return')
@login_required
def sales_return():
    return render_template('sales-return.html')

@app.route('/reporting-analytics')
@login_required
def reporting_analytics():
    return render_template('reporting-analytics.html')

@app.route('/sku-generator')
@login_required
def sku_generator():
    return render_template('sku-generator.html')

@app.route('/recorder-points')
@login_required
def recorder_points():
    return render_template('recorder-points.html')

@app.route('/package-geometry')
@login_required
def package_geometry():
    return render_template('package-geometry.html')

# Route for the 'Contact Us' page
@app.route('/contact-us')
@login_required
def contact_us():
    return render_template('contact-us.html')

@app.route('/webinar-registration')
@login_required
def webinar_registration():
    return render_template('webinar-registration.html')


@app.route('/manage1')
def manage1():
    return render_template('manage1.html')

@app.route('/manage2')
def manage2():
    return render_template('manage2.html')

@app.route('/manage3')
def manage3():
    return render_template('manage3.html')

@app.route('/manage4')
def manage4():
    return render_template('manage4.html')

@app.route('/manage5')
def manage5():
    return render_template('manage5.html')

@app.route('/manage6')
def manage6():
    return render_template('manage6.html')

@app.route('/manage7')
def manage7():
    return render_template('manage7.html')

@app.route('/manage8')
def manage8():
    return render_template('manage8.html')

@app.route('/manage9')
def manage9():
    return render_template('manage9.html')


@app.route('/help-documentation')
@login_required
def help_documentation():
    return render_template('help-documentation.html')

@app.route('/faq')
@login_required
def faq():
    return render_template('faq.html')

@app.route('/forums')
@login_required
def forums():
    return render_template('forums.html')

@app.route('/learn-more')
def learn_more():
    return render_template('learn-more.html')

@app.route('/blogs')
@login_required
def blogs():
    return render_template('blogs.html')

@app.route('/essential-business-guides')
@login_required
def essential_business_guides():
    return render_template('essential-business-guides.html')

@app.route('/webinar')
@login_required
def webinar():
    return render_template('webinar.html')

@app.route('/register')
@login_required
def register():
    return render_template('register.html')

@app.route('/reach-out-to-us')
@login_required
def reach_out_to_us():
    return render_template('reach-out-to-us.html')

@app.route('/quick-reference')
@login_required
def quick_reference():
    return render_template('quick-reference.html')


# for API:

# -----------------------------MOVEMENT PAGE:---------------------------------------
# Route to fetch movements
@app.route('/add_movement', methods=['POST'])
def add_movement():
    data = request.get_json()
    movement = Movement(
        product_name=data['product_name'],
        quantity=data['quantity'],
        from_location=data['from_location'],
        to=data['to_location'],
        date=data['date'],
        time=data['time']
    )
    db.session.add(movement)
    db.session.commit()
    return jsonify({"message": "Movement added successfully"}), 201

# GET
@app.route('/get_movements', methods=['GET'])
def get_movements():
    movements = Movement.query.all()
    return jsonify([
        {
            "id": m.id,
            "product_name": m.product_name,
            "quantity": m.quantity,
            "from_location": m.from_location,
            "to_location": m.to,
            "date": m.date,
            "time": m.time
        }
        for m in movements
    ])

# Route to update a movement
@app.route('/update_movement/<int:movement_id>', methods=['PUT'])
def update_move(movement_id):
    movement = Movement.query.get_or_404(movement_id)
    data = request.get_json()

    # Update the fields
    movement.product_name = data.get('product_name', movement.product_name)
    movement.quantity = data.get('quantity', movement.quantity)
    movement.from_location = data.get('from_location', movement.from_location)
    movement.to = data.get('to_location', movement.to)
    movement.date = data.get('date', movement.date)
    movement.time = data.get('time', movement.time)

    try:
        db.session.commit()
        return jsonify({"message": "Movement updated successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



# Route to delete a movement
@app.route("/delete_movement/<int:movement_id>", methods=["DELETE"])
def delete_move(movement_id):
    try:
        movement = Movement.query.get(movement_id)
        if movement:
            db.session.delete(movement)
            db.session.commit()
            return jsonify({"message": "Movement deleted successfully"}), 200
        else:
            return jsonify({"message": "Movement not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------Login/Signup-------------------------------

@app.route('/register', methods=['POST'])
def register_api():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already taken'}), 400

    user = User(
        company_name=data['company_name'],
        email=data['email'],
        phone_number=data['phone_number'],
        username=data['username'],
        country=data['country'],
        state=data['state'],
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    print(f"User registered: {user.username}, Email: {user.email}")

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login_api():
    try:
        data = request.get_json()

        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'message': 'Email and password required'}), 400

        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({
                'status': 'success',
                'user_id': user.id,
                'username': user.username
            }), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': 'Server error'}), 500


# get user:
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'user_id': user.id,
            'company_name': user.company_name,
            'email': user.email,
            'phone_number': user.phone_number,
            'username': user.username,
            'country': user.country,
            'state': user.state
        }), 200
    return jsonify({'message': 'User not found'}), 404

# put- update user:
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user.company_name = data.get('company_name', user.company_name)
    user.phone_number = data.get('phone_number', user.phone_number)
    user.username = data.get('username', user.username)
    user.country = data.get('country', user.country)
    user.state = data.get('state', user.state)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

#  delete user:
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
