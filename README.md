# 🧠 Smart Inventory Management System

A **dynamic**, **modular**, and **scalable** Inventory Management System engineered with **Flask** for robust backend operations and **Django** for a seamless, interactive frontend. This full-stack solution supports advanced business workflows like order processing, inventory tracking, warehouse logistics, secure user authentication, barcode scanning, reporting, and feedback collection. Built using modern REST APIs and tested with **POSTMAN**, this project exemplifies clean architecture and smooth integration across components.

---

## 🚀 Tech Stack Overview

| Layer          | Technology                           |
| -------------- | ------------------------------------ |
| Frontend       | Django, HTML5, CSS3, Bootstrap 5, JS |
| Backend        | Flask, Python 3.x                    |
| Styling        | Bootstrap, Custom CSS                |
| APIs           | RESTful APIs, tested with POSTMAN    |
| Authentication | Flask Login, Django Auth             |

---

## 🧩 Modular System Architecture

* **Flask (Backend)**: Processes API calls, handles logic, and manages database operations.
* **Django (Frontend)**: Consumes Flask APIs and renders data-driven, responsive UI components.
* Clear separation of concerns leads to high **maintainability**, **testability**, and **scalability**.

```mermaid
flowchart LR
    A[User Interaction] --> B[Django Frontend]
    B --> C[Flask API Layer]
    C --> D[Database Layer]
```

> 🛠️ All APIs validated using **POSTMAN** to ensure robust performance, security, and accurate data exchange.

---

## 🔐 Authentication & Role-Based Access

* Secure **login/signup system** using encrypted credentials.
* **Admin vs User** access control.
* Features like **barcode scanning** are restricted to admins for operational security.

---

## 🔑 Key Features

### 📦 Order Management

Effortless creation, modification, and real-time tracking of orders through their entire lifecycle.

### 📊 Inventory Tracking

Live monitoring of inventory levels with automated alerts for low stock and replenishment suggestions.

### 🏭 Warehouse Management

Manage multiple warehouses and track the flow of goods between storage units efficiently.

### 🧾 Barcode Scanning (Admin Only)

Admins can scan and retrieve product data instantly, improving accuracy and reducing manual entry.

### 📈 Reports & Analytics

Generate meaningful insights with exportable reports on orders, inventory levels, and warehouse movements.

### 🔐 Login & Signup

Secure onboarding system with encrypted user credentials, validations, and session control.

### 💬 Customer Feedback

Capture customer experiences through feedback forms, helping evolve product offerings.

### 💸 Feature & Pricing Pages

Clear display of available modules and flexible pricing plans tailored to user needs.

### 🔌 API Integrations

RESTful APIs allow seamless future extensions such as third-party logistics, ERPs, and payment gateways.

### 🛠️ Solutions for All

Configurable for **Retail**, **B2B**, and **Warehousing** workflows. Designed to grow with your business.

---

## 🔗 API Communication

* REST APIs developed in **Flask** serve as the system’s communication backbone.
* Supported HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
* Sample API Endpoints:

  * `/api/orders`
  * `/api/inventory`
  * `/api/warehouse`
  * `/api/users`

✅ **All endpoints tested rigorously using POSTMAN**:

* Response format validation
* Error handling
* Security headers & role validations

---

## ⚙️ System Workflow

1. User accesses web interface built with Django.
2. Django makes real-time HTTP calls to Flask APIs.
3. Flask processes requests and interacts with the database.
4. Response is sent back and dynamically rendered on the frontend.

> 🔁 This continuous feedback loop keeps data in sync and the user experience smooth.

---

## 🧪 Testing & QA

* **POSTMAN** used extensively to validate all API endpoints.
* Manual UI/UX testing on the Django side.
* Unit testing modules in progress for key Flask functions.

---

## 🌱 Planned Enhancements

* Multi-language support for global audiences.
* Role-based dashboards with real-time KPIs.
* Integrated chat support for customer service.
* Scheduled email reports and alerts.

---

## 🤝 Contributing

We welcome your ideas and code contributions!

To contribute:

1. Fork this repository
2. Create a feature branch
3. Raise a pull request after proper testing

---

## 📬 Contact

For support, collaboration, or queries:
📧 **[ishleenk722@gmail.com](mailto:ishleenk722@gmail.com)**

---

## 👨‍💼 Contributors

Special thanks to the brilliant minds who built this system:

* 🧑‍💻 **Khushboo Jain**
* 👩‍💻 **Ishleen Kaur**
* 👩‍💼 **Gurleen Kaur**
* 💡 **Liza**

**DEPLOYMENT LINK :-** https://lizasingla.pythonanywhere.com/

> ⭐ Don’t forget to **star** the repo if you liked the project. Your support means a lot!
