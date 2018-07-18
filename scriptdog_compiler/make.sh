#!/bin/bash

# NOTE: you should only have to run this if you modify the grammar

java -jar antlr-4.7.1-complete.jar -o compiler -visitor -Dlanguage=Python3 Scriptdog.g
