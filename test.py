import Adafruit_PCA9685
import time

class servo_Class:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset

        #Initialize Adafruit_PCA9685
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))

    # Angle setting
    def SetPos(self,pos):
        #PCA9685 controls angles with pulses, 150~650 of pulses correspond to 0~180° of angle
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)

    # End processing
    def Cleanup(self):
        #The servo motor is set at 90°.
        self.SetPos(int(90))
        print('90')

if __name__ == '__main__':
    Servo0 = servo_Class(Channel=1, ZeroOffset=0)

    try:
        while True:

            for deg in range(180) :
                Servo0.SetPos(int(deg))
                print(deg)
                time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo0.Cleanup()

        print("\nexit program")
