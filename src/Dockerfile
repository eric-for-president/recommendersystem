# Declare the ARG before using it
ARG PYTHON_VERSION=3.12-slim

# Stage 1: Install Rust
FROM rust:latest AS rust_build

# Stage 2: Use Python with Rust support
FROM python:${PYTHON_VERSION}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/cargo/bin:$PATH"

# Copy Rust and Cargo from the Rust stage
COPY --from=rust_build /usr/local/cargo /usr/local/cargo
COPY --from=rust_build /usr/local/rustup /usr/local/rustup

# Set default Rust toolchain
RUN rustup default stable

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Verify Rust installation
RUN rustc --version && cargo --version

# Set working directory
WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Copy application files
COPY . /code

# Expose port 8000
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "cfehome.wsgi"]
