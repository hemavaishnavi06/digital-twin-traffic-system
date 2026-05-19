# Digital Twin Based Adaptive Traffic Flow Management System

## Project Overview

This project is a Digital Twin based Virtual Commissioning Platform developed for smart traffic infrastructure simulation.

The system enables:

- PLC controller logic testing
- HMI graphics validation
- Alarm testing
- Divider actuator simulation
- Traffic prediction
- Emergency lane management
- Historian logging
- Fault injection testing

without requiring physical hardware.

The project simulates an adaptive traffic management system where a smart movable divider dynamically reallocates lanes based on real-time traffic density.

---

# Features

## Smart Divider Control

- Dynamic divider movement
- Adaptive lane allocation
- Congestion balancing
- Emergency lane creation

---

## PLC Logic Simulation

- Traffic state detection
- Industrial controller logic
- Threshold-based decision making
- Traffic signal sequencing

---

## HMI Dashboard

- Live traffic density
- Alarm display
- Prediction status
- System logs
- Divider status
- Sensor status

---

## Traffic Signal System

- RED / YELLOW / GREEN simulation
- Automatic signal timing
- Vehicle stop/go control

---

## Fault Injection

- Motor fault simulation
- Sensor fault simulation
- Communication fault simulation
- Alarm triggering and reset

---

## Prediction Engine

- Traffic trend monitoring
- Congestion prediction
- Smart monitoring system

---

## Historian Logging

- CSV data logging
- Real-time process storage
- Alarm history
- Prediction history

---

# Project Architecture

Sensors
↓
Vehicle Counter
↓
Traffic State Manager
↓
PLC Controller
↓
Divider Motor Logic
↓
Traffic Signal Controller
↓
HMI Dashboard
↓
Alarm System
↓
Historian Logger

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming |
| PyQt5 | HMI & GUI |
| CSV | Historian Logging |
| Object Oriented Programming | Modular Architecture |

---

# Folder Structure

project/
│
├── main.py
├── config.py
├── vehicle_manager.py
├── road_drawer.py
├── analytics.py
├── hmi_panel.py
├── plc_controller.py
├── traffic_state_manager.py
├── traffic_light_controller.py
├── prediction_engine.py
├── fault_manager.py
├── data_logger.py
├── splash_screen.py
├── traffic_data.csv
└── README.md

---

# Industrial Relevance

This project demonstrates:

- Virtual commissioning
- PLC logic validation
- HMI graphics testing
- SCADA-style monitoring
- Industrial alarm systems
- Adaptive infrastructure simulation

The system acts as a Digital Twin of a real smart movable road divider infrastructure.

---

# Future Scope

- AI traffic prediction
- IoT integration
- CCTV-based vehicle detection
- Multi-road scalability
- Cloud analytics
- Smart city integration

---

# Developed For

ABB Industrial Automation Competition

---

# Author

Vaishnavi