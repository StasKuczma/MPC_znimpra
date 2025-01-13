FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    cmake \
    git \
    python3 \
    python3-pip \
    python3-tk \
    libomp-dev \
    vim \
    wget \
    bash-completion \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    freeglut3-dev \
    mesa-utils \
    xvfb \
    x11-utils \
    x11-xserver-utils \
    libosmesa6-dev \
    patchelf \
    ffmpeg


COPY --from=parent requirements.txt .
ENV PIP_DEFAULT_TIMEOUT=1200
RUN pip install -U pip  \
    && pip install -r requirements.txt

# # Install acados
RUN cd opt/ && git clone https://github.com/acados/acados.git
COPY . opt/acados
RUN cd opt/acados && git submodule update --recursive --init
RUN mkdir -p build 
WORKDIR /opt/acados/build
RUN cmake -DACADOS_WITH_QPDUNES=ON -DACADOS_WITH_OSQP=ON -DACADOS_WITH_QPOASES=ON -DACADOS_NUM_THREADS=4 -DACADOS_WITH_OPENMP=ON .. && make install -j8
RUN pip3 install -e /opt/acados/interfaces/acados_template
RUN wget https://github.com/acados/tera_renderer/releases/download/v0.0.34/t_renderer-v0.0.34-linux && chmod +x t_renderer-v0.0.34-linux && mv t_renderer-v0.0.34-linux /opt/acados/bin/t_renderer


# Clean up the package cache to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "export ACADOS_SOURCE_DIR=\"/opt/acados\"" >> ~/.bashrc
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:\"/opt/acados/lib\"" >> ~/.bashrc

WORKDIR /mpc
