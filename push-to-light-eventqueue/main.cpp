#include "mbed.h"
#include "mbed_events.h"
 
DigitalOut led1(LED1);
InterruptIn button(USER_BUTTON);
 
void rise_handler(void) {
    led1 = 0;
}
 
void fall_handler(void) {
    led1 = 1;
}
 
int main() {
    EventQueue *queue = mbed_event_queue();
    button.rise(rise_handler);
    button.fall(queue->event(fall_handler));
    queue->dispatch_forever();
}