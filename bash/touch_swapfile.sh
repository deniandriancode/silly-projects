#!/usr/bin/env bash

# usage: script_name location bytesize

swap_loc=$1
count=$2

sudo dd if=/dev/zero of=$1 bs=1024 count=$count status=progress
sudo chmod 600 $swap_loc
sudo mkswap $swap_loc
sudo swapon $swap_loc

<<COMMENT_BLOCK
Append the following line to /etc/fstab to get the permanent effect

$swap_loc swap swap defaults 0 0

COMMENT_BLOCK
