# 🔄 Unit Converter Web App

A clean, modular **Unit Converter Web Application** built with Python and Flask.  
This project is inspired by the [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter) and is designed to demonstrate fundamental software engineering principles, including **Separation of Concerns (SoC)**, base-unit strategy conversions, and clean web application architecture.

---

## 📖 Overview
The Unit Converter allows users to seamlessly convert values across multiple categories:
- **Length**: Convert between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles.
- **Weight**: Convert between milligrams, grams, kilograms, ounces, and pounds.
- **Temperature**: Convert between Celsius, Fahrenheit, and Kelvin.

The application separates business logic from presentation, using Flask templates and strict input sanitization for a reliable user experience.

---

## ⚙️ Features
- **Multi-Category Conversion**: Length, weight, and temperature conversions.
- **Efficient Math Engine**: Uses an $O(N)$ base-unit transformation strategy to scale conversion formulas efficiently.
- **Input Sanitization**: Handles user errors, invalid numbers, and special characters gracefully without crashing.
- **Clean UI**: Responsive navigation tabs and dynamic form components built with HTML5 and CSS3.
- **Modular Architecture**: Decoupled routes, conversion logic, and view layers.

---

## 🏗️ Project Architecture

```text
unit_converter/
│
├── .gitignore          # Version control ignore rules
├── app.py              # Main Flask server & route handlers
├── converters.py       # Core conversion business logic engine
├── requirements.txt    # Project dependencies
└── templates/
    ├── base.html       # Shared navigation layout & CSS styling
    ├── length.html     # Length conversion page
    ├── weight.html     # Weight conversion page
    └── temperature.html# Temperature conversion page
```
## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/unit-converter.git](https://github.com/YOUR_USERNAME/unit-converter.git)
cd unit-converter
```
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python app.py