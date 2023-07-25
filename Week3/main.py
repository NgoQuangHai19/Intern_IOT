from RS485Controller import * 
from scheduler import *
from softwaretimer import * 
from Task1 import * 
from Task2 import * 
from read_sensor_task import *
from adafruit import *
from test_UII import *
import sys
import time

###

m485  = RS485Controller()

scheduler = Scheduler()
scheduler.SCH_Init()
monitoring_timer = softwaretimer()

monitoring= MonitoringTask(m485, monitoring_timer)
main_ui = Main_UI(monitoring)

scheduler.SCH_Add_Task(main_ui.UI_Refresh, 1, 1)
scheduler.SCH_Add_Task(monitoring_timer.Timer_Run, 1, 1000)
#scheduler.SCH_Add_Task(monitoring.MonitoringTask_Run, 1, 100)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

