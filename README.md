<p align="center">
  <img src="CPA_GPA_Portal.png" width="500" alt="CPA_GPA_Portal">
</p>

<h1 align="center">GPA & CGPA Portal 🎓</h1>

A Django-based GPA & CGPA calculator portal where students can input semester-wise subject grades, automatically compute GPA and CGPA, and receive performance feedback. Built with a clean UI and a focus on academic insights.

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Screenshots](#screenshots)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

### Goal

Build a web application where students can:

- Add semester-wise subject results
- Get calculated GPA for each semester
- Track their cumulative CGPA across multiple semesters
- Receive dynamic guidance based on their performance

---

### Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap)
- **Database**: SQLite (Django default, switchable)
- **Optional Tools**: Chart.js for visual GPA/CGPA graphs

---

## Core Features

### Student GPA Entry per Semester

- Students can enter grades and credits for each subject.
- GPA is automatically calculated using:

GPA = (Sum of (Grade Point x Credit Hours)) / Total Credit Hours.

---

### Multi-Semester CGPA Calculation

- Add results for multiple semesters
- CGPA is calculated using:

- CGPA formula:

CGPA = {Sum of (GPA × Credit of that semester)} / Total Credits across all semesters.

---

### Guidance System Based on GPA/CGPA

Feedback is provided based on academic performance:

| Score Range       | Feedback               |
|-------------------|------------------------|
| GPA/CGPA ≥ 3.75   |Excellent            |
| GPA/CGPA ≥ 3.00   | Good                |
| GPA/CGPA ≥ 2.00   | Improvement   |
| GPA/CGPA < 2.00   | At Risk – Get Help  |

---

### Authentication

- Student registration/login to securely save results
- Django Admin Panel for management (admin only)

---

### User Interface

- Responsive and clean design using Bootstrap
- Real-time GPA result display with feedback
- Edit/Delete semester entries anytime

---

## Main Components

| Component           | Description                                   |
|---------------------|-----------------------------------------------|
| `Student Model`     | Stores student (user) info                    |
| `SemesterResult`    | Stores GPA + total credit per semester        |
| `Subject Model`     | Stores individual course marks and credits    |
| `GPA Calculator`    | Backend logic to compute GPA                  |
| `CGPA Calculator`   | Backend logic to compute CGPA                 |
| `Feedback System`   | Guidance messages based on GPA/CGPA           |
| `Forms & Views`     | Handles input and rendering in Django         |
| `Templates`         | HTML + Bootstrap for UI                       |
| `JavaScript`        | For interactive elements (optional)           |

---

## Features

- 🔐 User registration and authentication
- 📝 Add semesters with multiple subjects
- 🧮 GPA calculation per semester
- 📊 CGPA calculation across all semesters
- 💬 Smart academic feedback based on performance
- 🎨 Clean Bootstrap-powered UI
- 🛠 Admin dashboard for testing and control

---

## Getting Started

### 1. Clone the Repository

```
git clone https://github.com/RR0327/GPA-CGPA-Portal.git
cd GPA-CGPA-Portal
```

### 2. Create Virtual Environment

````
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
````

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```
python manage.py createsuperuser
```

### 6. Run the Development Server

```
python manage.py runserver
```

Visit the portal at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Screenshots

### Home-page
![Home-page](images/Home-page.png)

### Register-page
![Register-page](images/Register-page.png)

### Login-page
![Login-page](images/Login-page.png)

### User Dashboard with GPA & CGPA Overview
![Dashboard](images/Dashboard-with-Database.png)

---

## Credits

Built using Django by **Md Rakibul Hassan**

*CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast*

🔗 [LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)

🐙 [GitHub](https://github.com/RR0327)

Designed to help students calculate, visualize, and reflect on their academic performance through an intuitive GPA & CGPA tracking portal.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---