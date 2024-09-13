Prerequisites:
- 1 million data populated
- Siege testing lasts 10 minutes
- For testing slow query log it is run SELECT query

I've test

Result - the memory stays the same because I think that database and graylog reserves some part of the memory

| Logging       | Slow Query Log | Memory Usage | IOPS | 
|---------------|----------------|--------------|------|
| Graylog       | 1              | 3 Gb         | 40%  |
| Graylog       | 2              | 3 Gb         | 40%  |
| Graylog       | 10             | 3 Gb         | 40%  |
| Elasticsearch | 1              | 3 Gb         | 40%  |
| Elasticsearch | 2              | 3 Gb         | 40%  |
| Elasticsearch | 10             | 3 Gb         | 40%  |
