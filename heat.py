import time
name = input('whats your name: ')
from random import randint
print('\n' * 100)
print('\n[- HEAT / by Owen Basore -]')
print('\n[------------------------]')
print('        HEAT')
print('[------------------------]')
print('\n30:44-945.7 : cryptTek inc.')
time.sleep(3)
def loading_bar(seconds):
    for progress in range(0, seconds + 1):
        percent = (progress * 100) // seconds
        print('''
        ''')
        print("\rLoading...")
        print("\r<" + ("=" * progress) + (" " * (seconds - progress)) + "> " + str(percent) + "%")
        print("\r\r",end='\r')
        time.sleep(.5)
loading_bar(10)
print('\nInitalizing System Control..')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(.5)
print('\nTerminal 1 Online...')
time.sleep(1.3)
print('\nTerminal 2 Online...')
time.sleep(1.3)
print('\nSecurity Cam 1-5 Offline...')
time.sleep(1.3)
print('\nLife Support Online...')
time.sleep(1.3)
print('\nEmergency Power Online...')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
print('''\n/ERROR/ : cryo pod 368 containing crew member ''',name,''' has been Deactivated''')
time.sleep(1.7)
print('''\ntime/year [304 of 450] 96 Year(s) Left Until Decent on Europa''')
time.sleep(1.7)
print('''\n\n[-Scanning Passenger-]''')
time.sleep(2)
print('\nSCAN COMPLETE \n')
time.sleep(1)
print('passenger #688',name.upper(),' has logged into terminal 1')
time.sleep(1.5)
def start(inventory):
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('\n-[/ Map /]-')
    time.sleep(.5)
    print('\n1.) deck 1 - Security')
    time.sleep(.5)
    print('2.) deck 2 - Maintenance')
    time.sleep(.5)
    print('3.) deck 3 - Cargo Bay - Airlock')
    time.sleep(.5)
    print('4.) deck 4 - Droid hanger')
    time.sleep(.5)
    print('5.) deck 5 - Shuttle Control')
    time.sleep(.5)
    print('6.) deck 6 - Observation Deck')
    time.sleep(.5)
    print('''
type help for help''')
    cmdlist = ['1', '2', '3', '4', '5', '6', ]
    cmd = getcmd(cmdlist)

    if cmd == '1':
        security(inventory)
    elif cmd == '2':
        if 'droid hack' in inventory:
            print('\n- DECK 2 - MAINTENANCE LOCKED -')
            time.sleep(1)
            start(inventory)
        else:
            maintenance(inventory)
    elif cmd == '3':
        cargo_hold(inventory)
    elif cmd == '4':
        if 'laser' in inventory:
            print('\n- DECK 4 - DROID HANGAR LOCKED -')
            time.sleep(2)
            start(inventory)
        else:
            droid_hangar(inventory)
    elif cmd == '5':
        shuttle_control(inventory)
    elif cmd == '6':
        if 'sight' in inventory:
            print('\n- DECK 6 - OBSERVATION LOCKED -')
            time.sleep(2)
            start(inventory)
        else:
            observation(inventory)

def maintenance(inventory):
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('''\nThis is the maintenance deck There are 10 enemy droids and 3 soldiers
You can see a terminated crew droid, it has sustained
severe laser fire .''')
    print('\n[-MAINTENANCE-]\n')
    print('1.) carry the crew droid to the main elevator and inspect it')
    print('2.) Retreat to Main Elevator')
    print('3.) Fight the Enemy troops')

    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        crew_droid(inventory)
    elif cmd == '2':
        start(inventory)
    elif cmd == '3':
        if 'laser' and 'laser pistol sight' and 'armour' in inventory:
            time.sleep(.5)
            print('your laser pistols auto aim sight locks onto the largest enemy\n')
            time.sleep(.5)
            print('[- ENEMY COMANDER DROID TERMINATED -]\n')
            time.sleep(1)
            print('''the crew droid activates self destruct
1.) run to main elevator
2.) fight more droids
3.) grab the comander droids laser rifle and run''')
            cmdlist = ['1', '2', '3']
            cmd = getcmd(cmdlist)
            if cmd == '1':
                start(inventory)
            elif cmd == '2':
                print('a barage of bullets fly at you, you try to run but its too late\n')
                time.sleep(1)
                print('GAME OVER')
            elif cmd == '3':
                print('you grab the dead comander droids laser rifle and bolt out the door')
                time.sleep(1)
                items = ['armour']
                item = ['laser rifle']
                if len(items) > 0:
                    for item in items:
                        item = ['laser rifle']
                        print('\n--> %s' % (item))
                else:
                    item = ['laser rifle']
                    print('\n--> %s' % (item), '\n')
                inventory.append('laser rifle')
                item = ['laser rifle']
        else:
            time.sleep(1)
            print('the droids let out a barage of fire, you get hit multiple times')
            time.sleep(1)
            print('YOU LOSE')
            print('tip: next time find armour, a siqht, and a weapon before fighting a comand droid')


def crew_droid(inventory, items=['droid hack']):
    print('\n----------')
    print('''\nmaintnence droid #716 has a droid hack program uploaded on it 
and it's connection outlet is still intact.
You can connect to this droids service
port and download the program for later use.
1.) to go back
.) type "service port" to download the program for later use''')
    if len(items) > 0:
        for item in items:
            print('\n', (item),' has been added to your inventory')
    cmdlist = ['service port', '1']
    cmd = getcmd(cmdlist)
    if cmd == 'service port':
        inventory.append('droid hack')
#        items = ['droid hack']
        print('\nservice port connected.')
        time.sleep(1)
        print('accessing file..')
        time.sleep(1)
        print('downloading..')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('\ndownload complete.')
        print('\nYou have downloaded the droid hack program and return\n')
        print('to the Main Elevator.')
        time.sleep(2)
        start(inventory)
    elif cmd == '1':
        maintenance(inventory)
    else:
        print('\n error. invalid command-')


def cargo_hold(inventory):
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('''\nYou enter the Cargo Hold, eight Enemy Combat droids
unload a barrage of laser fire at you. Their fire is very accurate
and you take a direct hit.''')
    print('\n[-CARGO HOLD - AIRLOCK-]')
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('\n')
    time.sleep(1)
    print('[- YOU LOSE -]')
    time.sleep(1)
    print('\nGAME OVER\n')
    exit(0)


def droid_hangar(inventory):
    print('\n----------')
    print('\nMoving..')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('''\nThe Droid Hangar is filled with debri. There
is laser scoring everywhere and all droids are terminated.
In the corner there is one inactive repair droid still in his security
cylinder. You can initialise the droid to repair your laser but you will 
require a 3 digit access code.\n''')
    print('[-DROID HANGAR-]')
    print('\n1.) Repair Droid 3 digit code')
    print('2.) Return to Main Elevator')

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        access_code(inventory)
    elif cmd == '2':
        start(inventory)


def access_code(inventory):
    code = '%d%d%d' % (randint(0, 9), randint(0, 9), randint(0, 9))
    guess = input('\n[KEYPAD]> ')
    guesses = 0

    while guess != code and guess != 'yu8xxj3' and guesses < 4:
        print('\n* ACCESS - DENIED *')
        guesses += 1
        guess = input('\n[KEYPAD]> ')

    if guess == code or 'yu8xxj3' or 'code':
        repair_droid(inventory)
    else:
        print('\n....')
        time.sleep(1)
        print('\n....')
        time.sleep(1)
        print('\nKEYPAD - LOCKED')
        time.sleep(1)
        print('\ncode randomizing..')
        time.sleep(1)
        print('\nKEYPAD - OPEN')
        time.sleep(1)
        droid_hangar(inventory)


def repair_droid(inventory, items=['laser']):
    print('\n\n----------')
    print('\n~$ Initiating DROID#323 boot sequence....')
    time.sleep(1)
    print('Repair Droid#323 booting....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('Repair Droid Active.')
    time.sleep(1)
    print('''\nThe Repair droid is now active. You MUST connect to
this droid with service port to repair laser pistol for later use.''')
#    if len(items) > 0:
#        for item in items:
    cmdlist = ['service port']
    cmd = getcmd(cmdlist)
    if cmd == 'service port':
        inventory.append('laser')
        item = ['laser']
        print('\nservice port connected.')
        time.sleep(1)
        print('Repairing Laser...')
        time.sleep(1)
        print('Detaching Laser..')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('\n[- LASER ONLINE -]')
        print('''\nYou have collected a laser pistol which can be used to defeat enemy entities
You de-activate the RepairDroid and return to the Main Elevator.''')
        time.sleep(.5)
        print('\n--> %s' % (item))
        time.sleep(.5)
        start(inventory)
    else:
        print('\n error. invalid command-')


def security(inventory):
    security_attempts = 10
    print('\n----------')
    print('Moving..')
    time.sleep(1)
    print('----------')
    time.sleep(1)
    one_locked = 1
    while one_locked == 1:
        print('# Door Locked #')
        security_password = input('''Enter one Digit Password
''')
        if security_password == '7':
            print('# UNLOCKED #')
            one_locked = 0
        elif security_attempts < 1:
            print('just go ')
            one_locked = 0
        else:

            print(security_attempts, ' Attempts Left')
            security_attempts = security_attempts - 1
    print('''\nyou have entered the Security Deck. This is where all
surveillance aboard the shuttle is done. A terminated droid is lying on the floor.
You must access the Sentry droid's logs to enter an escape pod to escape but you
will have to hack the data recorder first.\n''')
    print('[-SECURITY-]\n')
    print('1.) View Surveillance monitors of other decks')
    print('2.) Hack Sentry droid 343')
    print('3.) Return to main elevator')

    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        print('\n----------')
        print('\nLoading Terminal....')
        print('\n----------')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('Terminal 2 Active.')
        time.sleep(1)
        cam_boot_loop = 1
        while one_locked == 1:
            print('# Terminal 2 Locked #')
            security_password = input('''Enter 1 Digit Password
''')
            if security_password == '4':
                print('# UNLOCKED #')
                one_locked = 0
            elif security_attempts < 1:
                print('I give up, just go ')
                one_locked = 0
            else:
                print(security_attempts, '\n Attempts Left')
                security_attempts = security_attempts - 1
                time.sleep(1)
        print('\n[- SURVEILLANCE FEED -]')
        time.sleep(1)
        print('''\n-The Droid Hangar Camera is offline you have no live feed.''')
        time.sleep(1)
        print('\n-Eight droids are patrolling the cargo bay.')
        time.sleep(1)
        print('\n-The air lock in the Maintnence Deck has breeched, droids are pooring in through the hole.')
        time.sleep(1)
        print('\n-A Large Enemy Command droid Has hyjacked The Bridge.')
        time.sleep(1)
        print(''''\n-The observation deck holds a large 3-legged enemy robot and a wounded crew member.''')
        time.sleep(2)
        security_returning(inventory)

    elif cmd == '2':
        if 'droid hack' in inventory:
            print('\nuploading program....')
            time.sleep(2)
            print('....')
            time.sleep(1)
            print('....')
            time.sleep(2)
            print('''<html>
    <head>
<meta charset="utf-8">
<title>Test</title>
<link rel="stylesheet" type="text/css" href="spaced.css">
<link rel="shortcut icon" type="image/png" href="http://test.noa16.png"/>
<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300' rel='stylesheet' type='text/css'>
</head>
<body>
<p class="text" data-text="test text 010101101010101 lolol whatever"</p>
<script>
   var printText = $('.text').data('text');

var contentArray = printText.split('/n');
$.each(contentArray, function(index, newLine) {
  $('.text').append('<span style="display:block;" id="'+index+'"></span>');

  var lineID = index;
  var self = $(this);
    setTimeout(function () {
      $.each(self, function(index, chunk){
          setTimeout(function () {
            $('#'+lineID).append("<span>"+chunk+"</span>");
            $('body, html').scrollTop($(document).height());
          }, index*5);
      });

    }, index*100);
}); 
</script>
[over ride ]-#-##]
-----''' * 10)
            time.sleep(1)
            print("PROCESS COMPLETE")
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('Accessing encrypted files...')
            time.sleep(2)
            print('Decrypting....')
            time.sleep(2)
            print('\n\n[-SEN343 LOG-]')
            time.sleep(1)
            print('\n\nOVER-RIDE CODES- HANGAR DROIDS')
            time.sleep(1)
            print('\n\n-Combat Droids - szb41ee')
            time.sleep(1)
            print('\n\n-Sentry Droids - qr66mop')
            time.sleep(1)
            print('\n\n-Repair Droids - yu8xxj3')
            time.sleep(1)
            print('\n\nCODES WILL BE RESET EVERY 24 HOURS')
            security(inventory)
        else:
            print('\n[- ACCESS DENIED -]')
            time.sleep(2)
            security_returning(inventory)

    elif cmd == '3':
        start(inventory)

def security_returning(inventory):
    print('''\nyou are in the Security Deck. \n''')
    print('[-SECURITY-]\n')
    print('1.) View Surveillance monitors of other decks')
    print('2.) Hack Sentry droid 343')
    print('3.) Return to main elevator')

    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        print('\n----------')
        print('\nLoading Terminal....')
        time.sleep(1)
        print('---')
        time.sleep(1)
        print('---')
        time.sleep(1)
        print('Terminal 2 Active.')
        time.sleep(1)
        cam_boot_loop = 1
        while one_locked == 1:
            print('# Terminal 2 Locked #')
            security_password = input('''Enter 1 Digit Password
    ''')
            if security_password == '4':
                print('# UNLOCKED #')
                one_locked = 0
            elif security_attempts < 1:
                print('I give up, just go ')
                one_locked = 0
            else:
                print(security_attempts, '\n Attempts Left')
                security_attempts = security_attempts - 1
                time.sleep(1)
        print('\n[-SURVEILLANCE FEED-]')
        print('''\n-The  Droid Hangar Camera is offline you have no live feed.
    \n-Two drones are entering the Cargo Bay.
    \n-The air lock in the Maintnence Deck has breeched, 
enemy droids and soldiers are pooring in through the breached air lock
    \n-A Large Enemy Command droid Has hyjacked The Bridge.
    \n-The observation deck has a large 3-legged enemy robot and a wounded crew member.''')
        time.sleep(2)
        security(inventory)

    elif cmd == '2':
        if 'droid hack' in inventory:
            print('\nuploading files....')
            time.sleep(2)
            print('....')
            time.sleep(2)
            print('''<html>
        <head>
    <meta charset="utf-8">
    <title>Test</title>
    <link rel="stylesheet" type="text/css" href="spaced.css">
    <link rel="shortcut icon" type="image/png" href="http://test.noa16.png"/>
    <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300' rel='stylesheet' type='text/css'>
    </head>
    <body>
    <p class="text" data-text="test text 010101101010101 lolol whatever"</p>
    <script>
       var printText = $('.text').data('text');

    var contentArray = printText.split('/n');
    $.each(contentArray, function(index, newLine) {
      $('.text').append('<span style="display:block;" id="'+index+'"></span>');

      var lineID = index;
      var self = $(this);
        setTimeout(function () {
          $.each(self, function(index, chunk){
              setTimeout(function () {
                $('#'+lineID).append("<span>"+chunk+"</span>");
                $('body, html').scrollTop($(document).height());
              }, index*5);
          });

        }, index*100);
    }); 
    </script>
    [over ride ]-#-##]
    -----''' * 10)
            time.sleep(1)
            print("PROCESS COMPLETE")
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('Accessing encrypted files...')
            time.sleep(2)
            print('Decrypting....')
            time.sleep(2)
            print('\n\n[-SEN343 LOG-]')
            time.sleep(1)
            print('\n\nOVER-RIDE CODES- HANGAR DROIDS')
            time.sleep(1)
            print('\n\n-Combat Droids - szb41ee')
            time.sleep(1)
            print('\n\n-Sentry Droids - qr66mop')
            time.sleep(1)
            print('\n\n-Repair Droids - yu8xxj3')
            time.sleep(1)
            print('\n\nCODES WILL BE RESET EVERY 24 HOURS')
            security(inventory)
        else:
            print('\n[- ACCESS DENIED -]')
            time.sleep(2)
            security_returning(inventory)

    elif cmd == '3':
        start(inventory)


def observation(inventory):
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('''\nYou enter the Observation deck and are confronted 
with a 3-legged Enemy Sentry Droid in front of a wounded crew member
who is in need of serious medical attention\n''')
    print('[-CHOISE-]\n')
    print('1.) Terminate 3-Legged Sentry Droid')
    print('2.) Retreat to Main Elevator.')

    cmdlist = ['1', '2']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if 'laser' and 'laser pistol sight' in inventory:
            print('\nlaser active...')
            time.sleep(1)
            print('target locked...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('\n[- TARGET TERMINATED -]\n')
            items = ['laser']
            item = ['armour']
            if len(items) > 0:
                for item in items:
                    item = ['armour']
                    print('\n--> %s' % (item))
            else:
                item = ['armour']
                print('\n--> %s' % (item), ', made from the thick steel shell of the 3-legged sentry droid\n')
                print('')
            inventory.append('armour')
            item = ['armour']
        elif 'laser' in inventory and 'laser pistol sight' not in inventory:
            print('LASER CHARGING')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('you missed')
            time.sleep(.5)
            print('''the three legged sentry droid fires it's laser cannon with pin point acuracy
turning you into a pile of ash''')
            time.sleep(1)
            print('[- YOU LOSE -]')
            time.sleep(.5)
            print('tip: next time collect the sight sight item')
        else:
            print('\n[- WARNING NO WEAPON IN INVENTORY -]')
            time.sleep(2)
            print('''\nThe Sentry Droids is charging it's laser..''')
            answer = input('''1.) Retreat
2.) Try to disable it's laser cannon before it can fire''')
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            if cmd =='1':
                print('[- RETREAT SUCESSFUL -]')
                start(inventory)
            else:
                print("""You run at the droid as fast as you can and reach for it's laser,
but it's too late""")
                time.sleep(1)
                print('....')
                time.sleep(1)
                print('every thing is going dark')
                time.sleep(1)
                print('[-GAME OVER-]')
                exit(0)
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('[- YOU LOSE -]')
            time.sleep(1)
            print('\nGAME OVER\n')
            exit(0)

    elif cmd == '2':
        print('''\nThe Sentry droids laser is now active and has you locked
on. You try to retreat to the main elevator but its to late..''')
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('[- YOU LOSE -]')
        time.sleep(1)
        print('\nGAME OVER\n')
        exit(0)


def enemy_sentry(inventory, items=['sight']):
    print('\n----------')
    time.sleep(1)
    item = ['sight']
    print('''\nThe Enemy Sentry droid has been terminated. 
you notice he has a sight on his laser pistol
You take the sight for later use''')
    if len(items) > 0:
        for item in items:
            item = ['laser pistol sight']
            print('\n--> %s' % (item))
    else:
        item = ['laser pistol sight']
        print('\n--> %s' % (item),'\n')
    inventory.append('laser pistol sight')
    item = ['sight']
    time.sleep(1)
    print('asight auto repair intiated.')
    time.sleep(1)
    print('downloading..')
    time.sleep(1)
    time.sleep(1)
    print('Auto alignment initiated...')
    time.sleep(1)
    print('....')
    time.sleep(2)

    print('\nSIGHT ONLINE.')
    time.sleep(2)
    print('''\n
You return to the main elevator''')
    start(inventory)

def shuttle_control(inventory):
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('''\nYou enter The Bridge where the captain 
sets the ships course at the beguining of the voyage.
A gen 9 Elite Enemy Command droid is posted here.
This Droid is extremely powerfull.''')
    print('\n[-SHUTTLE CONTROL-]')
    print('''\n1.) terminate the gen 9 Elite Enemy Command Droid
if you have a gun,hack and sight this means fight it. if not this means hack it''')
    print('2.) Retreat to Main Elevator')
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)

    if cmd == '1':
        if 'laser' in inventory and 'laser pistol sight' in inventory and 'droid hack' in inventory:
            print('\n....')
            time.sleep(1)
            print('\n....')
            command_droid(inventory)
        else:
            time.sleep(1)
            print('\nEECD999:>')
            print('\n100101010101010101010101010101010' * 10)
            time.sleep(1)
            print('''\nThe Elite Enemy Command droid laughs in machine language
at your pathetic attempt. The last thing you hear is the
deafing sound of a Target Lock.''')
            print('....')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('\n[- YOU LOSE -]')
            time.sleep(1)
            print('\nGAME OVER\n')
            exit(0)
    elif cmd == '2':
        start(inventory)
    else:
        start(inventory)


def command_droid(inventory):
    print('\nRunning droid hack...')
    time.sleep(1)
    print('\njamming EECD999 Target Lock...')
    time.sleep(1)
    print('\n......')
    time.sleep(1)
    print('\nAuto sight active...')
    time.sleep(1)
    print('\nTracking motion of droid #EECD999...')
    time.sleep(.5)
    print('\n......')
    time.sleep(.5)
    print('\nLaser active...')
    time.sleep(1)
    print('\nTargeting EECD999...')
    time.sleep(1)
    print('\nTarget Locked...')
    time.sleep(1)
    print('\n......')
    time.sleep(2)
    print('\n\[- nTARGET TERMINATED -]\n')
    time.sleep(1)
    print('''\n\nYou have defeated the EECD999 droid and taken back control
of the inter stelar star ship 'Hermes'. The flight path has been restored and
a distress signal sent on the emergency space frequency during the 5 minutes of
inter planetary silence. Help is n it's way.''')
    time.sleep(3)
    print('\n [- GAME OVER -]\n')
    time.sleep(1)
    print('[- YOU WIN -]')
    quit(0)

def getcmd(cmdlist):
    cmd = input('\nCTRL866:> ')
    if cmd in cmdlist:
        return cmd
    elif cmd == 'help':
        print('\nTYPE: inventory to view items')
        print('or quit to quit')
        return getcmd(cmdlist)
    elif cmd == 'inventory':
        print('\ninventory contains:\n')
        for item in inventory:
            print('-- %s' % (item))
        return getcmd(cmdlist)
    elif cmd == 'secret':
        print('\n........')
        time.sleep(1)
        print('\n[-- OWEN inc.-- by:OWEN BASORE--]')
        time.sleep(1)
        print('\n........\n')
        return getcmd(cmdlist)
    elif cmd == 'quit':
        print('\n----------')
        exit(0)
    else:
        print('\n   /ERROR/ [-invalid command-]\n')
        return getcmd(cmdlist)


if __name__ == "__main__":
    inventory = ['service port']
    print('\n----------')
    print('\nMoving..')
    print('\n----------')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('\n-[/ Map /]-')
    print('\n1.) deck 1 - Security')
    print('2.) deck 2 - Maintenance')
    print('3.) deck 3 - Cargo Bay - Airlock')
    print('4.) deck 4 - Droid Deck')
    print('5.) deck 5 - Shuttle Control')
    print('6.) deck 6 - Observation')
    time.sleep(1)
    print('''
....
....
        ''')
    cmdlist = ['1', '2', '3', '4', '5', '6', ]
    cmd = getcmd(cmdlist)

    if cmd == '1':
        security(inventory)
    elif cmd == '2':
        if 'droid hack' in inventory:
            print('\n- DECK 2 - MAINTENANCE LOCKED -')
            time.sleep(2)
            start(inventory)
        else:
            maintenance(inventory)
    elif cmd == '3':
        cargo_hold(inventory)
    elif cmd == '4':
        if 'laser' in inventory:
            print('\n- DECK 4 - DROID HANGAR LOCKED -')
            time.sleep(2)
            start(inventory)
        else:
            droid_hangar(inventory)
    elif cmd == '5':
        shuttle_control(inventory)
    elif cmd == '6':
        if 'motion tracker' in inventory:
            print('\n- DECK 6 - OBSERVATION LOCKED -')
            time.sleep(2)
            start(inventory)
        else:
            observation(inventory)
