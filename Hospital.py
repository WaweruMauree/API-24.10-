class Person:
    def __init__(self, name, age):
        self.__name = name        # Encapsulated attribute by use of double underscore
        self.__age = age          # Encapsulated attribute

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def display_info(self):
        raise NotImplementedError("Subclasses should implement this!")


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.__patient_id = patient_id  # Encapsulated attribute

    @property
    def patient_id(self):
        return self.__patient_id

    def display_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.__specialization = specialization  # Encapsulated attribute

    @property
    def specialization(self):
        return self.__specialization

    def display_info(self):
        return f"Doctor Name: {self.name}, Age: {self.age}, Specialization: {self.specialization}"


class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def display_appointment(self):
        return f"Appointment for {self.patient.name} with {self.doctor.name} on {self.date_time}"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient_id, doctor_name, date_time):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name), None)
        if patient and doctor:
            appointment = Appointment(patient, doctor, date_time)
            self.appointments.append(appointment)
            return appointment.display_appointment()
        else:
            return "Patient or Doctor not found."


# Example usage
if __name__ == "__main__":
    hospital = Hospital()

    # Add doctors
    doc1 = Doctor("Alice", 35, "Cardiology")
    doc2 = Doctor("Bob", 40, "Neurology")
    hospital.add_doctor(doc1)
    hospital.add_doctor(doc2)

    # Add patients
    patient1 = Patient("James Karanja", 30, "P001")
    patient2 = Patient("Jane Tracy", 25, "P002")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Schedule appointments
    print(hospital.schedule_appointment("P001", "Alice", "2024-01-01 10:00"))
    print(hospital.schedule_appointment("P002", "Bob", "2024-01-01 11:00"))
