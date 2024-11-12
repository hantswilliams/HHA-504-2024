# Build
- command structure: docker build --platform linux/amd64 -t {name}:{version} .
    - `docker build --platform linux/amd64 -t 504flask:v1 .`

# Run (test local build)
- command structure: docker run -p {host_port}:{container_port} {name}:{version}
    - `docker run -p 5005:5000 504flask:v1`

# Publish to Docker Hub
- will need to first do `docker login -u {username}`
- then command structure: docker tag {name}:{version} {docker_hub_username}/{name}:{version}
    - `docker tag 504flask:v1 hants/504flask:v1`
- then command to push structure: docker push {docker_hub_username}/{name}:{version}
    - `docker push hants/504flask:v1`
