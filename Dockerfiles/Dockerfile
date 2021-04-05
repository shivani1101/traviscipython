
# Get python version
FROM ubuntu:bionic

# Install python dependencies
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install python-pip curl git -y && \
    pip install pytest codecov


# Setup work directory
ENV APP_HOME=/usr/local/app/
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Copy git content from current branch
ADD . $WORKDIR
CMD ["echo", "webapp"]
