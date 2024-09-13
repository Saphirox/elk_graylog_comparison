# Setup
- 1 million records
- Concurrency 100
- Load during 10 minutes
- Run query that gets employees by their random salaries
- docker-compose with graylog stack, elk stack. With TIG for monitoring

## Graylog: comparing memory usage

| Logging | Slow Query Log | Memory USAGE | Disk USAGE | Disk IO time | 
|---------|----------------|--------------|------------|--------------|
| Graylog | Baseline       | 5 Gi         | 29Gi       | 0mm          |
| Graylog | 1              | 6 Gi         | 37Gi       | 75mm         |
| Graylog | 2              | 6 Gi         | 29Gi       | 47mm         |
| Graylog | 10             | 5 Gi         | 29Gi       | 30Mm         |

## ELK: comparing memory usage
| Logging | Slow Query Log | Memory USAGE | Disk USAGE | Disk IO time | 
|---------|----------------|--------------|------------|--------------|
| ELK     | Baseline       | 2.72 Gi      | 29.9Gi     | 0mm          |
| ELK     | 1              | 3.93 Gi      | 31Gi       | 80mm         |
| ELK     | 2              | 3.73 Gi      | 30.4Gi     | 63mm         |
| ELK     | 10             | 3.63 Gi      | 30Gi       | 36Mm         |