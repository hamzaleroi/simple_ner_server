create DATABASE IF NOT EXISTS logs;
USE logs;
CREATE TABLE IF NOT EXISTS logs(
      id INT PRIMARY KEY AUTO_INCREMENT,
      request_query TEXT,
      nes TEXT,
      execution_time FLOAT,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
   );

