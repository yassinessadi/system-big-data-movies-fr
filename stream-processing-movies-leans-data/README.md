```
├──project_root
│    │
│    api/
│    │ └──
│    │
│    app/
│    │
│    ├── kafka_producer/
│    │   ├── src/
│    │   │   └── producer.py
│    │   │       └──broadcast (latest movies data)
│    │   ├── config/
│    │   └── requirements.txt
│    │
│    ├── pyspark_consumer/
│    │   ├── src/
│    │   │   └── consumer.py
│    │   │       ├── read stream (pyspark stream)
│    │   │       ├──Transformation (handle missing values ...)
│    │   │       └──loader (mongodb)
│    │   ├── config/
│    │   └── requirements.txt
│    │
│    │
│    ├── common_utils/
│    │   ├── src/
│    │   │   └── utils.py
│    │   └── requirements.txt
│    │
│    └── requirements.txt
│
└── README.md
```
