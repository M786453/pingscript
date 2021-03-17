#!/bin/bash
ip a | grep 192.168 | cut -d " " -f 6 | cut -d "/" -f 1



