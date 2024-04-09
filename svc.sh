#!/bin/bash 

kubectl get svc | awk '{print $4}' | tail -1
