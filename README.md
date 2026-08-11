# CognoDB Career Graph

A career intelligence web application that helps users explore and visualize career paths, skills, roles, and relationships using a graph-based data model.

## 🚀 Overview

**CognoDB Career Graph** is a full-stack web application designed to represent career information as interconnected entities such as:

* Career roles
* Skills
* Technologies
* Job opportunities
* Career relationships

The project uses **Django REST Framework** for the backend API and a **React-based frontend** to provide an interactive dashboard. **CognoDB** is used as the graph database for storing and querying relationships between career entities.

## Architecture

```text
                    ┌─────────────────────┐
                    │     Frontend        │
                    │   React / Vite      │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │      Backend        │
                    │ Django + DRF        │
                    └──────────┬──────────┘
                               │
                               │ Graph Database Driver
                               ▼
                    ┌─────────────────────┐
                    │      CognoDB        │
                    │   Graph Database    │
                    └─────────────────────┘
```

## 🛠️ Technologies Used

### Frontend

* React
* JavaScript
* HTML5
* CSS3
* Vite

### Backend

* Python
* Django
* Django REST Framework
* django-cors-headers

### Graph Database

* CognoDB
* Neo4j Python Driver

### Other Tools

* Git
* GitHub
* Python virtual environment
* python-dotenv

## 📁 Project Structure

```text
cognodb-career-graph/
│
├── backend/
│   └── Backend configuration and API components
│
├── frontend/
│   └── React frontend and dashboard
│
├── career/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── database.py
│   ├── models.py
│   ├── seed.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── test_connection.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/pathakadithi/cognodb-career-graph.git
cd cognodb-career-graph
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your CognoDB connection details:

```env
COGNODB_URI=your_cognodb_uri
COGNODB_USERNAME=your_cognodb_username
COGNODB_PASSWORD=your_cognodb_password
```

**Do not commit your `.env` file to GitHub.**

### 5. Run Django migrations

```bash
python manage.py migrate
```

### 6. Start the backend

```bash
python manage.py runserver
```

The Django backend will normally be available at:

```text
http://127.0.0.1:8000/
```

### 7. Start the frontend

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at the URL displayed by Vite.

## 🔗 API

The Django backend exposes REST API endpoints used by the frontend to retrieve and work with career-related data.

The API layer is implemented using:

* Django
* Django REST Framework
* Neo4j Python Driver
* CognoDB

## 🧠 Graph Database

CognoDB is used to represent career entities as nodes and their relationships as graph connections.

Example conceptual structure:

```text
       ┌─────────────┐
       │   Career    │
       │    Role     │
       └──────┬──────┘
              │ requires
              ▼
       ┌─────────────┐
       │   Skill     │
       └──────┬──────┘
              │ related_to
              ▼
       ┌─────────────┐
       │ Technology  │
       └─────────────┘
```

This graph structure makes it possible to explore relationships between careers, skills, and technologies.

## 🧪 Testing

A connection test is included in:

```text
test_connection.py
```

Run it with:

```bash
python test_connection.py
```

## 🔐 Security

Sensitive configuration such as database credentials should be stored in environment variables.

The following files should **not** be committed:

```text
.env
venv/
__pycache__/
```

## 🚀 Future Improvements

Possible future enhancements include:

* More career and skill relationships
* Advanced career-path recommendations
* Skill-gap analysis
* Personalized career recommendations
* Job-market data integration
* Interactive graph visualization
* Authentication and user profiles
* Deployment to a cloud platform

## 👩‍💻 Author

**Pathak Adithi**

Computer Science graduate specializing in Artificial Intelligence and Machine Learning.

GitHub:
https://github.com/pathakadithi

---

⭐ If you find this project useful, feel free to explore the repository and provide feedback.
