#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on February 13, 2020, at 17:31
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
psychopyVersion = '3.2.4'
expName = 'TSN_PostQ_Feb_13_2020'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\eLearn\\Desktop\\TSN_PostQ\\TSN_PostQ_Feb_13_2020_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
textIntro = visual.TextStim(win=win, name='textIntro',
    text='Please answer all of the following questions truthfully; all information collected through this questionnaire will be kept confidential. The answers will be anonymized and cannot be traced back to you as an individual.\n\nPress the space bar to start the questionnaire.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
respIntro = keyboard.Keyboard()

# Initialize components for Routine "age"
ageClock = core.Clock()
ageinstr = visual.TextStim(win=win, name='ageinstr',
    text='How old are you? (please type your answer in and press enter)',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "edu"
eduClock = core.Clock()
eduinstr = visual.TextStim(win=win, name='eduinstr',
    text='How many years of post-secondary education have you completed? (please type your answer in and press enter)',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "demog"
demogClock = core.Clock()
win.allowStencil = True
formDemog = visual.Form(win=win, name='formDemog',
    items='demographics.csv',
    textHeight=0.025,
    randomize=False,
    size=(1.3, 0.7),
    pos=(0, 0),
    itemPadding=0.08)

# Initialize components for Routine "secQs_2"
secQs_2Clock = core.Clock()
win.allowStencil = True
formsecQs2 = visual.Form(win=win, name='formsecQs2',
    items='secQs2.csv',
    textHeight=0.025,
    randomize=False,
    size=(1.3, 0.7),
    pos=(0, 0),
    itemPadding=0.08)

# Initialize components for Routine "securityQs"
securityQsClock = core.Clock()
win.allowStencil = True
formSecurityQs = visual.Form(win=win, name='formSecurityQs',
    items='VanceQs.csv',
    textHeight=0.025,
    randomize=False,
    size=(1.6, 0.7),
    pos=(0, 0),
    itemPadding=0.08)
securityQinstr = visual.TextStim(win=win, name='securityQinstr',
    text='Please answer the following questions by rating them on a scale between 1 (strongly disagree) and 5 (strongly agree).',
    font='Arial',
    pos=(0, 0.4), height=0.035, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
endtext = visual.TextStim(win=win, name='endtext',
    text='You have completed the questionnaire! This page will close automatically in 5 seconds. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
# update component parameters for each repeat
respIntro.keys = []
respIntro.rt = []
# keep track of which components have finished
introComponents = [textIntro, respIntro]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textIntro* updates
    if textIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textIntro.frameNStart = frameN  # exact frame index
        textIntro.tStart = t  # local t and not account for scr refresh
        textIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textIntro, 'tStartRefresh')  # time at next scr refresh
        textIntro.setAutoDraw(True)
    
    # *respIntro* updates
    waitOnFlip = False
    if respIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respIntro.frameNStart = frameN  # exact frame index
        respIntro.tStart = t  # local t and not account for scr refresh
        respIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respIntro, 'tStartRefresh')  # time at next scr refresh
        respIntro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respIntro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respIntro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respIntro.status == STARTED and not waitOnFlip:
        theseKeys = respIntro.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            respIntro.keys = theseKeys.name  # just the last key pressed
            respIntro.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textIntro.started', textIntro.tStartRefresh)
thisExp.addData('textIntro.stopped', textIntro.tStopRefresh)
# check responses
if respIntro.keys in ['', [], None]:  # No response was made
    respIntro.keys = None
thisExp.addData('respIntro.keys',respIntro.keys)
if respIntro.keys != None:  # we had a response
    thisExp.addData('respIntro.rt', respIntro.rt)
thisExp.addData('respIntro.started', respIntro.tStartRefresh)
thisExp.addData('respIntro.stopped', respIntro.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "age"-------
# update component parameters for each repeat
modify = False
text.text = ''
event.clearEvents('keyboard')
# keep track of which components have finished
ageComponents = [ageinstr, text]
for thisComponent in ageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "age"-------
while continueRoutine:
    # get current time
    t = ageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ageinstr* updates
    if ageinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ageinstr.frameNStart = frameN  # exact frame index
        ageinstr.tStart = t  # local t and not account for scr refresh
        ageinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ageinstr, 'tStartRefresh')  # time at next scr refresh
        ageinstr.setAutoDraw(True)
    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            text.text = text.text + ' '
        elif 'backspace' in keys:
            text.text = text.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                text.text = text.text + keys[0].upper()
                modify = False
            else:
                text.text = text.text + keys[0]
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "age"-------
for thisComponent in ageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ageinstr.started', ageinstr.tStartRefresh)
thisExp.addData('ageinstr.stopped', ageinstr.tStopRefresh)
thisExp.addData("age", text.text)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "age" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "edu"-------
# update component parameters for each repeat
modify = False
text_2.text = ''
event.clearEvents('keyboard')
# keep track of which components have finished
eduComponents = [eduinstr, text_2]
for thisComponent in eduComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eduClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "edu"-------
while continueRoutine:
    # get current time
    t = eduClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eduClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *eduinstr* updates
    if eduinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eduinstr.frameNStart = frameN  # exact frame index
        eduinstr.tStart = t  # local t and not account for scr refresh
        eduinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eduinstr, 'tStartRefresh')  # time at next scr refresh
        eduinstr.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    keys = event.getKeys()
    if len(keys):
        if 'space' in keys:
            text_2.text = text_2.text + ' '
        elif 'backspace' in keys:
            text_2.text = text_2.text[:-1]
        elif 'lshift' in keys or 'rshift' in keys:
            modify = True
        elif 'return' in keys:
            continueRoutine = False
        else:
            if modify:
                text_2.text = text_2.text + keys[0].upper()
                modify = False
            else:
                text_2.text = text_2.text + keys[0]
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eduComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "edu"-------
for thisComponent in eduComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('eduinstr.started', eduinstr.tStartRefresh)
thisExp.addData('eduinstr.stopped', eduinstr.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData("edu_yrs", text_2.text)
# the Routine "edu" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demog"-------
# update component parameters for each repeat
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.35, -.4))
# keep track of which components have finished
demogComponents = [formDemog]
for thisComponent in demogComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demogClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "demog"-------
while continueRoutine:
    # get current time
    t = demogClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demogClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    formDemog.draw()
    continueButton.draw()
    
    if formDemog.formComplete():
        continueButton.buttonEnabled = True
        
    if continueButton.buttonSelected:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demogComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demog"-------
for thisComponent in demogComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
formDemogData = formDemog.getData()
while formDemogData['questions']:
    for dataTypes in formDemogData.keys():
        thisExp.addData(dataTypes, formDemogData[dataTypes].popleft())
    thisExp.nextEntry()
# the Routine "demog" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "secQs_2"-------
# update component parameters for each repeat
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.35, -.4))
# keep track of which components have finished
secQs_2Components = [formsecQs2]
for thisComponent in secQs_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
secQs_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "secQs_2"-------
while continueRoutine:
    # get current time
    t = secQs_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=secQs_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    formsecQs2.draw()
    continueButton.draw()
    
    if formsecQs2.formComplete():
        continueButton.buttonEnabled = True
        
    if continueButton.buttonSelected:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in secQs_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "secQs_2"-------
for thisComponent in secQs_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
formsecQs2Data = formsecQs2.getData()
while formsecQs2Data['questions']:
    for dataTypes in formsecQs2Data.keys():
        thisExp.addData(dataTypes, formsecQs2Data[dataTypes].popleft())
    thisExp.nextEntry()
# the Routine "secQs_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "securityQs"-------
# update component parameters for each repeat
continueButton = visual.ButtonStim(win, labelText= "Continue", pos=(.35, -.4))
# keep track of which components have finished
securityQsComponents = [formSecurityQs, securityQinstr]
for thisComponent in securityQsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
securityQsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "securityQs"-------
while continueRoutine:
    # get current time
    t = securityQsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=securityQsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    formSecurityQs.draw()
    continueButton.draw()
    
    if formSecurityQs.formComplete():
        continueButton.buttonEnabled = True
        
    if continueButton.buttonSelected:
        continueRoutine = False
    
    # *securityQinstr* updates
    if securityQinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        securityQinstr.frameNStart = frameN  # exact frame index
        securityQinstr.tStart = t  # local t and not account for scr refresh
        securityQinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(securityQinstr, 'tStartRefresh')  # time at next scr refresh
        securityQinstr.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in securityQsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "securityQs"-------
for thisComponent in securityQsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
formSecurityQsData = formSecurityQs.getData()
while formSecurityQsData['questions']:
    for dataTypes in formSecurityQsData.keys():
        thisExp.addData(dataTypes, formSecurityQsData[dataTypes].popleft())
    thisExp.nextEntry()
thisExp.addData('securityQinstr.started', securityQinstr.tStartRefresh)
thisExp.addData('securityQinstr.stopped', securityQinstr.tStopRefresh)
# the Routine "securityQs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndScreen"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [endtext]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endtext* updates
    if endtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endtext.frameNStart = frameN  # exact frame index
        endtext.tStart = t  # local t and not account for scr refresh
        endtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endtext, 'tStartRefresh')  # time at next scr refresh
        endtext.setAutoDraw(True)
    if endtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endtext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            endtext.tStop = t  # not accounting for scr refresh
            endtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endtext, 'tStopRefresh')  # time at next scr refresh
            endtext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endtext.started', endtext.tStartRefresh)
thisExp.addData('endtext.stopped', endtext.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
