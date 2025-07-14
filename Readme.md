# 3-Tier Dockerized Web Application

This project demonstrates a **3-tier architecture** using Docker and Docker Compose. It includes:

- **Frontend**: React
- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Proxy**: Nginx

---

## 📁 Project Structure

```

3tier_docker_app/
├── backend/
│   ├── Dockerfile
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       └── index.js
├── nginx/
│   └── default.conf
└── docker-compose.yml

````

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### Clone the Repository

```bash
git clone https://github.com/gskumar-lab/3tier_docker_app.git
cd 3tier_docker_app
```

---

### Run the Application

```bash
docker-compose up --build
````

This will:

* Build the **frontend** and **backend**
* Launch a **PostgreSQL** database container
* Start **Nginx** to route traffic

---

## 🌐 Access the Application

| Component | URL                                          |
| --------- | -------------------------------------------- |
| Frontend  | [http://localhost](http://localhost)         |
| API       | [http://localhost/api](http://localhost/api) |
| DB        | Internal only (Postgres)                     |

---

## ⚙️ Environment Variables

**PostgreSQL (in `docker-compose.yml`):**

```yaml
POSTGRES_USER: myuser
POSTGRES_PASSWORD: mypassword
POSTGRES_DB: mydb
```

**Backend uses the same env variables to connect to Postgres:**

```yaml
POSTGRES_HOST=postgres
```

---

## 🛠 Development Tips

### Frontend

* Modify `src/App.js` or `index.js`
* Rebuild using Docker

### Backend

* Modify logic in `backend/app/main.py`
* Add dependencies to `backend/requirements.txt`

### Database

* Persistent volume: `pgdata`
* You can inspect data using a DB tool like DBeaver (use service name `postgres`)

---

## 🧹 Clean Up

To stop containers:

```bash
docker-compose down
```

To remove containers, volumes, and images:

```bash
docker-compose down --rmi all -v
```

---
