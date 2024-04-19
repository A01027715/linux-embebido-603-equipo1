#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main (void){
    DDRB |= _BV(PORTD1);
    DDRB |= _BV(PORTD2);
    DDRB |= _BV(PORTD3);
    DDRB |= _BV(PORTD4);
    DDRB |= _BV(PORTD5);


    for (;;){
        PORTB |= _BV(PORTB1);
               _delay_ms(1000); 
        PORTB &= ~_BV(PORTB1);
                _delay_ms(1000);
        PORTB |= _BV(PORTB2);
                _delay_ms(1000);
        PORTB &= ~_BV(PORTB2);
                _delay_ms(1000);
        PORTB |= _BV(PORTB3);
                _delay_ms(1000);
        PORTB &= ~_BV(PORTB3);
                _delay_ms(1000);
        PORTB |= _BV(PORTB4);
                _delay_ms(1000);
        PORTB &= ~_BV(PORTB4);
                _delay_ms(1000);
        PORTB |= _BV(PORTB5);
                _delay_ms(1000);
        PORTB &= ~_BV(PORTB5);
                _delay_ms(1000);

    }
}