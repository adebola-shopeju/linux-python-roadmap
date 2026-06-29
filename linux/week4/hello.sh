#!/bin/bash

# My first shell script
NAME="Adebola"

echo "Hello, $NAME! Welcome to CloudOps World!"

# If/else check
if [ "$NAME" = "Adebola" ]; then 
    echo "Access granted, Cloud Engineer! 🚀"
else
    echo "Who are you? Access denied! 🚫"
fi 
# For loop
for SERVICE in EC2 S3 Lambda; do
    echo "AWS Service: $SERVICE"
done 