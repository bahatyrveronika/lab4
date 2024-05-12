import random
class State:
    SLEEP = "Sleep"
    WORK = "Work"
    EAT = "Eat"
    RELAX = "Relax"
    EXERCISE = "Exercise"
    COMMUTE_TO_WORK = "Commute to work"
    COMMUTE_HOME = "Commute home"
    BREAKFAST = "Breakfast"
    DINNER = "Dinner"
    READ_BOOK = "Read book"
    DANCE_CLASS = "Dance class"
    DANCE = "Dance"
    SHOWER = "Shower"
    BRUSH_TEETH = "Brush teeth"
    CHANGE_CLOTHES = "Change clothes"
    MORNING_EXERCISE = "Morning exercise"
    EVENING_SHOWER = "Evening shower"
    GO_DANCE = 'GD'
    DO_DANCE = 'DD'
    ENTERTAIMENT1 = 'ENihT'
    ENTERTAIMENT2 = 'ENjnjT'
    S = 'ZZZ'

class Event:
    BREAKFAST = 'BR'
    ALARM = "Alarm"
    LUNCH_BREAK = "Lunch break"
    LEAVE_FOR_WORK = "Leave for work"
    LEAVE_WORK = "Leave work"
    DINNER = "DI"
    READ_BOOK = "RB"
    DANCE_CLASS = "DC"
    START_DANCE = "Start dance"
    END_DANCE = "End dance"
    SHOWER = "Shower"
    BRUSH_TEETH = "Brush teeth"
    CHANGE_CLOTHES = "Change clothes"
    MORNING_EXERCISE = "Morning exercise"
    EVENING_SHOWER = "Evening shower"
    WORK = 'Work'
    GO_DANCE = 'GD'
    DO_DANCE = 'DD'
    DISCO = "RE1"
    DANCE = "RE2"
    RANDOM_EVENT_3 = "RE3"
    TAKING_TAXI = 'taxi'
    FLEX = 'flex'
    END_DISCO = 'end'

class FiniteStateMachine:
    def __init__(self, hour=None, minute=None):
        self.state = State.SLEEP
        self.hour=hour
        self.minute=minute

    def transition(self, event, c=None):
        if self.state == State.SLEEP:
            if event == Event.ALARM:
                print("Waking up...")
                self.state = State.SHOWER
            else:
                print("ZZZ...")
        elif self.state == State.SHOWER:
            print("Taking a shower...")
            self.state = State.CHANGE_CLOTHES

        elif self.state == State.CHANGE_CLOTHES:
            print("Changing clothes...")
            self.state = State.MORNING_EXERCISE

        elif self.state == State.MORNING_EXERCISE:
            print("Doing morning exercises...")
            self.state = State.BREAKFAST

        elif self.state == State.BREAKFAST:
            print("Having breakfast...")
            self.state = State.COMMUTE_TO_WORK

        elif self.state == State.COMMUTE_TO_WORK:
            print("Go to university...")
            self.state = State.WORK

        elif self.state == State.WORK:
            if event == Event.LUNCH_BREAK:
                print("Time for lunch!")
                self.state = State.EAT
            elif event == Event.LEAVE_WORK:
                print("Leaving university...")
                if c==1:
                    self.state = State.ENTERTAIMENT1
                else:
                    self.state = State.ENTERTAIMENT2
            else:
                print("Study hard...")

        elif self.state == State.EAT:
            print("Having lunch...")
            self.state = State.RELAX

        elif self.state == State.RELAX:
            print("Taking a break...")
            self.state = State.EXERCISE

        elif self.state == State.EXERCISE:
            print("Going for a walk near the working place...")
            self.state = State.WORK

        elif self.state == State.COMMUTE_HOME:
            print("Returning home...")
            self.state = State.DINNER

        elif self.state == State.DINNER:
            print("Having dinner...")
            self.state = State.EVENING_SHOWER

        elif self.state == State.EVENING_SHOWER:
            print("Taking an evening shower...")
            self.state = State.READ_BOOK

        elif self.state == State.READ_BOOK:
            print("Reading a book...")
            self.state = State.SLEEP

        elif self.state == State.ENTERTAIMENT1:
            if event == Event.GO_DANCE:
                print("Going to dance classes...")

            elif event == Event.DO_DANCE:
                print("Dancing...")

            elif event == Event.END_DANCE:
                print("End of dance class...")
                self.state = State.COMMUTE_HOME

        elif self.state == State.ENTERTAIMENT2:
            if event == Event.TAKING_TAXI:
                print("calling to taxi service...")

            elif event == Event.END_DISCO:
                print("Planning to return home...")
                
            else:
                print('Flexing...')
                self.state = State.COMMUTE_HOME
        else:
            print('ZZZ....')

def main():
    fsm = FiniteStateMachine()

    for hour in range(24):
        for minute in range(0, 60, 30):
            print("Hour:", hour, "Minute:", minute)
            count=0
            random_state=None
            if random.random() < 0.25 and count==0 and hour == 19 and minute == 0:
                count+=1
                random_state = random.choice([State.ENTERTAIMENT1, State.ENTERTAIMENT2])
                if random_state==State.ENTERTAIMENT1:
                    fsm.state = random_state
                if random_state==State.ENTERTAIMENT2:
                    fsm.state = random_state

            if random.random() < 0.1 and count==0 and hour == 6 and minute == 0:
                count=7

            if count!=1:
                if hour == 19 and minute == 0:
                    fsm.state=State.SLEEP
                
            if hour == 6 and minute == 0 and count!=7:
                fsm.transition(Event.ALARM)
            elif hour == 6 and minute == 30:
                fsm.transition(Event.SHOWER)
            elif hour == 7 and minute == 0:
                fsm.transition(Event.BRUSH_TEETH)
            elif hour == 7 and minute == 30:
                fsm.transition(Event.CHANGE_CLOTHES)
            elif hour == 8 and minute == 0:
                fsm.transition(Event.MORNING_EXERCISE) 
            elif hour == 8 and minute == 30:
                fsm.transition(Event.BREAKFAST) 
            elif hour == 12 and minute == 0:
                fsm.transition(Event.LUNCH_BREAK)
            elif hour == 18 and minute == 30:
                fsm.transition(Event.LEAVE_WORK)

            elif hour == 19 and minute == 0 and fsm.state==State.ENTERTAIMENT1:
                fsm.transition(Event.GO_DANCE)  # No event
            elif hour == 19 and minute == 30 and fsm.state==State.ENTERTAIMENT1:
                fsm.transition(Event.DO_DANCE)
            elif hour == 20 and minute == 00 and fsm.state==State.ENTERTAIMENT1:
                fsm.transition(Event.END_DANCE)
            
            elif hour == 19 and minute == 0 and fsm.state==State.ENTERTAIMENT2:
                fsm.transition(Event.TAKING_TAXI)
            elif hour == 19 and minute == 30 and fsm.state==State.ENTERTAIMENT2:
                fsm.transition(Event.FLEX)
            elif hour == 20 and minute == 00 and fsm.state==State.ENTERTAIMENT2:
                fsm.transition(Event.END_DANCE)

            elif hour == 20 and minute == 00 and fsm.state==State.ENTERTAIMENT2:
                fsm.transition(Event.END_DISCO)

            elif hour == 20 and minute == 30:
                fsm.transition(Event.EVENING_SHOWER)
            else:
                fsm.transition(None)

if __name__ == "__main__":
    main()
