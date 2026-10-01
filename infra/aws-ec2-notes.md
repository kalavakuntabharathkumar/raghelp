# AWS EC2 deployment notes

1. Create an EC2 instance with a supported Linux image and restrict inbound access to the required ports/IP ranges.
2. Install Docker, clone the repository, and configure `OPENAI_API_KEY` in the host environment or a secret manager (never in the image).
3. Build and run the container behind a TLS reverse proxy; add a health check, logs, least-privilege IAM, and security updates.
4. Optional S3 extension: store versioned, approved knowledge files in a private bucket and ingest them with a scoped IAM role. This PoC reads the bundled JSON file and does not create AWS resources.
