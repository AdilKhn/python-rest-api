docker save -o mockapi.tar fastapi:1.0

#copy this to the target and run:
# docker load -i mockapi.tar
#docker run -p9999:9999 fastapi:1.0
#https://www.linkedin.com/pulse/how-copy-docker-image-from-one-machine-another-abhishek-rana/