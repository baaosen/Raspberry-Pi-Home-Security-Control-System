#include "mbed.h"
#include "SDFileSystem.h"
#include "wave_player.h"

DigitalOut myled(p21);
SDFileSystem sd(p5, p6, p7, p8, "sd"); //SD card
AnalogOut DACout(p18);
wave_player waver(&DACout);
DigitalOut led1(LED1);
DigitalOut led2(LED2);
Serial  pi(USBTX, USBRX);


/*
void dev_recv()
{
    char temp = 0;
    led1 = !led1;
    while(pi.readable()) {
        temp = pi.getc();
        pi.putc(temp);
        if (temp=='1') {
            pi.putc('1');
            FILE *wave_file;
            wave_file=fopen("/sd/ahem.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
        if (temp=='2') {
            pi.putc('2');
            FILE *wave_file;
            wave_file=fopen("/sd/chime.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
        if (temp=='3') {
            pi.putc('3');
            FILE *wave_file;
            wave_file=fopen("/sd/alarm.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
    }
}
*/

int main()
{
    pi.baud(9600);
    while(/*pi.readable()*/ 1) {
        char temp = pi.getc();
        pi.putc(temp);
        if (temp=='1') {
            //pi.putc('1');
            FILE *wave_file;
            wave_file=fopen("/sd/ahem.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
        if (temp=='2') {
            //pi.putc('2');
            FILE *wave_file;
            wave_file=fopen("/sd/chime.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
        if (temp=='3') {
            //pi.putc('3');
            FILE *wave_file;
            wave_file=fopen("/sd/alarm.wav","r");
            waver.play(wave_file);
            fclose(wave_file);
        }
        if (temp=='5') {
            if (myled == 1) {
                myled = 0;
            } else {
                myled = 1;
            }
            
        }
    }
}
