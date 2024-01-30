# Project Scenario: Subscription Video on Demand (SVOD) Platform

## 1. Introduction:

**Context:** Develop and optimize a Subscription Video on Demand (SVOD) Platform.

**Objective:** Deliver a seamless and personalized streaming experience, catering to user preferences and behaviors, and ensuring efficient content recommendation and delivery in real-time.

## 2. Development Steps:

### 2.1. Data Collection:

- **Utilize TheMovieDB API for comprehensive film data:**
  Employ TheMovieDB API to retrieve comprehensive film data, encompassing movie details, crew details, companies, and budget for each movie, facilitating an understanding of individual film requirements.
- **Leverage TheMovieDB insights for strategic data collection:**
  Leverage TheMovieDB insights to gather information on popular movies, trends, and user preferences, thereby shaping the data collection strategy for your SVOD platform effectively.

### 2.2. Data Processing and Analysis:

- Streamline film data processing using Python libraries.
- Implement advanced natural language processing techniques for content recommendations.
- Leverage big data tools, like Apache Spark, for real-time insights.
- Provide up-to-date content recommendations based on live data.
- Ensure scalability for expanding data volumes.

### 2.3. Batch Processing for BI Insights:

- Periodically process and analyze data in batch mode using technologies like HDFS, Python libraries.
- Store processed data in a data warehouse for subsequent analysis.
- Generate BI insights, including film popularity trends, user segmentation, and sentiment analysis.

### 2.4. Real-time Recommendation Engine:

- Use Apache Kafka for real-time user interactions and film updates.
- Implement a real-time recommendation engine with Apache Spark Streaming.
- Continuously update user profiles and film recommendations based on real-time behavior, sentiment analysis, and film updates.
- Provide personalized real-time recommendations based on viewing history, ratings, and sentiment analysis.

### 2.5. Visualization and Reporting:

- Utilize BI tools like Tableau, Power BI, or Kibana for interactive dashboards.
- Visualize film trends, user preferences, sentiment analysis, and relevant metrics.
- Allow user exploration and filtering of visualizations based on genres, release dates, or demographics.

### 2.6. Additional Considerations:

- Ensure GDPR compliance by anonymizing personal data and implementing access controls.
- Implement logging and monitoring for tracking the health and performance of the data pipeline and recommendation system.
- Design infrastructure for horizontal scaling to handle growing data and user interactions, especially in the real-time recommendation engine.

## 3. Tools & Technologies:

### 2.1. Batch Processing:

- **Python:** Utilize Python for scripting and automation.
- **Pandas:** Employ Pandas for data manipulation and analysis.
- **PyODBC:** Use PyODBC for connecting to SQL Server.
- **SQL Server:** Utilize SQL Server as the data warehouse for storing and managing batch processed data.
- **HDFS (Hadoop Distributed File System):** Store and manage large-scale data in HDFS.
- **Airflow:** Automate and orchestrate batch processing workflows.
- **ERASER:** Employ ERASER as a pipeline tool for batch processing.
- **ERD (Entity Relationship Diagram) and ERM (Entity-Relationship Model):** Employ ERD and ERM for data modeling.
- **SQLAlchemy:** Implement SQLAlchemy for managing database connections and interactions.
- **SCD Type 1 (Slowly Changing Dimension - Type 1):** Apply SCD Type 1 for overwriting data changes.
- **Power BI:** Use Power BI for in-depth insights and reporting.

### 2.2. Stream Processing:

- **PySpark:** Utilize PySpark for real-time data processing.
- **Elasticsearch:** Store and index real-time data with Elasticsearch.
- **Flask API:** Develop a Flask API as the backend for creating an interactive website
- **Kafka Producer-Consumer:** Use Kafka for real-time data streaming with producer-consumer architecture.
- **Kibana:** Visualize and explore data with Kibana.
- **ERASER:** Employ ERASER as a pipeline tool for stream processing.

## 4. Acteurs (Stakeholders):

- **Jane Essadi:**
  - **Role:** System Architect.
- **Yassine Essadi:**

  - **Role:** Data Engineer.

- **`EC`ode (The Organization):**
  - **Role:** Platform Development and Management.

## 5. Deliverables:

### Functional `SVOD` Platform:

- Development of a fully functional Subscription Video on Demand (`SVOD`) platform.
- Integration of a real-time recommendation engine.

### GDPR Compliance Framework:

- Implementation of measures to ensure General Data Protection Regulation (`GDPR`) compliance.
- Anonymization of personal data and implementation of access control mechanisms.

### Scalable Infrastructure Design:

- Design of a scalable infrastructure to handle growing data volumes.
- Consideration of horizontal scaling for the real-time recommendation engine.
- Demonstration of horizontal scaling capabilities in the infrastructure.
- Efficient handling of increased data and user interactions by the real-time recommendation engine.

### Acceptance Criteria:

#### Functional `SVOD` Platform:

- All core functionalities of the `SVOD` platform are operational as expected.
- Real-time recommendations are accurate and aligned with user preferences.

## 6. Project Planning:

### Project Phases:

#### 1. Phase 1 - Stream Processing (Month 1):

- Real-time data collection using Apache Kafka.
- Utilizing PySpark for real-time processing.
- Implementation of real-time recommendation engine logic.
- Integration of TheMovieDB API for real-time updates.
- Testing and validation of the real-time processing phase.

#### 2. Phase 2 - Batch Processing (Month 2):

- Configuration of batch processing workflows using process and analyze data in batch mode using technologies like HDFS, Python libraries.
- Development of storage and periodic data analysis mechanisms.
- Generation of BI analyses based on batch-processed data.
- Testing of Phase 2.
- Finalization of project deliverables.

### Timeline:

#### Month 1

`(01/01 - 31/01)`:

- Commencement of Phase 1 - Stream Processing.
- Scheduled tasks for real-time data collection and processing.
- Testing of Phase 1.
- Preparation of Phase 1 deliverables.
- Preliminary delivery of Phase 1 (31/01).

#### Month 2

`(01/02 - 28/02)`:

- Commencement of Phase 2 - Batch Processing.
- Configuration of batch processing workflows.
- Development of storage and periodic analysis mechanisms.
- Generation of BI analyses based on batch-processed data.
- Testing of Phase 2.
- Finalization of project deliverables.
- Final project delivery (28/02).

## 7. Budget:

- Platform Development: 50,000€
- Workflow Setup: 80,000€
- Other Costs (`Hosting`, `Licenses`): 12,000€
- **Total: 142,000€**

## 8. Risks and Mitigation:

### Analysis of Risks:

- Delays in development.
- Budget overrun.
- Inaccurate or irrelevant data.
- Increased consumption charges and potential access limitations for external APIs.

### Mitigation Plans:

- Regular project monitoring and tracking to identify and address delays promptly.
- Adequate resource allocation, with the provision for additional resources if necessary.
- Continuous validation and verification of data to ensure accuracy and relevance.
- Develop a strategy to bypass the rate limit of the API, allowing unrestricted consumption.

## 9. Conclusion:

The proposed SVOD platform aims to revolutionize the streaming experience by providing personalized content recommendations in real-time, ensuring compliance with data protection regulations, scalability for future growth, and careful budget management.

## 10. Annexes:

- Diagrams of architecture.
- Detailed technical specifications.
