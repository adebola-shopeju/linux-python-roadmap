#!/bin/bash
# System Health Checker - built by Adebola
echo "🔍 Starting system health check..."
df -h
vm_stat
ps aux | head -5
uptime 