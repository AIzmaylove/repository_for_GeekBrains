import time

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print('Change color ', {TrafficLight.__color[i]})
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            else:
                time.sleep(10)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()
