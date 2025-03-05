# DjangoLogin  

**DjangoLogin** is a project designed to help web developers **speed up** their Django website development. It provides ready-to-use **login, registration, and dashboard pages** with **full user information**, including profile pictures.  

By default, this project uses **SQLite**, but you can easily adapt it to another database that fits your needs.  

---

## **Features**  

- **`/accounts/cadastro/`** – The **registration page**, where users provide their profile information.  
- **`/accounts/login/`** – The **login page**, where users can sign in using their username and password.  
- **`/accounts/dashboard/`** – The **user dashboard**, where users can view and update their profile information.  
- **Easily customizable** – Modify the fields users provide and adapt the dashboard to your needs.  
- **Lightweight and flexible** – No built-in styling, so you can **fully customize the design** with your own CSS.  

---

## **Installation**  

To install and run this project, follow these steps:  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Barradas13/DjangoLogin.git
   ```
2. Navigate to the project directory and activate the virtual environment:  
   ```sh
   cd DjangoLogin
   source venv/bin/activate
   ```
3. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations and start the Django development server:  
   ```sh
   python3 manage.py migrate
   python3 manage.py runserver
   ```

---

## **Usage**  

You can customize this project for your web application by:  
- **Modifying the user information fields** in the registration form.  
- **Adding custom pages** to integrate with your website.  
- **Applying your own CSS styling** to match your project's design.  

DjangoLogin provides a **functional authentication system**, so you can focus on building the rest of your website without worrying about login and user management.  

---

## **Contributing**  

Contributions are welcome! Follow these steps to contribute:  

1. Fork the repository.  
2. Create a new branch:  
   ```sh
   git checkout -b feature-branch-name
   ```
3. Make your changes and commit them:  
   ```sh
   git commit -m 'Add new feature'
   ```
4. Push to the branch:  
   ```sh
   git push origin feature-branch-name
   ```
5. Open a **pull request** and describe your changes.  

---

