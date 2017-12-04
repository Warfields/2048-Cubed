# 2048-Cubed
Our CSCI250 Capstone project code. This code drives an array of RGB LEDs controlled by a raspberry pi. This Repo contains a class for making any sized game of 2048 in three dimensions (Inculding custom 2D boards). The other file included is the GPIO implementation to push values to our array. This is done by using SN74HC595 Shift registers, allowing the control of many LEDs (192 individual color channels in our case) with only four GPIO outputs from the raspberry pi.

Coded in Python.
