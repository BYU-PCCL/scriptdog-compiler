# ScriptDog Compiler

A compiler for ScriptDog scripts. The base code for ScriptDog can be found at https://github.com/BYU-PCCL/scriptdog. It compiles ScriptDog scripts to pkl files.

## install
First you need to install scriptdog:
```
pip3 install git+https://github.com/BYU-PCCL/scriptdog.git
```

Then you can install the compiler:
```
pip3 install git+https://github.com/BYU-PCCL/scriptdog-compiler.git
```
## use

The compiler is used after you have written a ScriptDog script. The arguments look like this:
```
scriptdog-compile /path/to/scriptdog-script.dog /path/to/output-compiled-script.pkl
```
The second param is optional. If not specified then it will name the compiled script after the original script and place it in the same directory. _IMPORTANT_: The file type of your compiled script is a pkl. If you try something else, things will break.

Example: Assuming that you have a ScriptDog script called sample.dog:
```
scriptdog-compile sample.dog sample.pkl
```
