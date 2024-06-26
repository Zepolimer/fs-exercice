FROM ubuntu:focal

WORKDIR /src
ENV PYTHONIOENCODING=UTF-8
RUN groupadd --gid 1000 docker \
  && useradd --uid 1000 --gid docker --shell /bin/bash --create-home docker

# Define timezone
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Set the locale
RUN apt-get update -y && \
    apt-get install -y locales && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install -y \
	    curl \
	    gnupg2 \
	    ca-certificates \
	    unzip \
	    git \
	    python3 \
	    python3-pip \
	    python-dev

# Move Python3.9 and PIP3 by default
RUN ln -sf /usr/bin/python3.9 /usr/bin/python && \
    ln -sf /usr/bin/python3.9-config /usr/bin/python-config && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    echo "PATH=/home/docker/.local/bin:$PATH" >> /home/docker/.bashrc


COPY ./src /src
ADD docker/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN docker-entrypoint.sh install

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["run"]