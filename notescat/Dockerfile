FROM python:alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache socat

# Copy service files
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY app/ /opt/app/

# Install requirements and make serve executable
RUN pip install -r requirements.txt && \
	chmod +x /opt/app/serve.sh

# Add user that runs the service and manage permissions
RUN adduser -D ctflib && \
	mkdir -p /opt/app/files && \
	chown -R ctflib:ctflib /opt/app/files

# Expose port and run
EXPOSE 4242
CMD ["/bin/ash", "/opt/app/serve.sh"]
