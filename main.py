
try:
    import machine
    machine.freq(240000000)
    from openNetwork import *
    try:
        from machine import Pin
        led = Pin(19, Pin.OUT)
        led.off()
    except:
        pass
    # DummySensorServer()
    # DummyMPUServer()
    # DummyPressureSensorServer()
    DummyStepperMotorServer()
    # DummyFactoryServer(port=40000)
    # DummyServoMotorServer(ch=[0,1,2,3])
except:
    pass