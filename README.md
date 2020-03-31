# Lab1 of ICT 710 course  
This is first lab of Software for embedded that consists of 3 problems. The board that we use is DISCO-L475VG-IOT01A:
- push-to-light-baremetal
- push-to-light-thread
- push-to-light-eventqueue

# Lab2 of ICT 710 course  
This is second lab of Software for embedded that consists of 3 problems. The board that we use is DISCO-L475VG-IOT01A:
- push-to-http access HTTP website (http://www.example.com)
- push-to-https access HTTPS website (https://www.example.com)
- push-to-mqtt publish to NETPIE2020

# Lab3 of ICT 710 course 
This is third lab of Software for embedded that consists of 3 problems. The board that we use is DISCO-L475VG-IOT01A:
- modify the flask-ws-register to work with Postgres database (http_main.cpp)
- study and make mbed code to read temperature and humidity, then send data to server
- make server code for /update and /query and deploy on Heroku cloud (app.py)

# Car-parking Group work assignment for Hardware part
This section is to explain the system in hardware part of Car-parking group [ToF folder](https://github.com/ICT710-TAIST-12-Group1/software_Taist/tree/master/ToF)

we use 
- ![DISCO_L475VG_IOT01A](./image/DISCO_L475VG_IOT01A.jpg) Time-of-Flight and gesture-detection sensor (VL53L0X) of DISCO_L475VG_IOT01A board in hardware part (as red circle)
- [VL53L0X](https://os.mbed.com/teams/ST/code/VL53L0X/#e9269ff624ed) library 
- According to the standard size of car-park-lot the high is 2.4 meter and normal car height is around 1.47 meter referd by this site ![hight of car](https://3.bp.blogspot.com/-PGCxG6SMCxs/VgtPimM3dVI/AAAAAAAAC00/lYaVA7Xlj2A/s640/%25E0%25B8%25A3%25E0%25B8%25B0%25E0%25B8%2594%25E0%25B8%25B1%25E0%25B8%259A%25E0%25B8%2584%25E0%25B8%25A7%25E0%25B8%25B2%25E0%25B8%25A1%25E0%25B8%25AA%25E0%25B8%25B9%25E0%25B8%2587%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B8%259B%25E0%25B8%25A3%25E0%25B8%25B0%25E0%25B8%2595%25E0%25B8%25B9%25E0%25B8%2595%25E0%25B8%25B2%25E0%25B8%25A1%25E0%25B8%25A5%25E0%25B8%25B1%25E0%25B8%2581%25E0%25B8%25A9%25E0%25B8%2593%25E0%25B8%25B0%25E0%25B8%2581%25E0%25B8%25B2%25E0%25B8%25A3%25E0%25B9%2583%25E0%25B8%258A%25E0%25B9%2589%25E0%25B8%2587%25E0%25B8%25B2%25E0%25B8%2599%25E0%25B8%2595%25E0%25B9%2588%25E0%25B8%25B2%25E0%25B8%2587%25E0%25B9%2586.jpg) 
- we decided to use the ToF (mm) threshold
```
 if more than 1000 == no car in the lot
```
- in order to test the system 
    - for reed data testing
        **Test case**: VL53L0X module
        **Discription**: Verify that VL53L0X module is work properly
        **Test procedure**:	1. activate the sensor.
				    2. change the distance.
				    3. check the value from sensor.
        **Test data/device**: the values from sensor.
        **Expected results**: the value from sensor will be changed, when the distance change. 
        **Actual results**: Sensor return a random value when object is out of range(2m).

    - for the threshold value testing   
        **Test case**: Threshold value  
        **Description**: Determine accurate threshold value to define that a parking lot is empty or occupied.  
        **Test procedure**:   
        1.	Get data from the sensor  
        2.	Examine accuracy of the data from the sensor (when it says 1000 mm. is it real 1000 mm.) by set-up actual situation of 1 meter and other meter ranges.  
        3.	Calculate the actual size of a car parking lot. In order to get the threshold value. According to the information that I’ve got the standard of the parking lot is around 2.4 meters and car height is around 1.47 meters. Therefore, the time of flight should be around 1 meter for occupied and if more than 1 meter is empty.   

        **Test data/device**: The values from time of flight sensor.    
        **Expected results**: Knowing the car parking lot is empty or occupied.   
        **Actual results**: The sensor is too weak to sense the time of flight that more than around 1.5 meters. Hence, we may not sure that if the data lost coming from "Empty" or "sensor is wrong".    

    - we use [mbed](https://os.mbed.com/docs/mbed-os/v5.15/tools/test-and-debug.html) as testing system and debugging tools [black box]
    ```
     mbed test -t GCC_ARM -m auto -v --source . --source ../mbed-os --source VL53L0X
    ```
    - the result will show like this [it will take some time] ![testing-result](./image/testing-result.png)






# Members
- Asadang Tanatipuk     6222040484  
- Pitisit Dillon        6222040278  
- Thanakorn Aksorndit   6222040336  
