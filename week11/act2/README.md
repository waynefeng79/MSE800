# Feasibility Study Report

**Project Name:** Public Transport Auckland  
**Target Region:** Auckland, New Zealand  
**Data Sources:** Auckland Transport (AT) GTFS Static Feed & Legacy Realtime JSON Feed

## Executive Summary
This report examines whether it is practical to build a responsive and high-performance public transport web application for Auckland. The proposed system uses Auckland Transport (AT) General Transit Feed Specification (GTFS) static datasets together with real-time traffic information.

The application is built around an asynchronous backend stack that includes FastAPI, GeoAlchemy2, Redis, and SSE, while the frontend uses React, Node.js, and MapLibre GL for geospatial visualization. A PostgreSQL database enhanced with the PostGIS extension provides spatial data support. This architecture is expected to deliver near real-time interface updates, support different devices, and remain aligned with local cultural expectations and ethical requirements for data processing.

## 1. Technical Feasibility
The technical feasibility assessment focuses on whether the selected technologies, data pipelines, and infrastructure can satisfy the expected performance and architectural requirements of the application.

### 1.1 Technology Stack Assessment
The proposed technology stack is mature and widely adopted for building high-throughput, low-latency geospatial applications.

* **Backend (FastAPI, GeoAlchemy2, Redis, Server-Sent Events):**
  * **FastAPI** runs on an asynchronous ASGI architecture through `uvicorn`, enabling it to manage concurrent connections and I/O operations efficiently without relying heavily on thread blocking.
  * **GeoAlchemy2** extends SQLAlchemy with PostGIS capabilities, making spatial operations such as distance calculations and bounding-box queries easier to implement and maintain.
  * **Redis** acts as an in-memory data store that caches real-time vehicle locations and trip updates. Using Redis reduces database pressure caused by frequent polling cycles.
  * **Server-Sent Events (SSE)** establishes a lightweight one-way HTTP streaming channel that continuously pushes updates from Redis to web clients with less overhead than WebSocket-based communication.
* **Frontend (React, MapLibre GL):**
  * **React** manages application state changes and allows the interface to update quickly when route information or metrics change.
  * **MapLibre GL** uses hardware acceleration through WebGL/WebGPU to render dense vector layers, route geometries, and moving vehicle markers smoothly, reducing the likelihood of interface lag.
* **Database (PostgreSQL + PostGIS Extension):**
  * **PostGIS** is an established open-source spatial extension for PostgreSQL. It introduces native spatial data types, along with spatial indexes and functions that are essential for converting GTFS text files into interactive geographic features.

### 1.2 Data Pipelines and System Architecture
The system handles two independent data pipelines that operate at different update intervals.

1. **Static Data Engine (1-Hour Loop):** A background process checks the AT server (`https://gtfs.at.govt.nz/gtfs.zip`) every hour using HTTP `HEAD` requests. When the `Last-Modified` header indicates a new release, the application downloads and extracts the zip package, then parses and updates data from files such as `routes.txt`, `trips.txt`, `stops.txt`, and `shapes.txt` into PostGIS tables.
2. **Dynamic Data Engine (20-Second Loop):** A dedicated worker polls the legacy AT Realtime API (`https://api.at.govt.nz/realtime/legacy/`) every 20 seconds using a developer access key. The returned JSON payload is immediately parsed, serialized, and stored in Redis under structured keys.

```
                +----------------------------+
                | Auckland Transport Feeds   |
                +----------------------------+
                  /                        \
    (1-Hour HTTP HEAD Request)          (20-Second API Poll)
                /                            \
               v                              v
    +--------------------+          +--------------------+
    | AT GTFS Static Zip |          |  AT Realtime JSON  |
    +--------------------+          +--------------------+
               |                              |
      [Parser Engine]                [Ingestion Worker]
               |                              |
               v                              v
    +--------------------+          +--------------------+
    | PostgreSQL/PostGIS |          |    Redis Cache     |
    +--------------------+          +--------------------+
               \                              /
         (Spatial Joins)               (SSE Streaming)
                 \                          /
                  v                        v
                +----------------------------+
                |    FastAPI Backend Core    |
                +----------------------------+
                              |
                     (REST JSON & SSE)
                              |
                              v
                +----------------------------+
                |    MapLibre GL / React     |
                +----------------------------+
```

### 1.3 Technical Skills, Maintainability, and Upgrades
* **Skill Requirements:** The development team should be familiar with asynchronous Python programming, relational and spatial database indexing, and WebGL map styling. These skills are generally considered part of standard full-stack development capabilities.
* **Database Upgrades:** Schema management and structural migrations will be handled through Alembic, allowing model changes to be deployed without causing service interruptions.
* **Infrastructure Scalability:** Backend services are largely stateless. FastAPI, Redis, and the frontend can be containerized with Docker and deployed either on a single low-cost VPS or on a horizontally scalable cloud infrastructure.

## 2. Operational Feasibility
Operational feasibility evaluates how effectively the system satisfies user needs, maintains stable operations, and supports long-term maintenance.

### 2.1 Functional Requirements Fulfillment
The proposed architecture is designed to support all major user interactions.

* **User Management:** User registration, authentication, and JSON Web Token (JWT) issuance are handled by the FastAPI backend, helping protect access to restricted services.
* **Favorite Routes and Spatial Filtering:** Users can search for, filter, and save favorite routes. For nearby route searches, the frontend sends either the viewport center or user-approved coordinates, and PostGIS performs indexed distance queries on `stops.txt` and `routes.txt`.
* **Real-Time Interactive Mapping:** Selecting a route triggers queries for route shapes and stop information from PostGIS. At the same time, an SSE connection subscribes to updates related to vehicles on that route through Redis.
* **Popup Overlays and Alert Windows:** Selecting a vehicle displays information retrieved directly from Redis. Selecting a stop combines static timetable data from PostgreSQL with real-time delay information from the cache to estimate arrivals for the next three vehicles. Service disruptions are continuously displayed in a dedicated alert panel beside the map.

### 2.2 System Operations and Network Resilience
* **Low-Bandwidth Operations:** Under constrained network conditions (<10MBps), the application minimizes data usage by streaming cached data and using optimized payload structures instead of repeatedly requesting large datasets.
* **Automation Stability:** Separating data collection services from the main web server improves reliability. If the AT API becomes temporarily unavailable, the application can continue serving cached information without interrupting the user experience.

## 3. Economic Feasibility
The economic feasibility assessment compares development resources and operational expenses with the expected benefits of the system.

### 3.1 Initial Development and Cost Factors
* **Infrastructure Overhead:** FastAPI, Redis, and PostgreSQL are lightweight enough to operate on a single low-cost cloud server, typically costing around $15–$40 NZD per month.
* **API Expense Framework:** Auckland Transport provides access to its open-data platform and legacy real-time feeds at no cost to registered developers, removing transactional API expenses.
* **Engineering Timeline Investments:** Most project costs are associated with development and future maintenance work, estimated at approximately $50 NZD per hour for 80 hours across two developers.

### 3.2 Financial and Operational Justification
Although the application is intended as a public utility rather than a profit-generating product, its value comes from improving public transport accessibility, increasing service reliability, and providing commuters with a lightweight tracking tool that consumes less mobile data.

## 4. Legal Feasibility
This section evaluates compliance with regulations, licensing obligations, and ethical responsibilities.

### 4.1 Te Tiriti o Waitangi Data Protection Compliance
To align with the principles of Te Tiriti o Waitangi, the application adopts a strict Māori Data Sovereignty approach.

* The server follows a zero-telemetry retention policy.
* User coordinates used to search for nearby stops are processed only in temporary memory and are not written to logs, disks, or persistent databases.
* No historical travel paths or tracking records are stored, reducing privacy risks for users.

### 4.2 Open Data Licensing and Copyright
* **AT Licensing:** Data obtained from Auckland Transport is covered by open-data usage provisions that require attribution. The application addresses this requirement by clearly displaying licensing information within the interface.
* **Open-Source Integrity:** The selected technologies—FastAPI (MIT License), PostGIS (GPLv2), Redis (BSD/RSAL), and MapLibre GL (BSD-3-Clause)—support modification, integration, and deployment without introducing vendor lock-in or additional licensing costs.

## 5. Schedule Feasibility
The project is planned as a structured 6-week development cycle divided into three sprints, leaving enough time for testing and quality assurance before deployment.

### 5.1 Project Milestone Breakdown

```
Week:  1   2   3   4   5   6
       [-S1-]
               [-S2-]
                       [-S3-]
S1: Database Schema & Static GTFS Feeds importing
S2: Redis Cache & Real-time GTFS Feeds Integration
S3: Optimization and bug fixes
```

#### Sprint 1: Database Schema & Static GTFS Feeds Importing (Weeks 1–2)
* Initialize PostgreSQL/PostGIS and configure Alembic migration tracking.
* Develop the automated GTFS static data parser.
* Implement JWT authentication and user account tables.
* Integrate user registration and login interfaces.
* Configure the Docker environment for local testing.
* Create backend unit and integration tests.

#### Sprint 2: Redis Cache & Real-Time Integration (Weeks 3–4)
* Build the polling service for real-time updates.
* Design and implement Redis caching structures.
* Provide asynchronous SSE endpoints for live vehicle locations.
* Integrate map interactions based on GTFS data.
* Extend backend testing coverage.
* Identify a suitable free hosting platform for deployment.

#### Sprint 3: Optimization and Bug Fixes (Weeks 5–6)
* Measure performance against non-functional requirements and optimize where necessary.
* Resolve critical issues identified during testing.
* Complete final documentation.

### 5.2 Schedule Risk Assessment
* **Risk:**
  * Changes to the legacy AT real-time API format could introduce parsing failures.
  * Unexpected exceptions may increase debugging and maintenance time.
* **Mitigation:**
  * The ingestion service will isolate errors and generate alerts while allowing the underlying server to continue operating.
  * Exception handling will be implemented with appropriate granularity to reduce debugging effort and limit fault propagation.

## 6. Resource Feasibility
The resource assessment indicates that all necessary components for development and maintenance are available.

### 6.1 Resource Availability Analysis
* **Human Resources:** The project can be delivered by two developers who have practical experience with Python, React, and GIS concepts. No specialized data science team is required.
* **Software Assets:** All major technologies are open-source and free to use. Access credentials for the AT API have already been generated and verified.
* **Hardware and Infrastructure:** The system can run on an entry-level cloud server, such as a Linux instance with 2 vCPUs, 4GB RAM, and 40GB SSD storage, which helps keep infrastructure expenses manageable.

## Feasibility Verdict
The Auckland Public Transport GTFS Web Application is considered highly feasible from technical, operational, economic, legal, scheduling, cultural, and resource perspectives.
The selected technologies satisfy the application's low-latency requirements and provide sufficient support for real-time synchronization with Auckland Transport data feeds. At the same time, the commitment to zero telemetry collection aligns well with modern privacy expectations and the principles of Māori Data Sovereignty under Te Tiriti o Waitangi.
