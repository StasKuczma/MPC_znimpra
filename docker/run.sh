docker rm acados
xhost + local:root

docker run -it \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:ro" \
    --volume="$(pwd)/..:/mpc" \
    --privileged \
    --network=host \
    --name=acados \
    acados
