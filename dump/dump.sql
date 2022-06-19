USE logs;
CREATE TABLE IF NOT EXISTS logs(
      id INT PRIMARY KEY AUTO_INCREMENT,
      request_query TEXT,
      ners TEXT,
      execution_time FLOAT,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
   )