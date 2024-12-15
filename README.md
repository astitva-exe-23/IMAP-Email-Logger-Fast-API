

 📧 Email Logger  

**A FastAPI-based application to fetch, log, and periodically scan unread emails using IMAP.**  

## 🚀 Project Overview  

Email Logger is a backend service built using FastAPI and SQLAlchemy. It connects to an IMAP server to fetch unread emails, logs them into a SQLite database, and provides APIs for periodic email scanning. The project is cleanly structured, making it easy to extend and deploy.  

---

## 🛠️ Features  

- **Fetch Unread Emails:** Connect to an IMAP server and retrieve unread emails.  
- **Log Emails:** Store email details (id, sender, subject, timestamp) in a SQLite database.  
- **Periodic Scanning:** Background task to scan for new emails every 30 seconds.  
- **Clean Architecture:** Organized project structure for scalability and maintenance.  
- **FastAPI Integration:** Modern, asynchronous, and high-performance API framework.  

---

## 📂 Project Structure  

```
email-logger/
│
├── app/                        # Core application
│   ├── email_handler/          # Email fetching logic and database setup
│   │   ├── database.py         # Database connection and Email model
│   │   ├── imap_client.py      # IMAP client for email fetching
│   ├── routes/                 # API route definitions
│   │   ├── email_routes.py     # Email-related endpoints
│   ├── utils/                  # Utility functions
│   ├── config.py               # Configuration and constants
│   └── main.py                 # FastAPI application entry point
│
├── emails.db                   # SQLite database file (local)
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files to ignore in Git
└── README.md                   # Project documentation
```

---

## ⚙️ Installation  

Follow these steps to set up the project on your local machine:  

### 1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/email-logger.git
cd email-logger
```

### 2. **Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4. **Configure Environment Variables**  
Create a `.env` file in the root directory to store sensitive information like IMAP credentials.  
Example:  

```plaintext
IMAP_SERVER=imap.example.com
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-password
```

### 5. **Run the Application**  
```bash
uvicorn app.main:app --reload
```
- The server will run at: **http://127.0.0.1:8000**

---

## 🔗 API Endpoints  

### 1. **Fetch Emails**  
- **Route:** `/fetch-emails`  
- **Method:** `GET`  
- **Description:** Connects to the IMAP server, fetches unread emails, and stores them in the database.  

### 2. **Start Periodic Scan**  
- **Route:** `/start-periodic-scan`  
- **Method:** `GET`  
- **Description:** Starts a background task that scans for new emails every 30 seconds.  

---

## 🗃️ Database Schema  

The SQLite database (`emails.db`) contains the following schema:  

| Column      | Type       | Description                |
|-------------|------------|----------------------------|
| id          | INTEGER    | Unique email ID (Primary Key) |
| sender      | VARCHAR    | Email sender address       |
| subject     | VARCHAR    | Email subject line         |
| timestamp   | VARCHAR    | Email received timestamp   |

---

## 🛡️ .gitignore  

To protect sensitive information and exclude unnecessary files, the following entries are added to `.gitignore`:  

```plaintext
.env
emails.db
__pycache__/
*.pyc
*.log
```

---

## 🧪 Testing  

- Use tools like **Postman** or **curl** to test the API endpoints.  
- Example to fetch emails:  
  ```bash
  curl http://127.0.0.1:8000/fetch-emails
  ```

## 🤝 Contributing  

Contributions are welcome! Please follow these steps:  

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature/your-feature-name`.  
3. Commit your changes: `git commit -m "Add some feature"`.  
4. Push to the branch: `git push origin feature/your-feature-name`.  
5. Submit a pull request.  


## 📜 License  

This project is licensed under the **MIT License**.  


## 📧 Contact  

For any questions or support, feel free to reach out:  
**Name:**Astitva Singh  
**Email:** astitmini@gmail.com
