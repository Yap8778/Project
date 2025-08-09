# 🏥 Hospital Management System (Java)

A modular **Java-based Hospital Management System** with both **console-based** and **JavaFX GUI** interfaces.  
It manages patient information, admissions, appointments, bed allotments, medical reports, insurance claims, and more.

---

## 📜 Overview

The system is split into multiple **independent modules**, each responsible for a specific hospital operation.  
It includes **text-based console modules** for backend logic, **JavaFX GUI modules** for user-friendly interaction, and **list management modules** for structured data handling.

---

## 📂 Modules

### **Core Backend Modules**
| File | Description |
|------|-------------|
| `PatientRegistration.java` | Handles new patient registrations and stores patient details. |
| `PatientAppointment.java` | Manages scheduling of patient appointments with doctors. |
| `PatientAdmission.java` | Records and manages hospital admission details. |
| `PatientHospitalAdmission.java` | Tracks the hospital-specific admission workflow. |
| `Inpatient.java` | Manages admitted (inpatient) details and services. |
| `Outpatient.java` | Manages outpatient records and services. |
| `BedAllotment.java` | Assigns beds to patients and manages bed availability. |
| `MedicalReports.java` | Stores and retrieves patient medical reports. |
| `InsuranceClaims.java` | Handles insurance claim requests and processing. |
| `ClearAllTables.java` | Utility to clear all stored data tables (for resets). |
| `connectdb.java` | Database connection utility for all modules. |

---

### **JavaFX GUI Modules**
| File | Description |
|------|-------------|
| `RegistrationGUI.java` | GUI for patient registration. |
| `AppointmentGUI.java` | GUI for scheduling and managing appointments. |
| `AdmissionGUI.java` | GUI for handling patient admissions. |
| `BedAllotmentFX.java` | GUI for bed assignment and tracking. |
| `MedicalReportsFX.java` | GUI for managing patient medical reports. |
| `InsuranceClaimsFX.java` | GUI for processing insurance claims. |
| `HospitalMainMenu.java` | Main application menu to access all modules. |

---

### **List Management Modules**
| File | Description |
|------|-------------|
| `PatientList.java` | Maintains a centralized list of all registered patients. |
| `AdmissionList.java` | Stores and manages patient admission records. |
| `AssignedInpatientList.java` | Tracks inpatients who have been assigned beds. |
| `UnassignInpatientList.java` | Tracks inpatients awaiting bed assignment. |
| `OutpatientList.java` | Maintains a list of outpatients. |
| `ScheduleAppointmentList.java` | Stores and manages scheduled appointments. |

---

## 🛠 Features

- 🧾 **Patient Registration** – Store patient details via console or GUI.
- 📅 **Appointment Scheduling** – Manage doctor-patient appointments.
- 🛏 **Bed Management** – Allocate and manage hospital beds.
- 🏥 **Inpatient & Outpatient Handling** – Maintain detailed medical records.
- 🩺 **Medical Report Management** – Store, retrieve, and update reports.
- 💰 **Insurance Claim Processing** – Manage insurance requests and settlements.
- 📋 **List-based Data Management** – Centralized and categorized patient record handling.
- 🖥 **JavaFX GUI Support** – User-friendly interface for all major modules.
- 🧹 **Data Reset Tool** – Clear all records when required.
- 🔗 **Database Integration** – Centralized connection handling via `connectdb.java`.

---

## 🚀 How to Run

### **1. Compile the Project**
```bash
javac *.java
