#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line


python3 /home/bhavani/Documents/optimization/opt_linear/opt_1.py

cd /home/bhavani/Documents/optimization/opt_linear
pdflatex opt.tex
xdg-open opt.pdf


#Test Python Installation
#Uncomment only the following line
