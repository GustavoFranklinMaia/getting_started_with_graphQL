# getting_started_with_graphQL
This project is a simple GraphQL API developed in Python using the Ariadne library. It allows you to manage users with basic create, delete, and list operations. The server runs on Uvicorn and supports queries and mutations for data manipulation.

## 📌 Features  

### 🔹 Query: `usuarios`  
📌 Returns the list of all registered users.  

### 🔹 Mutation: `criarUsuario`  
📌 Adds a new user with the following fields:  
   - `name` (String)  
   - `age` (Int)  
   - `city` (String)  

### 🔹 Mutation: `deletarUsuario`  
📌 Removes a user based on the provided name.  

---

## 🛠 Technologies Used  

✅ **Python** → Main programming language.  
✅ **Ariadne** → Used to define the schema and resolve GraphQL queries.  
✅ **Uvicorn** → ASGI server to run the application.  

---

## ▶ How to Run the Project  

1️⃣ Install dependencies:  
pip install ariadne uvicorn

2️⃣ Start the server:
python app.py

3️⃣ Access the GraphQL Playground in your browser:
http://localhost:8000
Now you're ready to test your queries and mutations! 🚀
