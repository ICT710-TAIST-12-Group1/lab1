#include "mbed.h"
#include "mbed_events.h"
 
DigitalOut led1(LED1);
InterruptIn button(USER_BUTTON);
 
int main() {
    while(true){
        if (button){
            led1 = 1;
        }else {
            led1 = 0;
        }
    }
}