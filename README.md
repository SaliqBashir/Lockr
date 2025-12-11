# 🔐 Lockr - Secure Password Manager

> A full-stack web application for secure password management with enterprise-grade encryption and intuitive user experience.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-3.0+-orange.svg)](https://sqlite.org)
[![AES Encryption](https://img.shields.io/badge/Encryption-AES-red.svg)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

Lockr is a comprehensive password management solution built with modern web technologies. It provides users with a secure, encrypted vault to store, manage, and retrieve their credentials with military-grade AES encryption. The application features a responsive dark-themed UI and implements industry-standard security practices.

## ✨ Key Features

- **🔒 Advanced Security**: AES encryption for all stored passwords
- **👤 User Authentication**: Secure registration and login system with session management
- **🔍 Smart Search**: Real-time filtering and search across all password entries
- **✏️ CRUD Operations**: Create, Read, Update, Delete password entries
- **📱 Responsive Design**: Mobile-friendly interface with clean look
- **🎯 User Experience**: Intuitive single-page dashboard with all essential features
- **🔐 Password Visibility Toggle**: Secure password viewing with click-to-reveal
- **🗑️ Bulk Operations**: Efficient management of multiple entries

## 🛠️ Technical Stack

### Backend
- **Framework**: Flask 2.0+ (Python)
- **Database**: SQLite 3.0+ with optimized schema design
- **Authentication**: Flask-Session with secure cookie handling
- **Encryption**: AES (Advanced Encryption Standard)
- **Security**: Input validation, SQL injection prevention, XSS protection

### Frontend
- **Template Engine**: Jinja2 with template inheritance
- **Styling**: Custom CSS with Bootstrap integration
- **JavaScript**: Vanilla ES6+ for dynamic interactions
- **UI/UX**: Modern design principles with clean look

### Architecture
- **Pattern**: MVC (Model-View-Controller)
- **Design**: Modular architecture with separation of concerns
- **Scalability**: Blueprint-ready structure for future expansion

## 📋 System Requirements

- Python 3.8+
- Flask 2.0+
- SQLite 3.0+
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🏗️ Project Structure

```
lockr/
├── app.py                 # Main Flask application with routing logic
├── helpers.py             # Utility functions (encryption, auth decorators)
├── lockr.db              # SQLite database (auto-generated)
├── templates/
│   ├── layout.html       # Base template with navigation
│   ├── index.html        # Main dashboard
│   ├── login.html        # Authentication page
│   ├── register.html     # User registration
│   ├── edit.html         # Password editing interface
│   └── error.html        # Error handling page
└── static/
    ├── styles.css        # Custom styling with dark theme
    ├── script.js         # Client-side JavaScript
    └── icon.png          # Application branding
```

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saliqbashir/lockr.git
   cd lockr
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Navigate to `http://localhost:5000`
   - Register a new account or login with existing credentials

## 📊 Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `hash` (Encrypted password)

### Passwords Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `service_name` (Website/Application)
- `service_username` (Account username)
- `service_password` (AES encrypted)

## 🔐 Security Features

- **Password Hashing**: Werkzeug PBKDF2 for user authentication
- **AES Encryption**: Industry-standard encryption for stored passwords
- **Session Management**: Secure session handling with Flask-Session
- **Input Validation**: Comprehensive server-side validation
- **CSRF Protection**: Built-in protection against cross-site attacks
- **SQL Injection Prevention**: Parameterized queries throughout

## 🎨 UI/UX Highlights

- **Responsive Layout**: Optimized for desktop and mobile devices
- **Real-time Search**: Instant filtering without page reloads
- **Password Visibility**: Toggle between hidden and visible passwords
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: User-friendly error messages and feedback

## Screenshots
![Login Page](https://github.com/user-attachments/assets/ebce9ca9-11d4-4ebf-9cc8-143d3d34d3fb)
![Main Dashboard](https://github.com/user-attachments/assets/b5a03ba1-c5e6-4317-846b-d6a5df958a5b)
![Edit Page](https://github.com/user-attachments/assets/32129019-3b0b-45f6-8ea1-a8cd01b87f05)

## 🚀 Future Enhancements

- [ ] Two-factor authentication (2FA)
- [ ] Password strength analyzer
- [ ] Secure password generator
- [ ] Data export/import functionality
- [ ] Multi-user admin panel
- [ ] API endpoints for mobile app integration
- [ ] Advanced audit logging

## 💡 Technical Highlights for Recruiters

- **Full-Stack Development**: End-to-end web application development
- **Security-First Approach**: Implementation of encryption and security best practices
- **Database Design**: Normalized schema with proper relationships
- **Clean Architecture**: Modular, maintainable, and scalable code structure
- **User Experience**: Focus on intuitive design and smooth interactions
- **Industry Standards**: Following Flask conventions and Python best practices

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For any questions or suggestions, please reach out through GitHub issues or connect with me on LinkedIn.

---
