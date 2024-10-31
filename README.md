# Hospital Management System

## Overview

The Hospital Management System is a simple yet effective Python application designed to manage patients and doctors within a hospital environment. It utilizes object-oriented programming principles to encapsulate the data and functionalities involved in handling hospital operations. The system enables users to add patients and doctors, manage appointments, and display relevant information.

## Features

- Add and manage patient information (name, age, patient ID).
- Add and manage doctor information (name, age, specialization).
- Display detailed information about patients and doctors.
- Simple interface for easy interaction with the system.

## Installation

To set up the Hospital Management System on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hospital-management-system.git
    cd hospital-management-system
    ```

2. Ensure you have Python installed (version 3.x is recommended).

3. Run the application using:
    ```bash
    python hospital_system.py
    ```

## Usage

### Creating Instances

You can create instances for patients and doctors using the `Patient` and `Doctor` classes:

```python
from hospital_system import Patient, Doctor

# Creating a patient
patient = Patient("Jane Doe", 28, "P001")

# Creating a doctor
doctor = Doctor("Dr. Smith", 40, "Cardiology")

print(patient.display_info())  # Outputs: Patient ID: P001, Name: Jane Doe, Age: 28
print(doctor.display_info())  # Outputs: Doctor Name: Dr. Smith, Age Specialization:Cardiology

try:
    person = Person("John Doe", 30)
    person.display_info()  # This will raise NotImplementedError
except NotImplementedError as e:
    print(e)  # Outputs: Subclasses should implement this!