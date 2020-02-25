#include "mbed.h"

DigitalOut led1(LED1);
InterruptIn button(USER_BUTTON);
Thread thread;

void led1_thread() {
    while(true){
        if (button){
            led1 = 1;
        }else {
            led1 = 0;
        }
    }
}
 
int main() {
thread.start(led1_thread);
}