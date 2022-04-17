#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on January 31, 2020, at 10:32
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
psychopyVersion = '3.2.3'
expName = 'TSN_Jan_31_2020'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Jasmine\\Desktop\\TSN_Jan_31_2020\\TSN_Jan_31_2020_lastrun.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "CodeInit"
CodeInitClock = core.Clock()
import random, xlrd

#randomize the seed
random.seed()

#test stimuli file
infile = 'pics160_wide.xlsx'

#num of pics in each type
num_pic = 32

#num of different types of pics
num_type = 5

#number of 5-trial blocks
num_blocks = 32

#number of sections of the experiment (gives break and EEG touch-up time)
num_sections = 4

#number of blocks per section
num_secblock = 8

#total number of pics
num_pictot = 160

#number of practice items
num_prac = 5

#Start the trial counter
cur_pic = 0

# Initialize components for Routine "RatingInstr"
RatingInstrClock = core.Clock()
textwelcome = visual.TextStim(win=win, name='textwelcome',
    text="Welcome to the experiment! You will be shown a series of pictures. First, the picture will appear on its own. Please observe the picture carefully. \n\nAfter a short delay, you will be asked to rate how the picture makes you feel on the following two 5-point scales (you will enter your response by moving the left and right arrow keys and pressing 'enter'):",
    font='Arial',
    pos=(0, .7), height=0.075, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PicValence = visual.ImageStim(
    win=win,
    name='PicValence', 
    image='SAM/Redondo2007_Valence_5pt_prac.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.2, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
PicArousal = visual.ImageStim(
    win=win,
    name='PicArousal', 
    image='SAM/Redondo2007_Arousal_5pt_prac.jpg', mask=None,
    ori=0, pos=(0, -0.7), size=(1.2, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
RatingInstrResp = keyboard.Keyboard()
textValence = visual.TextStim(win=win, name='textValence',
    text='The Unhappy vs. Happy Scale:',
    font='Arial',
    pos=(0, 0.3), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
textArousal = visual.TextStim(win=win, name='textArousal',
    text='The Calm vs. Excited Scale:',
    font='Arial',
    pos=(0, -0.4), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "SampleItem"
SampleItemClock = core.Clock()
sampleitempress = keyboard.Keyboard()
sampletext = visual.TextStim(win=win, name='sampletext',
    text="Let's do some practice items. Press 'space' when you are ready to start.",
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Blank2000"
Blank2000Clock = core.Clock()
FixationCross = visual.TextStim(win=win, name='FixationCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeCode"
PracticeCodeClock = core.Clock()
#counter for the current practice pic
curpic_prac = 0

#access the second sheet of the xls file, where the practice items are
inbook = xlrd.open_workbook(infile)
insheet = inbook.sheet_by_index(1)

#array for practice stimuli
pic_prac = []

#read the stimuli from our sheet

#load in pics
for rowx in range(0, num_prac):

    #read in the values of all columns on this row
    row = insheet.row_values(rowx)
    
    #saving the pics to the array
    pic_prac.append(row[0])


#randomizes the order of the practice pics
random.shuffle(pic_prac)


#assign picture for the first trial
PracStim = pic_prac[curpic_prac]

# Initialize components for Routine "PracticeImage"
PracticeImageClock = core.Clock()
Samplepic = visual.ImageStim(
    win=win,
    name='Samplepic', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.8, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "RateDelay"
RateDelayClock = core.Clock()
DelayBlack = visual.TextStim(win=win, name='DelayBlack',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RateValence"
RateValenceClock = core.Clock()
SAMValence = visual.ImageStim(
    win=win,
    name='SAMValence', 
    image='SAM/Redondo2007_Valence_5pt_test.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ratingValence = visual.RatingScale(win=win, name='ratingValence', marker='triangle', size=1.35, pos=[0.0, -0.5], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='', markerStart='3')
rateValencetxt = visual.TextStim(win=win, name='rateValencetxt',
    text='Please rate how the picture you just saw made you feel on the following 5-point scale:',
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank250"
Blank250Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RateArousal"
RateArousalClock = core.Clock()
SAMArousal = visual.ImageStim(
    win=win,
    name='SAMArousal', 
    image='SAM/Redondo2007_Arousal_5pt_test.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ratingArousal = visual.RatingScale(win=win, name='ratingArousal', marker='triangle', size=1.35, pos=[0.0, -0.5], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='', markerStart='3')
RateArousaltxt = visual.TextStim(win=win, name='RateArousaltxt',
    text='Please rate how the picture you just saw made you feel on the following 5-point scale:',
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
FixationCross2 = visual.TextStim(win=win, name='FixationCross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ExpStart"
ExpStartClock = core.Clock()
ExpStartText = visual.TextStim(win=win, name='ExpStartText',
    text='This is the end of the practice.\n\n\nThere are three breaks scheduled in the experiment, during which the researchers will come in and adjust your cap.\n\n\nWhen you are ready, the researcher will close the door and start the experiment for you.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RespStartExp = keyboard.Keyboard()

# Initialize components for Routine "CodeSection"
CodeSectionClock = core.Clock()
#start the section counter.

cur_section = 0



# Initialize components for Routine "Blank2000"
Blank2000Clock = core.Clock()
FixationCross = visual.TextStim(win=win, name='FixationCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CodeBlock"
CodeBlockClock = core.Clock()
#counter for the current block
cur_block = 0

#access the xls stimulusfile
inbook = xlrd.open_workbook(infile)
insheet = inbook.sheet_by_index(0)

#arrays for our stimuli
pic_nega = []
pic_posi = []
pic_neut = []
pic_warn = []
pic_onli = []

#read the stimuli from our sheet

#load in pics
for rowx in range(1, num_pic + 1):

    #read in the values of all columns on this row
    row = insheet.row_values(rowx)
    
    #print out values to see what happens
    #print(row[0, 1, 2, 3, 4]
    
    #saving the pics to the appropriate array
    pic_nega.append(row[0])
    pic_posi.append(row[1])
    pic_neut.append(row[2])
    pic_warn.append(row[3])
    pic_onli.append(row[4])

#randomizes the order of the four picture arrays
random.shuffle(pic_nega)
random.shuffle(pic_posi)
random.shuffle(pic_neut)
random.shuffle(pic_warn)
random.shuffle(pic_onli)
#print(pic_neg, pic_pos, pic_neu, pic_war)


#create array of all the picture arrays.

pics = [pic_nega, pic_posi, pic_neut, pic_warn, pic_onli]

#let's take a look. [0][0] means first item of first array.
#print(str(pic_order[0][0]) + " " + str(pic_order[1][0]) + " " + str(pic_order[2][0]) + " " + str(pic_order[3][0]))
#print(str(pic_order[0][1]) + " " + str(pic_order[1][1]) + " " + str(pic_order[2][1]) + " " + str(pic_order[3][1]))



# Initialize components for Routine "CodeTrial"
CodeTrialClock = core.Clock()
#create a pic order and shuffle it.
#pic_order = list(range(num_type))
#random.shuffle(pic_order)

#create an array that adds each displayed pic so we can rate l8r
stim_order = []



# Initialize components for Routine "StudyImage"
StudyImageClock = core.Clock()
StudyPic = visual.ImageStim(
    win=win,
    name='StudyPic', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(.8, .6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "RateDelay"
RateDelayClock = core.Clock()
DelayBlack = visual.TextStim(win=win, name='DelayBlack',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "CodeRate"
CodeRateClock = core.Clock()
#start the current pic rating counter.
cur_rating = 0

# Initialize components for Routine "RateValence"
RateValenceClock = core.Clock()
SAMValence = visual.ImageStim(
    win=win,
    name='SAMValence', 
    image='SAM/Redondo2007_Valence_5pt_test.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ratingValence = visual.RatingScale(win=win, name='ratingValence', marker='triangle', size=1.35, pos=[0.0, -0.5], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='', markerStart='3')
rateValencetxt = visual.TextStim(win=win, name='rateValencetxt',
    text='Please rate how the picture you just saw made you feel on the following 5-point scale:',
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Blank250"
Blank250Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RateArousal"
RateArousalClock = core.Clock()
SAMArousal = visual.ImageStim(
    win=win,
    name='SAMArousal', 
    image='SAM/Redondo2007_Arousal_5pt_test.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ratingArousal = visual.RatingScale(win=win, name='ratingArousal', marker='triangle', size=1.35, pos=[0.0, -0.5], low=1, high=5, labels=['1', '2', '3', '4', '5'], scale='', markerStart='3')
RateArousaltxt = visual.TextStim(win=win, name='RateArousaltxt',
    text='Please rate how the picture you just saw made you feel on the following 5-point scale:',
    font='Arial',
    pos=(0, 0.4), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
FixationCross2 = visual.TextStim(win=win, name='FixationCross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BreakCode"
BreakCodeClock = core.Clock()

# Initialize components for Routine "BreakScreen"
BreakScreenClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Cont_resp = keyboard.Keyboard()

# Initialize components for Routine "StudyEnd"
StudyEndClock = core.Clock()
Endtext = visual.TextStim(win=win, name='Endtext',
    text='Thank you! The experiment will close automatically in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "CodeInit"-------
# update component parameters for each repeat
# keep track of which components have finished
CodeInitComponents = []
for thisComponent in CodeInitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CodeInitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "CodeInit"-------
while continueRoutine:
    # get current time
    t = CodeInitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CodeInitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CodeInitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CodeInit"-------
for thisComponent in CodeInitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CodeInit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RatingInstr"-------
# update component parameters for each repeat
RatingInstrResp.keys = []
RatingInstrResp.rt = []
# keep track of which components have finished
RatingInstrComponents = [textwelcome, PicValence, PicArousal, RatingInstrResp, textValence, textArousal]
for thisComponent in RatingInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RatingInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "RatingInstr"-------
while continueRoutine:
    # get current time
    t = RatingInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RatingInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textwelcome* updates
    if textwelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textwelcome.frameNStart = frameN  # exact frame index
        textwelcome.tStart = t  # local t and not account for scr refresh
        textwelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textwelcome, 'tStartRefresh')  # time at next scr refresh
        textwelcome.setAutoDraw(True)
    
    # *PicValence* updates
    if PicValence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PicValence.frameNStart = frameN  # exact frame index
        PicValence.tStart = t  # local t and not account for scr refresh
        PicValence.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PicValence, 'tStartRefresh')  # time at next scr refresh
        PicValence.setAutoDraw(True)
    
    # *PicArousal* updates
    if PicArousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PicArousal.frameNStart = frameN  # exact frame index
        PicArousal.tStart = t  # local t and not account for scr refresh
        PicArousal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PicArousal, 'tStartRefresh')  # time at next scr refresh
        PicArousal.setAutoDraw(True)
    
    # *RatingInstrResp* updates
    waitOnFlip = False
    if RatingInstrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RatingInstrResp.frameNStart = frameN  # exact frame index
        RatingInstrResp.tStart = t  # local t and not account for scr refresh
        RatingInstrResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RatingInstrResp, 'tStartRefresh')  # time at next scr refresh
        RatingInstrResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RatingInstrResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RatingInstrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RatingInstrResp.status == STARTED and not waitOnFlip:
        theseKeys = RatingInstrResp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            RatingInstrResp.keys = theseKeys.name  # just the last key pressed
            RatingInstrResp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *textValence* updates
    if textValence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textValence.frameNStart = frameN  # exact frame index
        textValence.tStart = t  # local t and not account for scr refresh
        textValence.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textValence, 'tStartRefresh')  # time at next scr refresh
        textValence.setAutoDraw(True)
    
    # *textArousal* updates
    if textArousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textArousal.frameNStart = frameN  # exact frame index
        textArousal.tStart = t  # local t and not account for scr refresh
        textArousal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textArousal, 'tStartRefresh')  # time at next scr refresh
        textArousal.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatingInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RatingInstr"-------
for thisComponent in RatingInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textwelcome.started', textwelcome.tStartRefresh)
thisExp.addData('textwelcome.stopped', textwelcome.tStopRefresh)
thisExp.addData('PicValence.started', PicValence.tStartRefresh)
thisExp.addData('PicValence.stopped', PicValence.tStopRefresh)
thisExp.addData('PicArousal.started', PicArousal.tStartRefresh)
thisExp.addData('PicArousal.stopped', PicArousal.tStopRefresh)
# check responses
if RatingInstrResp.keys in ['', [], None]:  # No response was made
    RatingInstrResp.keys = None
thisExp.addData('RatingInstrResp.keys',RatingInstrResp.keys)
if RatingInstrResp.keys != None:  # we had a response
    thisExp.addData('RatingInstrResp.rt', RatingInstrResp.rt)
thisExp.addData('RatingInstrResp.started', RatingInstrResp.tStartRefresh)
thisExp.addData('RatingInstrResp.stopped', RatingInstrResp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textValence.started', textValence.tStartRefresh)
thisExp.addData('textValence.stopped', textValence.tStopRefresh)
thisExp.addData('textArousal.started', textArousal.tStartRefresh)
thisExp.addData('textArousal.stopped', textArousal.tStopRefresh)
# the Routine "RatingInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SampleItem"-------
# update component parameters for each repeat
sampleitempress.keys = []
sampleitempress.rt = []
# keep track of which components have finished
SampleItemComponents = [sampleitempress, sampletext]
for thisComponent in SampleItemComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SampleItemClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "SampleItem"-------
while continueRoutine:
    # get current time
    t = SampleItemClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SampleItemClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sampleitempress* updates
    waitOnFlip = False
    if sampleitempress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampleitempress.frameNStart = frameN  # exact frame index
        sampleitempress.tStart = t  # local t and not account for scr refresh
        sampleitempress.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampleitempress, 'tStartRefresh')  # time at next scr refresh
        sampleitempress.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sampleitempress.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sampleitempress.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sampleitempress.status == STARTED and not waitOnFlip:
        theseKeys = sampleitempress.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            sampleitempress.keys = theseKeys.name  # just the last key pressed
            sampleitempress.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *sampletext* updates
    if sampletext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sampletext.frameNStart = frameN  # exact frame index
        sampletext.tStart = t  # local t and not account for scr refresh
        sampletext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sampletext, 'tStartRefresh')  # time at next scr refresh
        sampletext.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SampleItemComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SampleItem"-------
for thisComponent in SampleItemComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if sampleitempress.keys in ['', [], None]:  # No response was made
    sampleitempress.keys = None
thisExp.addData('sampleitempress.keys',sampleitempress.keys)
if sampleitempress.keys != None:  # we had a response
    thisExp.addData('sampleitempress.rt', sampleitempress.rt)
thisExp.addData('sampleitempress.started', sampleitempress.tStartRefresh)
thisExp.addData('sampleitempress.stopped', sampleitempress.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('sampletext.started', sampletext.tStartRefresh)
thisExp.addData('sampletext.stopped', sampletext.tStopRefresh)
# the Routine "SampleItem" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank2000"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
Blank2000Components = [FixationCross]
for thisComponent in Blank2000Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank2000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Blank2000"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank2000Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank2000Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FixationCross* updates
    if FixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FixationCross.frameNStart = frameN  # exact frame index
        FixationCross.tStart = t  # local t and not account for scr refresh
        FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
        FixationCross.setAutoDraw(True)
    if FixationCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FixationCross.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            FixationCross.tStop = t  # not accounting for scr refresh
            FixationCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank2000Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank2000"-------
for thisComponent in Blank2000Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FixationCross.started', FixationCross.tStartRefresh)
thisExp.addData('FixationCross.stopped', FixationCross.tStopRefresh)

# set up handler to look after randomisation of conditions etc
practiceloop = data.TrialHandler(nReps=num_prac, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practiceloop')
thisExp.addLoop(practiceloop)  # add the loop to the experiment
thisPracticeloop = practiceloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeloop.rgb)
if thisPracticeloop != None:
    for paramName in thisPracticeloop:
        exec('{} = thisPracticeloop[paramName]'.format(paramName))

for thisPracticeloop in practiceloop:
    currentLoop = practiceloop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeloop.rgb)
    if thisPracticeloop != None:
        for paramName in thisPracticeloop:
            exec('{} = thisPracticeloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeCode"-------
    # update component parameters for each repeat
    #assign picture for the current trial
    PracStim = pic_prac[curpic_prac]
    
    #create a jittered delay between picture presentation and SAM rating.
    #Note that this makes it range from 2 to 3.
    RateDelay = random.random() * (3-2) + 2
    RateDelay = round(RateDelay, 1)
    
    #create a jittered ITI. Note this makes it range from 2 to 3
    ITI = random.random() * (3-2) + 2
    ITI = round(ITI, 1)
    
    #above is what it should be! BUT let's speed up the ITI so I can troubleshoot.
    #RateDelay = .25
    #ITI = .25
    # keep track of which components have finished
    PracticeCodeComponents = []
    for thisComponent in PracticeCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracticeCode"-------
    while continueRoutine:
        # get current time
        t = PracticeCodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeCodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeCode"-------
    for thisComponent in PracticeCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #Saving the picture type
    
    pic_type = []
    
    if 'fear' in PracStim:
        pic_type = 'nega'
    
    elif 'happy' in PracStim:
        pic_type = 'posi'
    
    elif 'neut' in PracStim:
        pic_type = 'neut'
    
    elif 'warn' in PracStim:
        pic_type = 'warn'
    else:
        pic_type = 'onli'
    
    
    #log important info to datafile
    thisExp.addData('PracStim', PracStim)
    thisExp.addData('pic_type', pic_type)
    thisExp.addData('curpic_prac', curpic_prac + 1)
    thisExp.addData('RateDelay', RateDelay)
    thisExp.addData('ITI', ITI)
    
    #Get the current picture to update counter
    curpic_prac = curpic_prac + 1
    # the Routine "PracticeCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeImage"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    Samplepic.setImage(PracStim)
    # keep track of which components have finished
    PracticeImageComponents = [Samplepic]
    for thisComponent in PracticeImageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracticeImage"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeImageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeImageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Samplepic* updates
        if Samplepic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Samplepic.frameNStart = frameN  # exact frame index
            Samplepic.tStart = t  # local t and not account for scr refresh
            Samplepic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Samplepic, 'tStartRefresh')  # time at next scr refresh
            Samplepic.setAutoDraw(True)
        if Samplepic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Samplepic.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Samplepic.tStop = t  # not accounting for scr refresh
                Samplepic.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Samplepic, 'tStopRefresh')  # time at next scr refresh
                Samplepic.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeImageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeImage"-------
    for thisComponent in PracticeImageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('Samplepic.started', Samplepic.tStartRefresh)
    practiceloop.addData('Samplepic.stopped', Samplepic.tStopRefresh)
    
    # ------Prepare to start Routine "RateDelay"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    RateDelayComponents = [DelayBlack]
    for thisComponent in RateDelayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RateDelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "RateDelay"-------
    while continueRoutine:
        # get current time
        t = RateDelayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RateDelayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DelayBlack* updates
        if DelayBlack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DelayBlack.frameNStart = frameN  # exact frame index
            DelayBlack.tStart = t  # local t and not account for scr refresh
            DelayBlack.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DelayBlack, 'tStartRefresh')  # time at next scr refresh
            DelayBlack.setAutoDraw(True)
        if DelayBlack.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DelayBlack.tStartRefresh + RateDelay-frameTolerance:
                # keep track of stop time/frame for later
                DelayBlack.tStop = t  # not accounting for scr refresh
                DelayBlack.frameNStop = frameN  # exact frame index
                win.timeOnFlip(DelayBlack, 'tStopRefresh')  # time at next scr refresh
                DelayBlack.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RateDelayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RateDelay"-------
    for thisComponent in RateDelayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('DelayBlack.started', DelayBlack.tStartRefresh)
    practiceloop.addData('DelayBlack.stopped', DelayBlack.tStopRefresh)
    # the Routine "RateDelay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "RateValence"-------
    # update component parameters for each repeat
    ratingValence.reset()
    # keep track of which components have finished
    RateValenceComponents = [SAMValence, ratingValence, rateValencetxt]
    for thisComponent in RateValenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RateValenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "RateValence"-------
    while continueRoutine:
        # get current time
        t = RateValenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RateValenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SAMValence* updates
        if SAMValence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SAMValence.frameNStart = frameN  # exact frame index
            SAMValence.tStart = t  # local t and not account for scr refresh
            SAMValence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SAMValence, 'tStartRefresh')  # time at next scr refresh
            SAMValence.setAutoDraw(True)
        # *ratingValence* updates
        if ratingValence.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ratingValence.frameNStart = frameN  # exact frame index
            ratingValence.tStart = t  # local t and not account for scr refresh
            ratingValence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingValence, 'tStartRefresh')  # time at next scr refresh
            ratingValence.setAutoDraw(True)
        continueRoutine &= ratingValence.noResponse  # a response ends the trial
        
        # *rateValencetxt* updates
        if rateValencetxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rateValencetxt.frameNStart = frameN  # exact frame index
            rateValencetxt.tStart = t  # local t and not account for scr refresh
            rateValencetxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rateValencetxt, 'tStartRefresh')  # time at next scr refresh
            rateValencetxt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RateValenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RateValence"-------
    for thisComponent in RateValenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('SAMValence.started', SAMValence.tStartRefresh)
    practiceloop.addData('SAMValence.stopped', SAMValence.tStopRefresh)
    # store data for practiceloop (TrialHandler)
    practiceloop.addData('ratingValence.response', ratingValence.getRating())
    practiceloop.addData('ratingValence.rt', ratingValence.getRT())
    practiceloop.addData('ratingValence.started', ratingValence.tStart)
    practiceloop.addData('ratingValence.stopped', ratingValence.tStop)
    practiceloop.addData('rateValencetxt.started', rateValencetxt.tStartRefresh)
    practiceloop.addData('rateValencetxt.stopped', rateValencetxt.tStopRefresh)
    # the Routine "RateValence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank250"-------
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank250Components = [text]
    for thisComponent in Blank250Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank250Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank250"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank250Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank250Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank250Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank250"-------
    for thisComponent in Blank250Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('text.started', text.tStartRefresh)
    practiceloop.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "RateArousal"-------
    # update component parameters for each repeat
    ratingArousal.reset()
    # keep track of which components have finished
    RateArousalComponents = [SAMArousal, ratingArousal, RateArousaltxt]
    for thisComponent in RateArousalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RateArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "RateArousal"-------
    while continueRoutine:
        # get current time
        t = RateArousalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RateArousalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SAMArousal* updates
        if SAMArousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SAMArousal.frameNStart = frameN  # exact frame index
            SAMArousal.tStart = t  # local t and not account for scr refresh
            SAMArousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SAMArousal, 'tStartRefresh')  # time at next scr refresh
            SAMArousal.setAutoDraw(True)
        # *ratingArousal* updates
        if ratingArousal.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ratingArousal.frameNStart = frameN  # exact frame index
            ratingArousal.tStart = t  # local t and not account for scr refresh
            ratingArousal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingArousal, 'tStartRefresh')  # time at next scr refresh
            ratingArousal.setAutoDraw(True)
        continueRoutine &= ratingArousal.noResponse  # a response ends the trial
        
        # *RateArousaltxt* updates
        if RateArousaltxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RateArousaltxt.frameNStart = frameN  # exact frame index
            RateArousaltxt.tStart = t  # local t and not account for scr refresh
            RateArousaltxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RateArousaltxt, 'tStartRefresh')  # time at next scr refresh
            RateArousaltxt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RateArousalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RateArousal"-------
    for thisComponent in RateArousalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('SAMArousal.started', SAMArousal.tStartRefresh)
    practiceloop.addData('SAMArousal.stopped', SAMArousal.tStopRefresh)
    # store data for practiceloop (TrialHandler)
    practiceloop.addData('ratingArousal.response', ratingArousal.getRating())
    practiceloop.addData('ratingArousal.rt', ratingArousal.getRT())
    practiceloop.addData('ratingArousal.started', ratingArousal.tStart)
    practiceloop.addData('ratingArousal.stopped', ratingArousal.tStop)
    practiceloop.addData('RateArousaltxt.started', RateArousaltxt.tStartRefresh)
    practiceloop.addData('RateArousaltxt.stopped', RateArousaltxt.tStopRefresh)
    # the Routine "RateArousal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [FixationCross2]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCross2* updates
        if FixationCross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCross2.frameNStart = frameN  # exact frame index
            FixationCross2.tStart = t  # local t and not account for scr refresh
            FixationCross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCross2, 'tStartRefresh')  # time at next scr refresh
            FixationCross2.setAutoDraw(True)
        if FixationCross2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCross2.tStartRefresh + ITI-frameTolerance:
                # keep track of stop time/frame for later
                FixationCross2.tStop = t  # not accounting for scr refresh
                FixationCross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCross2, 'tStopRefresh')  # time at next scr refresh
                FixationCross2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceloop.addData('FixationCross2.started', FixationCross2.tStartRefresh)
    practiceloop.addData('FixationCross2.stopped', FixationCross2.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_prac repeats of 'practiceloop'


# ------Prepare to start Routine "ExpStart"-------
# update component parameters for each repeat
RespStartExp.keys = []
RespStartExp.rt = []
# keep track of which components have finished
ExpStartComponents = [ExpStartText, RespStartExp]
for thisComponent in ExpStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExpStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ExpStart"-------
while continueRoutine:
    # get current time
    t = ExpStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExpStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExpStartText* updates
    if ExpStartText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExpStartText.frameNStart = frameN  # exact frame index
        ExpStartText.tStart = t  # local t and not account for scr refresh
        ExpStartText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExpStartText, 'tStartRefresh')  # time at next scr refresh
        ExpStartText.setAutoDraw(True)
    
    # *RespStartExp* updates
    waitOnFlip = False
    if RespStartExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RespStartExp.frameNStart = frameN  # exact frame index
        RespStartExp.tStart = t  # local t and not account for scr refresh
        RespStartExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RespStartExp, 'tStartRefresh')  # time at next scr refresh
        RespStartExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(RespStartExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(RespStartExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if RespStartExp.status == STARTED and not waitOnFlip:
        theseKeys = RespStartExp.getKeys(keyList=['s'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            RespStartExp.keys = theseKeys.name  # just the last key pressed
            RespStartExp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExpStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ExpStart"-------
for thisComponent in ExpStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ExpStartText.started', ExpStartText.tStartRefresh)
thisExp.addData('ExpStartText.stopped', ExpStartText.tStopRefresh)
# check responses
if RespStartExp.keys in ['', [], None]:  # No response was made
    RespStartExp.keys = None
thisExp.addData('RespStartExp.keys',RespStartExp.keys)
if RespStartExp.keys != None:  # we had a response
    thisExp.addData('RespStartExp.rt', RespStartExp.rt)
thisExp.addData('RespStartExp.started', RespStartExp.tStartRefresh)
thisExp.addData('RespStartExp.stopped', RespStartExp.tStopRefresh)
thisExp.nextEntry()
# the Routine "ExpStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SectionLoop = data.TrialHandler(nReps=num_sections, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='SectionLoop')
thisExp.addLoop(SectionLoop)  # add the loop to the experiment
thisSectionLoop = SectionLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSectionLoop.rgb)
if thisSectionLoop != None:
    for paramName in thisSectionLoop:
        exec('{} = thisSectionLoop[paramName]'.format(paramName))

for thisSectionLoop in SectionLoop:
    currentLoop = SectionLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSectionLoop.rgb)
    if thisSectionLoop != None:
        for paramName in thisSectionLoop:
            exec('{} = thisSectionLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "CodeSection"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    CodeSectionComponents = []
    for thisComponent in CodeSectionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CodeSectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "CodeSection"-------
    while continueRoutine:
        # get current time
        t = CodeSectionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CodeSectionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CodeSectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CodeSection"-------
    for thisComponent in CodeSectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #save the section number
    thisExp.addData('cur_section', cur_section + 1)
    
    #Get the current section to update counter
    cur_section = cur_section + 1
    # the Routine "CodeSection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Blank2000"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Blank2000Components = [FixationCross]
    for thisComponent in Blank2000Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Blank2000Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Blank2000"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Blank2000Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Blank2000Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCross* updates
        if FixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCross.frameNStart = frameN  # exact frame index
            FixationCross.tStart = t  # local t and not account for scr refresh
            FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(True)
        if FixationCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FixationCross.tStop = t  # not accounting for scr refresh
                FixationCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
                FixationCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Blank2000Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Blank2000"-------
    for thisComponent in Blank2000Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SectionLoop.addData('FixationCross.started', FixationCross.tStartRefresh)
    SectionLoop.addData('FixationCross.stopped', FixationCross.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    BlockLoop = data.TrialHandler(nReps=num_secblock, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='BlockLoop')
    thisExp.addLoop(BlockLoop)  # add the loop to the experiment
    thisBlockLoop = BlockLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    for thisBlockLoop in BlockLoop:
        currentLoop = BlockLoop
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
        if thisBlockLoop != None:
            for paramName in thisBlockLoop:
                exec('{} = thisBlockLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CodeBlock"-------
        # update component parameters for each repeat
        #pull the five photos we will need for this block and shuffle
        pic_block = [pics[0][cur_block], pics[1][cur_block], pics[2][cur_block], pics[3][cur_block], pics[4][cur_block]]
        random.shuffle(pic_block)
        
        #set pic counter
        cur_pic = 0
        
        
        
        # keep track of which components have finished
        CodeBlockComponents = []
        for thisComponent in CodeBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CodeBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "CodeBlock"-------
        while continueRoutine:
            # get current time
            t = CodeBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CodeBlockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CodeBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CodeBlock"-------
        for thisComponent in CodeBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #save the block number
        thisExp.addData('cur_block', cur_block + 1)
        
        #Get the current block to update counter
        cur_block = cur_block + 1
        # the Routine "CodeBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        TrialLoop = data.TrialHandler(nReps=num_type, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='TrialLoop')
        thisExp.addLoop(TrialLoop)  # add the loop to the experiment
        thisTrialLoop = TrialLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                exec('{} = thisTrialLoop[paramName]'.format(paramName))
        
        for thisTrialLoop in TrialLoop:
            currentLoop = TrialLoop
            # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
            if thisTrialLoop != None:
                for paramName in thisTrialLoop:
                    exec('{} = thisTrialLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "CodeTrial"-------
            # update component parameters for each repeat
            #assign picture for the current trial
            PicStim = pic_block[cur_pic]
            
            #create a jittered delay between picture presentation and SAM rating.
            #Note that this makes it range from 2 to 3.
            RateDelay = random.random() * (3-2) + 2
            RateDelay = round(RateDelay, 1)
            
            #create a jittered ITI. Note this makes it range from 2 to 3
            ITI = random.random() * (3-2) + 2
            ITI = round(ITI, 1)
            
            #above is what it should be! BUT let's speed up the ITI so I can troubleshoot.
            #RateDelay = .25
            #ITI = .25
            # keep track of which components have finished
            CodeTrialComponents = []
            for thisComponent in CodeTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            CodeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "CodeTrial"-------
            while continueRoutine:
                # get current time
                t = CodeTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=CodeTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in CodeTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "CodeTrial"-------
            for thisComponent in CodeTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #create an ongoing list of pics they viewed so we can rate l8r.
            stim_order.append(PicStim)
            
            #Saving the picture type
            
            pic_type = []
            
            if 'fear' in PicStim:
                pic_type = 'nega'
            
            elif 'happy' in PicStim:
                pic_type = 'posi'
            
            elif 'neutral' in PicStim:
                pic_type = 'neut'
            
            elif 'Security' in PicStim:
                pic_type = 'warn'
            else:
                pic_type = 'onli'
            
            
            #log important info to datafile
            thisExp.addData('cur_section', cur_section)
            thisExp.addData('cur_block', cur_block)
            thisExp.addData('PicStim', PicStim)
            thisExp.addData('pic_type', pic_type)
            thisExp.addData('cur_pic', cur_pic + 1)
            thisExp.addData('RateDelay', RateDelay)
            thisExp.addData('ITI', ITI)
            
            #Get the current picture to update counter
            cur_pic = cur_pic + 1
            
            
            # the Routine "CodeTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "StudyImage"-------
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            StudyPic.setImage(PicStim)
            # keep track of which components have finished
            StudyImageComponents = [StudyPic]
            for thisComponent in StudyImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            StudyImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "StudyImage"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = StudyImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=StudyImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *StudyPic* updates
                if StudyPic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    StudyPic.frameNStart = frameN  # exact frame index
                    StudyPic.tStart = t  # local t and not account for scr refresh
                    StudyPic.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StudyPic, 'tStartRefresh')  # time at next scr refresh
                    StudyPic.setAutoDraw(True)
                if StudyPic.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > StudyPic.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        StudyPic.tStop = t  # not accounting for scr refresh
                        StudyPic.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(StudyPic, 'tStopRefresh')  # time at next scr refresh
                        StudyPic.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in StudyImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "StudyImage"-------
            for thisComponent in StudyImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('StudyPic.started', StudyPic.tStartRefresh)
            TrialLoop.addData('StudyPic.stopped', StudyPic.tStopRefresh)
            
            # ------Prepare to start Routine "RateDelay"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            RateDelayComponents = [DelayBlack]
            for thisComponent in RateDelayComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            RateDelayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "RateDelay"-------
            while continueRoutine:
                # get current time
                t = RateDelayClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=RateDelayClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *DelayBlack* updates
                if DelayBlack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    DelayBlack.frameNStart = frameN  # exact frame index
                    DelayBlack.tStart = t  # local t and not account for scr refresh
                    DelayBlack.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DelayBlack, 'tStartRefresh')  # time at next scr refresh
                    DelayBlack.setAutoDraw(True)
                if DelayBlack.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DelayBlack.tStartRefresh + RateDelay-frameTolerance:
                        # keep track of stop time/frame for later
                        DelayBlack.tStop = t  # not accounting for scr refresh
                        DelayBlack.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DelayBlack, 'tStopRefresh')  # time at next scr refresh
                        DelayBlack.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RateDelayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "RateDelay"-------
            for thisComponent in RateDelayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('DelayBlack.started', DelayBlack.tStartRefresh)
            TrialLoop.addData('DelayBlack.stopped', DelayBlack.tStopRefresh)
            # the Routine "RateDelay" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "CodeRate"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            CodeRateComponents = []
            for thisComponent in CodeRateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            CodeRateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "CodeRate"-------
            while continueRoutine:
                # get current time
                t = CodeRateClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=CodeRateClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in CodeRateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "CodeRate"-------
            for thisComponent in CodeRateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #update the rating counter and save it
            cur_rating = cur_rating + 1
            thisExp.addData('cur_rating', cur_rating)
            
            # the Routine "CodeRate" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "RateValence"-------
            # update component parameters for each repeat
            ratingValence.reset()
            # keep track of which components have finished
            RateValenceComponents = [SAMValence, ratingValence, rateValencetxt]
            for thisComponent in RateValenceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            RateValenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "RateValence"-------
            while continueRoutine:
                # get current time
                t = RateValenceClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=RateValenceClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *SAMValence* updates
                if SAMValence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SAMValence.frameNStart = frameN  # exact frame index
                    SAMValence.tStart = t  # local t and not account for scr refresh
                    SAMValence.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SAMValence, 'tStartRefresh')  # time at next scr refresh
                    SAMValence.setAutoDraw(True)
                # *ratingValence* updates
                if ratingValence.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ratingValence.frameNStart = frameN  # exact frame index
                    ratingValence.tStart = t  # local t and not account for scr refresh
                    ratingValence.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ratingValence, 'tStartRefresh')  # time at next scr refresh
                    ratingValence.setAutoDraw(True)
                continueRoutine &= ratingValence.noResponse  # a response ends the trial
                
                # *rateValencetxt* updates
                if rateValencetxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rateValencetxt.frameNStart = frameN  # exact frame index
                    rateValencetxt.tStart = t  # local t and not account for scr refresh
                    rateValencetxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rateValencetxt, 'tStartRefresh')  # time at next scr refresh
                    rateValencetxt.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RateValenceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "RateValence"-------
            for thisComponent in RateValenceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('SAMValence.started', SAMValence.tStartRefresh)
            TrialLoop.addData('SAMValence.stopped', SAMValence.tStopRefresh)
            # store data for TrialLoop (TrialHandler)
            TrialLoop.addData('ratingValence.response', ratingValence.getRating())
            TrialLoop.addData('ratingValence.rt', ratingValence.getRT())
            TrialLoop.addData('ratingValence.started', ratingValence.tStart)
            TrialLoop.addData('ratingValence.stopped', ratingValence.tStop)
            TrialLoop.addData('rateValencetxt.started', rateValencetxt.tStartRefresh)
            TrialLoop.addData('rateValencetxt.stopped', rateValencetxt.tStopRefresh)
            # the Routine "RateValence" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Blank250"-------
            routineTimer.add(0.250000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Blank250Components = [text]
            for thisComponent in Blank250Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Blank250Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "Blank250"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Blank250Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Blank250Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + .25-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                        text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Blank250Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Blank250"-------
            for thisComponent in Blank250Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('text.started', text.tStartRefresh)
            TrialLoop.addData('text.stopped', text.tStopRefresh)
            
            # ------Prepare to start Routine "RateArousal"-------
            # update component parameters for each repeat
            ratingArousal.reset()
            # keep track of which components have finished
            RateArousalComponents = [SAMArousal, ratingArousal, RateArousaltxt]
            for thisComponent in RateArousalComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            RateArousalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "RateArousal"-------
            while continueRoutine:
                # get current time
                t = RateArousalClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=RateArousalClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *SAMArousal* updates
                if SAMArousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SAMArousal.frameNStart = frameN  # exact frame index
                    SAMArousal.tStart = t  # local t and not account for scr refresh
                    SAMArousal.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SAMArousal, 'tStartRefresh')  # time at next scr refresh
                    SAMArousal.setAutoDraw(True)
                # *ratingArousal* updates
                if ratingArousal.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ratingArousal.frameNStart = frameN  # exact frame index
                    ratingArousal.tStart = t  # local t and not account for scr refresh
                    ratingArousal.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ratingArousal, 'tStartRefresh')  # time at next scr refresh
                    ratingArousal.setAutoDraw(True)
                continueRoutine &= ratingArousal.noResponse  # a response ends the trial
                
                # *RateArousaltxt* updates
                if RateArousaltxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RateArousaltxt.frameNStart = frameN  # exact frame index
                    RateArousaltxt.tStart = t  # local t and not account for scr refresh
                    RateArousaltxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RateArousaltxt, 'tStartRefresh')  # time at next scr refresh
                    RateArousaltxt.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in RateArousalComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "RateArousal"-------
            for thisComponent in RateArousalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('SAMArousal.started', SAMArousal.tStartRefresh)
            TrialLoop.addData('SAMArousal.stopped', SAMArousal.tStopRefresh)
            # store data for TrialLoop (TrialHandler)
            TrialLoop.addData('ratingArousal.response', ratingArousal.getRating())
            TrialLoop.addData('ratingArousal.rt', ratingArousal.getRT())
            TrialLoop.addData('ratingArousal.started', ratingArousal.tStart)
            TrialLoop.addData('ratingArousal.stopped', ratingArousal.tStop)
            TrialLoop.addData('RateArousaltxt.started', RateArousaltxt.tStartRefresh)
            TrialLoop.addData('RateArousaltxt.stopped', RateArousaltxt.tStopRefresh)
            # the Routine "RateArousal" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ITI"-------
            # update component parameters for each repeat
            # keep track of which components have finished
            ITIComponents = [FixationCross2]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "ITI"-------
            while continueRoutine:
                # get current time
                t = ITIClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ITIClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *FixationCross2* updates
                if FixationCross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FixationCross2.frameNStart = frameN  # exact frame index
                    FixationCross2.tStart = t  # local t and not account for scr refresh
                    FixationCross2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FixationCross2, 'tStartRefresh')  # time at next scr refresh
                    FixationCross2.setAutoDraw(True)
                if FixationCross2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > FixationCross2.tStartRefresh + ITI-frameTolerance:
                        # keep track of stop time/frame for later
                        FixationCross2.tStop = t  # not accounting for scr refresh
                        FixationCross2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FixationCross2, 'tStopRefresh')  # time at next scr refresh
                        FixationCross2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ITI"-------
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrialLoop.addData('FixationCross2.started', FixationCross2.tStartRefresh)
            TrialLoop.addData('FixationCross2.stopped', FixationCross2.tStopRefresh)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed num_type repeats of 'TrialLoop'
        
        thisExp.nextEntry()
        
    # completed num_secblock repeats of 'BlockLoop'
    
    
    # ------Prepare to start Routine "BreakCode"-------
    # update component parameters for each repeat
    #Create break screen text so that the first three are breaks, and the fourth is to take the cap off.
    
    if cur_section < 4:
        textbreak = f'You are at a scheduled break! Please wait for the researcher to come in and adjust your cap. Once the cap is adjusted, they will close the door and start the experiment again for you.'
    else:
        textbreak = f'You have completed the EEG portion of the experiment! Please press the s key on the keyboard and wait for the researcher to come in and remove your cap.'
    # keep track of which components have finished
    BreakCodeComponents = []
    for thisComponent in BreakCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "BreakCode"-------
    while continueRoutine:
        # get current time
        t = BreakCodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakCodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BreakCode"-------
    for thisComponent in BreakCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BreakCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "BreakScreen"-------
    # update component parameters for each repeat
    BreakText.setText(textbreak)
    Cont_resp.keys = []
    Cont_resp.rt = []
    # keep track of which components have finished
    BreakScreenComponents = [BreakText, Cont_resp]
    for thisComponent in BreakScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "BreakScreen"-------
    while continueRoutine:
        # get current time
        t = BreakScreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakScreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BreakText* updates
        if BreakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BreakText.frameNStart = frameN  # exact frame index
            BreakText.tStart = t  # local t and not account for scr refresh
            BreakText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BreakText, 'tStartRefresh')  # time at next scr refresh
            BreakText.setAutoDraw(True)
        
        # *Cont_resp* updates
        waitOnFlip = False
        if Cont_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cont_resp.frameNStart = frameN  # exact frame index
            Cont_resp.tStart = t  # local t and not account for scr refresh
            Cont_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cont_resp, 'tStartRefresh')  # time at next scr refresh
            Cont_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Cont_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Cont_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Cont_resp.status == STARTED and not waitOnFlip:
            theseKeys = Cont_resp.getKeys(keyList=['s'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Cont_resp.keys = theseKeys.name  # just the last key pressed
                Cont_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BreakScreen"-------
    for thisComponent in BreakScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SectionLoop.addData('BreakText.started', BreakText.tStartRefresh)
    SectionLoop.addData('BreakText.stopped', BreakText.tStopRefresh)
    # check responses
    if Cont_resp.keys in ['', [], None]:  # No response was made
        Cont_resp.keys = None
    SectionLoop.addData('Cont_resp.keys',Cont_resp.keys)
    if Cont_resp.keys != None:  # we had a response
        SectionLoop.addData('Cont_resp.rt', Cont_resp.rt)
    SectionLoop.addData('Cont_resp.started', Cont_resp.tStartRefresh)
    SectionLoop.addData('Cont_resp.stopped', Cont_resp.tStopRefresh)
    # the Routine "BreakScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_sections repeats of 'SectionLoop'


# ------Prepare to start Routine "StudyEnd"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
StudyEndComponents = [Endtext]
for thisComponent in StudyEndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StudyEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "StudyEnd"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StudyEndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StudyEndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Endtext* updates
    if Endtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Endtext.frameNStart = frameN  # exact frame index
        Endtext.tStart = t  # local t and not account for scr refresh
        Endtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Endtext, 'tStartRefresh')  # time at next scr refresh
        Endtext.setAutoDraw(True)
    if Endtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Endtext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            Endtext.tStop = t  # not accounting for scr refresh
            Endtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Endtext, 'tStopRefresh')  # time at next scr refresh
            Endtext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StudyEndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StudyEnd"-------
for thisComponent in StudyEndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Endtext.started', Endtext.tStartRefresh)
thisExp.addData('Endtext.stopped', Endtext.tStopRefresh)
#can print the stim_order to cross-check with output file.
print(stim_order)

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
