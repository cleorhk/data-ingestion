# data-ingestion
This project sets up a data pipeline for the New York City Taxi dataset using Docker and Docker Compose. The pipeline includes a PostgreSQL database for storing the data and Adminer for database management. The data is loaded into PostgreSQL using a Python script.
#Features
PostgreSQL Database: A robust and scalable database for storing New York City taxi trip data.
Adminer: A lightweight database management tool to interact with the PostgreSQL database.
Docker & Docker Compose: Containerized services for easy deployment and scalability.
Python Data Loader: A Python script to load CSV data into the PostgreSQL database.
Prerequisites
Docker
Docker Compose
Getting Started
Clone the repository:
Place the data files:

Place your CSV files in the data directory. Ensure the CSV files are named appropriately, such as 2022_Green_Taxi_Trip_Data_20240517.csv.

Modify configuration (if needed):

Update the load_data.py script and docker-compose.yml file if you change the default settings, such as database credentials or ports.

Build and start the services:
docker-compose up --build -d
