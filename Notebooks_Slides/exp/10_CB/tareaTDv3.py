#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Tue Nov 10 20:12:18 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'ninosDelConv2'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/coreyziemba/Desktop/DD_Rosario/tareaTDv3.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Inst1"
Inst1Clock = core.Clock()
intro1 = visual.TextStim(win=win, name='intro1',
    text='A continuación vas a completar una tarea computarizada en la que tomarás una serie de decisiones.\n\nPresiona la barra de espacio para continuar.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key1 = keyboard.Keyboard()

# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
intro2 = visual.TextStim(win=win, name='intro2',
    text='Todas las decisiones que tendrás que tomar serán elecciones entre dos opciones de recompensas monetarias que podrías recibir: una opción de dinero que obtendrías hoy contra una opción de dinero que obtendrías en el futuro. \n\nEn cada pregunta, las cantidades de dinero ofrecido y el número de días que habría que esperar en el futuro cambiarán. \n\nEn cada pregunta, la opción inmediata y la  opción futura cambiarán de lado en la pantalla, así que debes poner atención para responder con el teclado cuál es tu preferencia.',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key2 = keyboard.Keyboard()

# Initialize components for Routine "Inst2_2"
Inst2_2Clock = core.Clock()
intro2_2 = visual.TextStim(win=win, name='intro2_2',
    text='Aunque estas decisiones son hipotéticas, te pedimos que hagas cada elección con honestidad, es decir, que respondas cuál es tu verdadera preferencia tal y como si fuéramos a darte el dinero que escogiste en la fecha en la que escogiste.\n\nEs muy importante que sepas que en esta tarea NO HAY respuestas correctas o incorrectas, cada pregunta es sobre TU preferencia, así que tus respuestas pueden ser muy distintas de las de otra persona. Por este motivo, te recomendamos que contestes con sinceridad para que tus respuestas reflejen tus preferencias únicas.',
    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key2_2 = keyboard.Keyboard()

# Initialize components for Routine "Inst2_3"
Inst2_3Clock = core.Clock()
Intro2_3 = visual.TextStim(win=win, name='Intro2_3',
    text='Si escoges la opción de la izquierda oprime la flecha hacia la izquierda, si escoges la opción de la derecha oprime la flecha hacia la derecha',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key2_3 = keyboard.Keyboard()

# Initialize components for Routine "Inst3"
Inst3Clock = core.Clock()
key3 = keyboard.Keyboard()
intro3 = visual.TextStim(win=win, name='intro3',
    text='Por ejemplo, ¿qué preferirías?',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ss_am = visual.TextStim(win=win, name='ss_am',
    text='$5.000',
    font='Arial',
    pos=[-0.5,0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ss_del = visual.TextStim(win=win, name='ss_del',
    text='hoy',
    font='Arial',
    pos=[-0.5, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ll_am = visual.TextStim(win=win, name='ll_am',
    text='$10.000',
    font='Arial',
    pos=[0.5, 0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ll_del = visual.TextStim(win=win, name='ll_del',
    text='en 7 días',
    font='Arial',
    pos=[0.5, -0.1], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Inst4"
Inst4Clock = core.Clock()
Intro4 = visual.TextStim(win=win, name='Intro4',
    text='Hagamos unos ensayos de práctica',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key4 = keyboard.Keyboard()

# Initialize components for Routine "Pract"
PractClock = core.Clock()
# specify default vars 
targetPosAmSS = [] 
targetPosAmLL = [] 
targetPosDelSS = [] 
targetPosDelLL = []  
# specify lists of stimulus positions and their corresponding responses: 
positionsAm = [[-0.5,0.1], [0.5,0.1]] 
positionsDel = [[-0.5,-0.1], [0.5,-0.1]] 
responses = ['left', 'right']
   
# create a list of indices to those lists, which will 
# get shuffled on each trial: 
indices = [0, 1]
pregunta = visual.TextStim(win=win, name='pregunta',
    text='¿qué preferirías?',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ssAm_P = visual.TextStim(win=win, name='ssAm_P',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ssDel_P = visual.TextStim(win=win, name='ssDel_P',
    text='hoy',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
llAm_P = visual.TextStim(win=win, name='llAm_P',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
llDel_P = visual.TextStim(win=win, name='llDel_P',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
respP = keyboard.Keyboard()

# Initialize components for Routine "fb_Pract"
fb_PractClock = core.Clock()
#some value for msg!
msg=''
feedbackP = visual.TextStim(win=win, name='feedbackP',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instr5"
Instr5Clock = core.Clock()
comienzo = visual.TextStim(win=win, name='comienzo',
    text='Ahora sí vamos a empezar con la tarea. Recuerda que debes contestar todas las preguntas. Tienes 20 segundos por cada pregunta. ',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key5 = keyboard.Keyboard()

# Initialize components for Routine "ITC"
ITCClock = core.Clock()
# specify default vars
targetPosAmSS = []
targetPosAmLL = []
targetPosDelSS = []
targetPosDelLL = []

# specify lists of stimulus positions and their corresponding responses:
positionsAm = [[-0.5,0.1], [0.5,0.1]]
positionsDel = [[-0.5,-0.1], [0.5,-0.1]]
responses = ['left', 'right'] 

# create a list of indices to those lists, which will
# get shuffled on each trial:
indices = [0, 1]
preguntaT = visual.TextStim(win=win, name='preguntaT',
    text='¿qué preferirías?',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ssAm_T = visual.TextStim(win=win, name='ssAm_T',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ssDel_T = visual.TextStim(win=win, name='ssDel_T',
    text='hoy',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
llAm_T = visual.TextStim(win=win, name='llAm_T',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
llDel_T = visual.TextStim(win=win, name='llDel_T',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
respT = keyboard.Keyboard()

# Initialize components for Routine "fb_Trials"
fb_TrialsClock = core.Clock()
#some value for msg!
msg=''
textfbT = visual.TextStim(win=win, name='textfbT',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fin"
FinClock = core.Clock()
Gracias = visual.TextStim(win=win, name='Gracias',
    text='Terminaste!\n\nMuchas gracias por participar!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Inst1"-------
continueRoutine = True
# update component parameters for each repeat
key1.keys = []
key1.rt = []
_key1_allKeys = []
# keep track of which components have finished
Inst1Components = [intro1, key1]
for thisComponent in Inst1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inst1"-------
while continueRoutine:
    # get current time
    t = Inst1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *key1* updates
    waitOnFlip = False
    if key1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key1.frameNStart = frameN  # exact frame index
        key1.tStart = t  # local t and not account for scr refresh
        key1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key1, 'tStartRefresh')  # time at next scr refresh
        key1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key1.status == STARTED and not waitOnFlip:
        theseKeys = key1.getKeys(keyList=['space'], waitRelease=False)
        _key1_allKeys.extend(theseKeys)
        if len(_key1_allKeys):
            key1.keys = _key1_allKeys[-1].name  # just the last key pressed
            key1.rt = _key1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst1"-------
for thisComponent in Inst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro1.started', intro1.tStartRefresh)
thisExp.addData('intro1.stopped', intro1.tStopRefresh)
# check responses
if key1.keys in ['', [], None]:  # No response was made
    key1.keys = None
thisExp.addData('key1.keys',key1.keys)
if key1.keys != None:  # we had a response
    thisExp.addData('key1.rt', key1.rt)
thisExp.addData('key1.started', key1.tStartRefresh)
thisExp.addData('key1.stopped', key1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr2"-------
continueRoutine = True
# update component parameters for each repeat
key2.keys = []
key2.rt = []
_key2_allKeys = []
# keep track of which components have finished
Instr2Components = [intro2, key2]
for thisComponent in Instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr2"-------
while continueRoutine:
    # get current time
    t = Instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro2* updates
    if intro2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        intro2.frameNStart = frameN  # exact frame index
        intro2.tStart = t  # local t and not account for scr refresh
        intro2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro2, 'tStartRefresh')  # time at next scr refresh
        intro2.setAutoDraw(True)
    
    # *key2* updates
    waitOnFlip = False
    if key2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key2.frameNStart = frameN  # exact frame index
        key2.tStart = t  # local t and not account for scr refresh
        key2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key2, 'tStartRefresh')  # time at next scr refresh
        key2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key2.status == STARTED and not waitOnFlip:
        theseKeys = key2.getKeys(keyList=['space'], waitRelease=False)
        _key2_allKeys.extend(theseKeys)
        if len(_key2_allKeys):
            key2.keys = _key2_allKeys[-1].name  # just the last key pressed
            key2.rt = _key2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr2"-------
for thisComponent in Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro2.started', intro2.tStartRefresh)
thisExp.addData('intro2.stopped', intro2.tStopRefresh)
# check responses
if key2.keys in ['', [], None]:  # No response was made
    key2.keys = None
thisExp.addData('key2.keys',key2.keys)
if key2.keys != None:  # we had a response
    thisExp.addData('key2.rt', key2.rt)
thisExp.addData('key2.started', key2.tStartRefresh)
thisExp.addData('key2.stopped', key2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst2_2"-------
continueRoutine = True
# update component parameters for each repeat
key2_2.keys = []
key2_2.rt = []
_key2_2_allKeys = []
# keep track of which components have finished
Inst2_2Components = [intro2_2, key2_2]
for thisComponent in Inst2_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inst2_2"-------
while continueRoutine:
    # get current time
    t = Inst2_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst2_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro2_2* updates
    if intro2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro2_2.frameNStart = frameN  # exact frame index
        intro2_2.tStart = t  # local t and not account for scr refresh
        intro2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro2_2, 'tStartRefresh')  # time at next scr refresh
        intro2_2.setAutoDraw(True)
    
    # *key2_2* updates
    waitOnFlip = False
    if key2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key2_2.frameNStart = frameN  # exact frame index
        key2_2.tStart = t  # local t and not account for scr refresh
        key2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key2_2, 'tStartRefresh')  # time at next scr refresh
        key2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key2_2.status == STARTED and not waitOnFlip:
        theseKeys = key2_2.getKeys(keyList=['space'], waitRelease=False)
        _key2_2_allKeys.extend(theseKeys)
        if len(_key2_2_allKeys):
            key2_2.keys = _key2_2_allKeys[-1].name  # just the last key pressed
            key2_2.rt = _key2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst2_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst2_2"-------
for thisComponent in Inst2_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro2_2.started', intro2_2.tStartRefresh)
thisExp.addData('intro2_2.stopped', intro2_2.tStopRefresh)
# check responses
if key2_2.keys in ['', [], None]:  # No response was made
    key2_2.keys = None
thisExp.addData('key2_2.keys',key2_2.keys)
if key2_2.keys != None:  # we had a response
    thisExp.addData('key2_2.rt', key2_2.rt)
thisExp.addData('key2_2.started', key2_2.tStartRefresh)
thisExp.addData('key2_2.stopped', key2_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst2_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst2_3"-------
continueRoutine = True
# update component parameters for each repeat
key2_3.keys = []
key2_3.rt = []
_key2_3_allKeys = []
# keep track of which components have finished
Inst2_3Components = [Intro2_3, key2_3]
for thisComponent in Inst2_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst2_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inst2_3"-------
while continueRoutine:
    # get current time
    t = Inst2_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst2_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro2_3* updates
    if Intro2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro2_3.frameNStart = frameN  # exact frame index
        Intro2_3.tStart = t  # local t and not account for scr refresh
        Intro2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro2_3, 'tStartRefresh')  # time at next scr refresh
        Intro2_3.setAutoDraw(True)
    
    # *key2_3* updates
    waitOnFlip = False
    if key2_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key2_3.frameNStart = frameN  # exact frame index
        key2_3.tStart = t  # local t and not account for scr refresh
        key2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key2_3, 'tStartRefresh')  # time at next scr refresh
        key2_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key2_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key2_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key2_3.status == STARTED and not waitOnFlip:
        theseKeys = key2_3.getKeys(keyList=['space'], waitRelease=False)
        _key2_3_allKeys.extend(theseKeys)
        if len(_key2_3_allKeys):
            key2_3.keys = _key2_3_allKeys[-1].name  # just the last key pressed
            key2_3.rt = _key2_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst2_3"-------
for thisComponent in Inst2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro2_3.started', Intro2_3.tStartRefresh)
thisExp.addData('Intro2_3.stopped', Intro2_3.tStopRefresh)
# check responses
if key2_3.keys in ['', [], None]:  # No response was made
    key2_3.keys = None
thisExp.addData('key2_3.keys',key2_3.keys)
if key2_3.keys != None:  # we had a response
    thisExp.addData('key2_3.rt', key2_3.rt)
thisExp.addData('key2_3.started', key2_3.tStartRefresh)
thisExp.addData('key2_3.stopped', key2_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst2_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst3"-------
continueRoutine = True
# update component parameters for each repeat
key3.keys = []
key3.rt = []
_key3_allKeys = []
# keep track of which components have finished
Inst3Components = [key3, intro3, ss_am, ss_del, ll_am, ll_del]
for thisComponent in Inst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inst3"-------
while continueRoutine:
    # get current time
    t = Inst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key3* updates
    waitOnFlip = False
    if key3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key3.frameNStart = frameN  # exact frame index
        key3.tStart = t  # local t and not account for scr refresh
        key3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key3, 'tStartRefresh')  # time at next scr refresh
        key3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key3.status == STARTED and not waitOnFlip:
        theseKeys = key3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key3_allKeys.extend(theseKeys)
        if len(_key3_allKeys):
            key3.keys = _key3_allKeys[-1].name  # just the last key pressed
            key3.rt = _key3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intro3* updates
    if intro3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro3.frameNStart = frameN  # exact frame index
        intro3.tStart = t  # local t and not account for scr refresh
        intro3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro3, 'tStartRefresh')  # time at next scr refresh
        intro3.setAutoDraw(True)
    
    # *ss_am* updates
    if ss_am.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ss_am.frameNStart = frameN  # exact frame index
        ss_am.tStart = t  # local t and not account for scr refresh
        ss_am.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ss_am, 'tStartRefresh')  # time at next scr refresh
        ss_am.setAutoDraw(True)
    
    # *ss_del* updates
    if ss_del.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ss_del.frameNStart = frameN  # exact frame index
        ss_del.tStart = t  # local t and not account for scr refresh
        ss_del.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ss_del, 'tStartRefresh')  # time at next scr refresh
        ss_del.setAutoDraw(True)
    
    # *ll_am* updates
    if ll_am.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ll_am.frameNStart = frameN  # exact frame index
        ll_am.tStart = t  # local t and not account for scr refresh
        ll_am.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ll_am, 'tStartRefresh')  # time at next scr refresh
        ll_am.setAutoDraw(True)
    
    # *ll_del* updates
    if ll_del.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ll_del.frameNStart = frameN  # exact frame index
        ll_del.tStart = t  # local t and not account for scr refresh
        ll_del.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ll_del, 'tStartRefresh')  # time at next scr refresh
        ll_del.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst3"-------
for thisComponent in Inst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key3.keys in ['', [], None]:  # No response was made
    key3.keys = None
thisExp.addData('key3.keys',key3.keys)
if key3.keys != None:  # we had a response
    thisExp.addData('key3.rt', key3.rt)
thisExp.addData('key3.started', key3.tStartRefresh)
thisExp.addData('key3.stopped', key3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('intro3.started', intro3.tStartRefresh)
thisExp.addData('intro3.stopped', intro3.tStopRefresh)
thisExp.addData('ss_am.started', ss_am.tStartRefresh)
thisExp.addData('ss_am.stopped', ss_am.tStopRefresh)
thisExp.addData('ss_del.started', ss_del.tStartRefresh)
thisExp.addData('ss_del.stopped', ss_del.tStopRefresh)
thisExp.addData('ll_am.started', ll_am.tStartRefresh)
thisExp.addData('ll_am.stopped', ll_am.tStopRefresh)
thisExp.addData('ll_del.started', ll_del.tStartRefresh)
thisExp.addData('ll_del.stopped', ll_del.tStopRefresh)
# the Routine "Inst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst4"-------
continueRoutine = True
# update component parameters for each repeat
key4.keys = []
key4.rt = []
_key4_allKeys = []
# keep track of which components have finished
Inst4Components = [Intro4, key4]
for thisComponent in Inst4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Inst4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Inst4"-------
while continueRoutine:
    # get current time
    t = Inst4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Inst4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro4* updates
    if Intro4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro4.frameNStart = frameN  # exact frame index
        Intro4.tStart = t  # local t and not account for scr refresh
        Intro4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro4, 'tStartRefresh')  # time at next scr refresh
        Intro4.setAutoDraw(True)
    
    # *key4* updates
    waitOnFlip = False
    if key4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key4.frameNStart = frameN  # exact frame index
        key4.tStart = t  # local t and not account for scr refresh
        key4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key4, 'tStartRefresh')  # time at next scr refresh
        key4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key4.status == STARTED and not waitOnFlip:
        theseKeys = key4.getKeys(keyList=['space'], waitRelease=False)
        _key4_allKeys.extend(theseKeys)
        if len(_key4_allKeys):
            key4.keys = _key4_allKeys[-1].name  # just the last key pressed
            key4.rt = _key4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Inst4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst4"-------
for thisComponent in Inst4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro4.started', Intro4.tStartRefresh)
thisExp.addData('Intro4.stopped', Intro4.tStopRefresh)
# check responses
if key4.keys in ['', [], None]:  # No response was made
    key4.keys = None
thisExp.addData('key4.keys',key4.keys)
if key4.keys != None:  # we had a response
    thisExp.addData('key4.rt', key4.rt)
thisExp.addData('key4.started', key4.tStartRefresh)
thisExp.addData('key4.stopped', key4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Inst4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choiceSet_practice.xlsx'),
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Pract"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # randomise locations for this trial: 
    shuffle(indices)
    targetPosAmSS = positionsAm[indices[0]] 
    targetPosAmLL = positionsAm[indices[1]] 
    targetPosDelSS = positionsDel[indices[0]] 
    targetPosDelLL = positionsDel[indices[1]]      
    # get the corresponding correct response: 
    corrAns = responses[indices[1]]
    ssAm_P.setPos(targetPosAmSS)
    ssAm_P.setText('ssAmount')
    ssDel_P.setPos(targetPosDelSS)
    llAm_P.setPos(targetPosAmLL)
    llAm_P.setText('llAmount')
    llDel_P.setPos(targetPosDelLL)
    llDel_P.setText('llDelay')
    respP.keys = []
    respP.rt = []
    _respP_allKeys = []
    # keep track of which components have finished
    PractComponents = [pregunta, ssAm_P, ssDel_P, llAm_P, llDel_P, respP]
    for thisComponent in PractComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PractClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pract"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PractClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PractClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pregunta* updates
        if pregunta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pregunta.frameNStart = frameN  # exact frame index
            pregunta.tStart = t  # local t and not account for scr refresh
            pregunta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pregunta, 'tStartRefresh')  # time at next scr refresh
            pregunta.setAutoDraw(True)
        if pregunta.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pregunta.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                pregunta.tStop = t  # not accounting for scr refresh
                pregunta.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pregunta, 'tStopRefresh')  # time at next scr refresh
                pregunta.setAutoDraw(False)
        
        # *ssAm_P* updates
        if ssAm_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ssAm_P.frameNStart = frameN  # exact frame index
            ssAm_P.tStart = t  # local t and not account for scr refresh
            ssAm_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ssAm_P, 'tStartRefresh')  # time at next scr refresh
            ssAm_P.setAutoDraw(True)
        if ssAm_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ssAm_P.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ssAm_P.tStop = t  # not accounting for scr refresh
                ssAm_P.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ssAm_P, 'tStopRefresh')  # time at next scr refresh
                ssAm_P.setAutoDraw(False)
        
        # *ssDel_P* updates
        if ssDel_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ssDel_P.frameNStart = frameN  # exact frame index
            ssDel_P.tStart = t  # local t and not account for scr refresh
            ssDel_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ssDel_P, 'tStartRefresh')  # time at next scr refresh
            ssDel_P.setAutoDraw(True)
        if ssDel_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ssDel_P.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ssDel_P.tStop = t  # not accounting for scr refresh
                ssDel_P.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ssDel_P, 'tStopRefresh')  # time at next scr refresh
                ssDel_P.setAutoDraw(False)
        
        # *llAm_P* updates
        if llAm_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            llAm_P.frameNStart = frameN  # exact frame index
            llAm_P.tStart = t  # local t and not account for scr refresh
            llAm_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(llAm_P, 'tStartRefresh')  # time at next scr refresh
            llAm_P.setAutoDraw(True)
        if llAm_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > llAm_P.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                llAm_P.tStop = t  # not accounting for scr refresh
                llAm_P.frameNStop = frameN  # exact frame index
                win.timeOnFlip(llAm_P, 'tStopRefresh')  # time at next scr refresh
                llAm_P.setAutoDraw(False)
        
        # *llDel_P* updates
        if llDel_P.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            llDel_P.frameNStart = frameN  # exact frame index
            llDel_P.tStart = t  # local t and not account for scr refresh
            llDel_P.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(llDel_P, 'tStartRefresh')  # time at next scr refresh
            llDel_P.setAutoDraw(True)
        if llDel_P.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > llDel_P.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                llDel_P.tStop = t  # not accounting for scr refresh
                llDel_P.frameNStop = frameN  # exact frame index
                win.timeOnFlip(llDel_P, 'tStopRefresh')  # time at next scr refresh
                llDel_P.setAutoDraw(False)
        
        # *respP* updates
        waitOnFlip = False
        if respP.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respP.frameNStart = frameN  # exact frame index
            respP.tStart = t  # local t and not account for scr refresh
            respP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respP, 'tStartRefresh')  # time at next scr refresh
            respP.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respP.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respP.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respP.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respP.tStartRefresh + 19.5-frameTolerance:
                # keep track of stop time/frame for later
                respP.tStop = t  # not accounting for scr refresh
                respP.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respP, 'tStopRefresh')  # time at next scr refresh
                respP.status = FINISHED
        if respP.status == STARTED and not waitOnFlip:
            theseKeys = respP.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respP_allKeys.extend(theseKeys)
            if len(_respP_allKeys):
                respP.keys = _respP_allKeys[-1].name  # just the last key pressed
                respP.rt = _respP_allKeys[-1].rt
                # was this correct?
                if (respP.keys == str(corrAns)) or (respP.keys == corrAns):
                    respP.corr = 1
                else:
                    respP.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PractComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pract"-------
    for thisComponent in PractComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('pregunta.started', pregunta.tStartRefresh)
    Practice.addData('pregunta.stopped', pregunta.tStopRefresh)
    Practice.addData('ssAm_P.started', ssAm_P.tStartRefresh)
    Practice.addData('ssAm_P.stopped', ssAm_P.tStopRefresh)
    Practice.addData('ssDel_P.started', ssDel_P.tStartRefresh)
    Practice.addData('ssDel_P.stopped', ssDel_P.tStopRefresh)
    Practice.addData('llAm_P.started', llAm_P.tStartRefresh)
    Practice.addData('llAm_P.stopped', llAm_P.tStopRefresh)
    Practice.addData('llDel_P.started', llDel_P.tStartRefresh)
    Practice.addData('llDel_P.stopped', llDel_P.tStopRefresh)
    # check responses
    if respP.keys in ['', [], None]:  # No response was made
        respP.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           respP.corr = 1;  # correct non-response
        else:
           respP.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice (TrialHandler)
    Practice.addData('respP.keys',respP.keys)
    Practice.addData('respP.corr', respP.corr)
    if respP.keys != None:  # we had a response
        Practice.addData('respP.rt', respP.rt)
    Practice.addData('respP.started', respP.tStartRefresh)
    Practice.addData('respP.stopped', respP.tStopRefresh)
    
    # ------Prepare to start Routine "fb_Pract"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if not respP.keys :
         msg="No respondiste a tiempo!" 
    elif respP.corr:#stored on last run routine
         msg="Elegiste esperar"  
    else:
         msg="Elegiste no esperar"
    feedbackP.setText(msg)
    # keep track of which components have finished
    fb_PractComponents = [feedbackP]
    for thisComponent in fb_PractComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fb_PractClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fb_Pract"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fb_PractClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fb_PractClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackP* updates
        if feedbackP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackP.frameNStart = frameN  # exact frame index
            feedbackP.tStart = t  # local t and not account for scr refresh
            feedbackP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackP, 'tStartRefresh')  # time at next scr refresh
            feedbackP.setAutoDraw(True)
        if feedbackP.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackP.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                feedbackP.tStop = t  # not accounting for scr refresh
                feedbackP.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackP, 'tStopRefresh')  # time at next scr refresh
                feedbackP.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fb_PractComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fb_Pract"-------
    for thisComponent in fb_PractComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('feedbackP.started', feedbackP.tStartRefresh)
    Practice.addData('feedbackP.stopped', feedbackP.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'


# ------Prepare to start Routine "Instr5"-------
continueRoutine = True
# update component parameters for each repeat
key5.keys = []
key5.rt = []
_key5_allKeys = []
# keep track of which components have finished
Instr5Components = [comienzo, key5]
for thisComponent in Instr5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr5"-------
while continueRoutine:
    # get current time
    t = Instr5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *comienzo* updates
    if comienzo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        comienzo.frameNStart = frameN  # exact frame index
        comienzo.tStart = t  # local t and not account for scr refresh
        comienzo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(comienzo, 'tStartRefresh')  # time at next scr refresh
        comienzo.setAutoDraw(True)
    
    # *key5* updates
    waitOnFlip = False
    if key5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key5.frameNStart = frameN  # exact frame index
        key5.tStart = t  # local t and not account for scr refresh
        key5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key5, 'tStartRefresh')  # time at next scr refresh
        key5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key5.status == STARTED and not waitOnFlip:
        theseKeys = key5.getKeys(keyList=['g'], waitRelease=False)
        _key5_allKeys.extend(theseKeys)
        if len(_key5_allKeys):
            key5.keys = _key5_allKeys[-1].name  # just the last key pressed
            key5.rt = _key5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr5"-------
for thisComponent in Instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('comienzo.started', comienzo.tStartRefresh)
thisExp.addData('comienzo.stopped', comienzo.tStopRefresh)
# check responses
if key5.keys in ['', [], None]:  # No response was made
    key5.keys = None
thisExp.addData('key5.keys',key5.keys)
if key5.keys != None:  # we had a response
    thisExp.addData('key5.rt', key5.rt)
thisExp.addData('key5.started', key5.tStartRefresh)
thisExp.addData('key5.stopped', key5.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choiceSet_trials.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITC"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # randomise locations for this trial:
    shuffle(indices)
        
    targetPosAmSS = positionsAm[indices[0]]
    targetPosAmLL = positionsAm[indices[1]]
    targetPosDelSS = positionsDel[indices[0]]
    targetPosDelLL = positionsDel[indices[1]]
        
    # get the corresponding correct response:
    corrAns = responses[indices[1]]
    ssAm_T.setPos(targetPosAmSS)
    ssAm_T.setText('ss_Amt')
    ssDel_T.setPos(targetPosDelSS)
    llAm_T.setPos(targetPosAmLL)
    llAm_T.setText('ll_Amt')
    llDel_T.setPos(targetPosDelLL)
    llDel_T.setText('ll_Delay')
    respT.keys = []
    respT.rt = []
    _respT_allKeys = []
    # keep track of which components have finished
    ITCComponents = [preguntaT, ssAm_T, ssDel_T, llAm_T, llDel_T, respT]
    for thisComponent in ITCComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITC"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITCClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITCClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preguntaT* updates
        if preguntaT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preguntaT.frameNStart = frameN  # exact frame index
            preguntaT.tStart = t  # local t and not account for scr refresh
            preguntaT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preguntaT, 'tStartRefresh')  # time at next scr refresh
            preguntaT.setAutoDraw(True)
        if preguntaT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > preguntaT.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                preguntaT.tStop = t  # not accounting for scr refresh
                preguntaT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(preguntaT, 'tStopRefresh')  # time at next scr refresh
                preguntaT.setAutoDraw(False)
        
        # *ssAm_T* updates
        if ssAm_T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ssAm_T.frameNStart = frameN  # exact frame index
            ssAm_T.tStart = t  # local t and not account for scr refresh
            ssAm_T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ssAm_T, 'tStartRefresh')  # time at next scr refresh
            ssAm_T.setAutoDraw(True)
        if ssAm_T.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ssAm_T.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ssAm_T.tStop = t  # not accounting for scr refresh
                ssAm_T.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ssAm_T, 'tStopRefresh')  # time at next scr refresh
                ssAm_T.setAutoDraw(False)
        
        # *ssDel_T* updates
        if ssDel_T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ssDel_T.frameNStart = frameN  # exact frame index
            ssDel_T.tStart = t  # local t and not account for scr refresh
            ssDel_T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ssDel_T, 'tStartRefresh')  # time at next scr refresh
            ssDel_T.setAutoDraw(True)
        if ssDel_T.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ssDel_T.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                ssDel_T.tStop = t  # not accounting for scr refresh
                ssDel_T.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ssDel_T, 'tStopRefresh')  # time at next scr refresh
                ssDel_T.setAutoDraw(False)
        
        # *llAm_T* updates
        if llAm_T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            llAm_T.frameNStart = frameN  # exact frame index
            llAm_T.tStart = t  # local t and not account for scr refresh
            llAm_T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(llAm_T, 'tStartRefresh')  # time at next scr refresh
            llAm_T.setAutoDraw(True)
        if llAm_T.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > llAm_T.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                llAm_T.tStop = t  # not accounting for scr refresh
                llAm_T.frameNStop = frameN  # exact frame index
                win.timeOnFlip(llAm_T, 'tStopRefresh')  # time at next scr refresh
                llAm_T.setAutoDraw(False)
        
        # *llDel_T* updates
        if llDel_T.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            llDel_T.frameNStart = frameN  # exact frame index
            llDel_T.tStart = t  # local t and not account for scr refresh
            llDel_T.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(llDel_T, 'tStartRefresh')  # time at next scr refresh
            llDel_T.setAutoDraw(True)
        if llDel_T.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > llDel_T.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                llDel_T.tStop = t  # not accounting for scr refresh
                llDel_T.frameNStop = frameN  # exact frame index
                win.timeOnFlip(llDel_T, 'tStopRefresh')  # time at next scr refresh
                llDel_T.setAutoDraw(False)
        
        # *respT* updates
        waitOnFlip = False
        if respT.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            respT.frameNStart = frameN  # exact frame index
            respT.tStart = t  # local t and not account for scr refresh
            respT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respT, 'tStartRefresh')  # time at next scr refresh
            respT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > respT.tStartRefresh + 19.5-frameTolerance:
                # keep track of stop time/frame for later
                respT.tStop = t  # not accounting for scr refresh
                respT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respT, 'tStopRefresh')  # time at next scr refresh
                respT.status = FINISHED
        if respT.status == STARTED and not waitOnFlip:
            theseKeys = respT.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respT_allKeys.extend(theseKeys)
            if len(_respT_allKeys):
                respT.keys = _respT_allKeys[-1].name  # just the last key pressed
                respT.rt = _respT_allKeys[-1].rt
                # was this correct?
                if (respT.keys == str(corrAns)) or (respT.keys == corrAns):
                    respT.corr = 1
                else:
                    respT.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITCComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITC"-------
    for thisComponent in ITCComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('preguntaT.started', preguntaT.tStartRefresh)
    trials.addData('preguntaT.stopped', preguntaT.tStopRefresh)
    trials.addData('ssAm_T.started', ssAm_T.tStartRefresh)
    trials.addData('ssAm_T.stopped', ssAm_T.tStopRefresh)
    trials.addData('ssDel_T.started', ssDel_T.tStartRefresh)
    trials.addData('ssDel_T.stopped', ssDel_T.tStopRefresh)
    trials.addData('llAm_T.started', llAm_T.tStartRefresh)
    trials.addData('llAm_T.stopped', llAm_T.tStopRefresh)
    trials.addData('llDel_T.started', llDel_T.tStartRefresh)
    trials.addData('llDel_T.stopped', llDel_T.tStopRefresh)
    # check responses
    if respT.keys in ['', [], None]:  # No response was made
        respT.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           respT.corr = 1;  # correct non-response
        else:
           respT.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('respT.keys',respT.keys)
    trials.addData('respT.corr', respT.corr)
    if respT.keys != None:  # we had a response
        trials.addData('respT.rt', respT.rt)
    trials.addData('respT.started', respT.tStartRefresh)
    trials.addData('respT.stopped', respT.tStopRefresh)
    
    # ------Prepare to start Routine "fb_Trials"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if not respT.keys :
        msg="No respondiste a tiempo!"
    elif respT.corr:#stored on last run routine
        msg="Elegiste esperar" 
    else:
        msg="Elegiste no esperar"
    textfbT.setText(msg)
    # keep track of which components have finished
    fb_TrialsComponents = [textfbT]
    for thisComponent in fb_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fb_TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fb_Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fb_TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fb_TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textfbT* updates
        if textfbT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textfbT.frameNStart = frameN  # exact frame index
            textfbT.tStart = t  # local t and not account for scr refresh
            textfbT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textfbT, 'tStartRefresh')  # time at next scr refresh
            textfbT.setAutoDraw(True)
        if textfbT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textfbT.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textfbT.tStop = t  # not accounting for scr refresh
                textfbT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textfbT, 'tStopRefresh')  # time at next scr refresh
                textfbT.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fb_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fb_Trials"-------
    for thisComponent in fb_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textfbT.started', textfbT.tStartRefresh)
    trials.addData('textfbT.stopped', textfbT.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Fin"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
FinComponents = [Gracias, key_resp_4]
for thisComponent in FinComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Fin"-------
while continueRoutine:
    # get current time
    t = FinClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Gracias* updates
    if Gracias.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Gracias.frameNStart = frameN  # exact frame index
        Gracias.tStart = t  # local t and not account for scr refresh
        Gracias.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Gracias, 'tStartRefresh')  # time at next scr refresh
        Gracias.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_4.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_4.tStop = t  # not accounting for scr refresh
            key_resp_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
            key_resp_4.status = FINISHED
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin"-------
for thisComponent in FinComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Gracias.started', Gracias.tStartRefresh)
thisExp.addData('Gracias.stopped', Gracias.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
