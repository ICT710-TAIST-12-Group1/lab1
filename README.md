# Lab1
This is first lab of Software for embedded that consists of 3 problems. The board that we use is DISCO-L475VG-IOT01A:
- push-to-light-baremetal
- push-to-light-thread
- push-to-light-eventqueue

# How to compile the source code?
1. Clone or download the repository.
2. Open the Git Bash command and change the directory to the MBED OS sub problems.
```console
User:~$ cd "[mbed folder path]"
```
3. Run this command to config the ARM path.

```console
User:~$ mbed config -G GCC_ARM-path "C:\Program Files (x86)\GNU Tools Arm Embedded\9 2019-q4-major\bin"
```
4. Run this command to flash the code to the board. 
```console
mbed compile --target DISCO_L475VG_IOT01A --toolchain GCC_ARM --flash
```

# Members
- Asadang Tanatipuk     6222040484  
- Pitisit Dillon        6222040278  
- Thanakorn Aksorndit   6222040336  
