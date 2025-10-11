# 🧠 Amazon Data System

A modular **Python-based data management and normalization system** built with `pandas`.

---

## 🚀 Description

This project processes and normalizes an Amazon dataset into separate, structured tables:

- `categories.csv`
- `products.csv`
- `users.csv`
- `sales.csv`

Each table is cleaned and normalized according to the **Third Normal Form (3NF)** to ensure data integrity and consistency.

---

## 🧩 Project Structure

```
AF4/
├── main.py
├── processing.py
├── normalization.py
├── data/
│   └── amazon.csv
├── results/
│   ├── products.csv
│   ├── categories.csv
│   ├── users.csv
│   └── sales.csv
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MrBrightside0/Programming-for-Artificial-Intelligence
   ```

2. **Navigate to the project folder:**

   ```bash
   cd Programming-for-Artificial-Intelligence
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # or
   source venv/bin/activate   # On Mac/Linux
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

To run the main program:

```bash
python main.py
```

The normalized tables will be automatically saved inside the `results/` folder.

---

## 📊 Output Tables

| Table | Description |
|--------|--------------|
| **categories** | Unique list of product categories |
| **products** | Product information with category references |
| **users** | List of unique users |
| **sales** | Reviews and ratings linking users and products |

---

## 👨‍💻 Authors

**Edmundo Ramses Moreno González**  
Bachelor in Artificial Intelligence Engineering  
Universidad Autónoma de Nuevo León – FIME

**Antonio Andre Martinez Martinez**  
Bachelor in Artificial Intelligence Engineering  
Universidad Autónoma de Nuevo León – FIME

---

## 🔗 Repository

[https://github.com/MrBrightside0/Programming-for-Artificial-Intelligence](https://github.com/MrBrightside0/Programming-for-Artificial-Intelligence)

---

Everything’s **fully ready to run** — just drop your `amazon.csv` inside `/data` and run:

```bash
python main.py
```
