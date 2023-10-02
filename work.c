/*
 * GccApplication1.c
 *
 * Created: 2023-10-01 오후 7:05:40
 * Author : lee
 */ 

#define F_CPU 16000000L
#include <avr/io.h>
#include <util/delay.h>
//PIN 외부연결, DDR 입출력, PORT 데이터
char circular_shift_left(char pattern){
	char LSB=pattern&0x80;
	char MSB=LSB>>7;
	char new_pattern= pattern<<1;
	new_pattern |= MSB;
	return new_pattern;
}


int main(void) {
	DDRB = 0xFF;
	DDRF &= ~0x01;
	PORTF |= 0x01;
	char pattern=0x01;
	PORTB=pattern;

	char state_previous=0, state_current;
	while(1){
		state_current = (PINF & 0x01);
		if(state_current ==1 && state_previous==0){
			_delay_ms(30);
			pattern= circular_shift_left(pattern);
			PORTB=pattern;
		}
		state_previous = state_current;
	}
	return 0;
}

