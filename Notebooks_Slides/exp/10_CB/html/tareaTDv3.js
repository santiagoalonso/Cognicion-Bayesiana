/****************** 
 * Tareatdv3 Test *
 ******************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'tareaTDv3';  // from the Builder filename that created this script
let expInfo = {'session': '002', 'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Inst1RoutineBegin());
flowScheduler.add(Inst1RoutineEachFrame());
flowScheduler.add(Inst1RoutineEnd());
flowScheduler.add(Instr2RoutineBegin());
flowScheduler.add(Instr2RoutineEachFrame());
flowScheduler.add(Instr2RoutineEnd());
flowScheduler.add(Inst2_2RoutineBegin());
flowScheduler.add(Inst2_2RoutineEachFrame());
flowScheduler.add(Inst2_2RoutineEnd());
flowScheduler.add(Inst2_3RoutineBegin());
flowScheduler.add(Inst2_3RoutineEachFrame());
flowScheduler.add(Inst2_3RoutineEnd());
flowScheduler.add(Inst3RoutineBegin());
flowScheduler.add(Inst3RoutineEachFrame());
flowScheduler.add(Inst3RoutineEnd());
flowScheduler.add(Inst4RoutineBegin());
flowScheduler.add(Inst4RoutineEachFrame());
flowScheduler.add(Inst4RoutineEnd());
const PracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopBegin, PracticeLoopScheduler);
flowScheduler.add(PracticeLoopScheduler);
flowScheduler.add(PracticeLoopEnd);
flowScheduler.add(Instr5RoutineBegin());
flowScheduler.add(Instr5RoutineEachFrame());
flowScheduler.add(Instr5RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(FinRoutineBegin());
flowScheduler.add(FinRoutineEachFrame());
flowScheduler.add(FinRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.5';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var Inst1Clock;
var intro1;
var key1;
var Instr2Clock;
var intro2;
var key2;
var Inst2_2Clock;
var intro2_2;
var key2_2;
var Inst2_3Clock;
var Intro2_3;
var key2_3;
var Inst3Clock;
var key3;
var intro3;
var ss_am;
var ss_del;
var ll_am;
var ll_del;
var Inst4Clock;
var Intro4;
var key4;
var PractClock;
var targetPosAmSS;
var targetPosAmLL;
var targetPosDelSS;
var targetPosDelLL;
var positionsAm;
var positionsDel;
var responses;
var indices;
var pregunta;
var ssAm_P;
var ssDel_P;
var llAm_P;
var llDel_P;
var respP;
var fb_PractClock;
var msg;
var feedbackP;
var Instr5Clock;
var comienzo;
var key5;
var ITCClock;
var preguntaT;
var ssAm_T;
var ssDel_T;
var llAm_T;
var llDel_T;
var respT;
var fb_TrialsClock;
var textfbT;
var FinClock;
var Gracias;
var key_resp_4;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Inst1"
  Inst1Clock = new util.Clock();
  intro1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro1',
    text: 'A continuación vas a completar una tarea computarizada en la que tomarás una serie de decisiones.\n\nPresiona la barra de espacio para continuar.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instr2"
  Instr2Clock = new util.Clock();
  intro2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro2',
    text: 'Todas las decisiones que tendrás que tomar serán elecciones entre dos opciones de recompensas monetarias que podrías recibir: una opción de dinero que obtendrías hoy contra una opción de dinero que obtendrías en el futuro. \n\nEn cada pregunta, las cantidades de dinero ofrecido y el número de días que habría que esperar en el futuro cambiarán. \n\nEn cada pregunta, la opción inmediata y la  opción futura cambiarán de lado en la pantalla, así que debes poner atención para responder con el teclado cuál es tu preferencia.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst2_2"
  Inst2_2Clock = new util.Clock();
  intro2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro2_2',
    text: 'Aunque estas decisiones son hipotéticas, te pedimos que hagas cada elección con honestidad, es decir, que respondas cuál es tu verdadera preferencia tal y como si fuéramos a darte el dinero que escogiste en la fecha en la que escogiste.\n\nEs muy importante que sepas que en esta tarea NO HAY respuestas correctas o incorrectas, cada pregunta es sobre TU preferencia, así que tus respuestas pueden ser muy distintas de las de otra persona. Por este motivo, te recomendamos que contestes con sinceridad para que tus respuestas reflejen tus preferencias únicas.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key2_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst2_3"
  Inst2_3Clock = new util.Clock();
  Intro2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Intro2_3',
    text: 'Si escoges la opción de la izquierda oprime la flecha hacia la izquierda, si escoges la opción de la derecha oprime la flecha hacia la derecha',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key2_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Inst3"
  Inst3Clock = new util.Clock();
  key3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  intro3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro3',
    text: 'Por ejemplo, ¿qué preferirías?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ss_am = new visual.TextStim({
    win: psychoJS.window,
    name: 'ss_am',
    text: '$5.000',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  ss_del = new visual.TextStim({
    win: psychoJS.window,
    name: 'ss_del',
    text: 'hoy',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.1)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ll_am = new visual.TextStim({
    win: psychoJS.window,
    name: 'll_am',
    text: '$10.000',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, 0.1], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  ll_del = new visual.TextStim({
    win: psychoJS.window,
    name: 'll_del',
    text: 'en 7 días',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.1)], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Inst4"
  Inst4Clock = new util.Clock();
  Intro4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Intro4',
    text: 'Hagamos unos ensayos de práctica',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pract"
  PractClock = new util.Clock();
  targetPosAmSS = [];
  targetPosAmLL = [];
  targetPosDelSS = [];
  targetPosDelLL = [];
  positionsAm = [[(- 0.5), 0.1], [0.5, 0.1]];
  positionsDel = [[(- 0.5), (- 0.1)], [0.5, (- 0.1)]];
  responses = ["left", "right"];
  indices = [0, 1];
  
  pregunta = new visual.TextStim({
    win: psychoJS.window,
    name: 'pregunta',
    text: '¿qué preferirías?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ssAm_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssAm_P',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  ssDel_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssDel_P',
    text: 'hoy',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  llAm_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'llAm_P',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  llDel_P = new visual.TextStim({
    win: psychoJS.window,
    name: 'llDel_P',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  respP = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fb_Pract"
  fb_PractClock = new util.Clock();
  msg = "";
  
  feedbackP = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackP',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instr5"
  Instr5Clock = new util.Clock();
  comienzo = new visual.TextStim({
    win: psychoJS.window,
    name: 'comienzo',
    text: 'Ahora sí vamos a empezar con la tarea. Recuerda que debes contestar todas las preguntas. Tienes 20 segundos por cada pregunta. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITC"
  ITCClock = new util.Clock();
  targetPosAmSS = [];
  targetPosAmLL = [];
  targetPosDelSS = [];
  targetPosDelLL = [];
  positionsAm = [[(- 0.5), 0.1], [0.5, 0.1]];
  positionsDel = [[(- 0.5), (- 0.1)], [0.5, (- 0.1)]];
  responses = ["left", "right"];
  indices = [0, 1];
  
  preguntaT = new visual.TextStim({
    win: psychoJS.window,
    name: 'preguntaT',
    text: '¿qué preferirías?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ssAm_T = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssAm_T',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  ssDel_T = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssDel_T',
    text: 'hoy',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  llAm_T = new visual.TextStim({
    win: psychoJS.window,
    name: 'llAm_T',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  llDel_T = new visual.TextStim({
    win: psychoJS.window,
    name: 'llDel_T',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  respT = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fb_Trials"
  fb_TrialsClock = new util.Clock();
  msg = "";
  
  textfbT = new visual.TextStim({
    win: psychoJS.window,
    name: 'textfbT',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Fin"
  FinClock = new util.Clock();
  Gracias = new visual.TextStim({
    win: psychoJS.window,
    name: 'Gracias',
    text: 'Terminaste!\n\nMuchas gracias por participar!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key1_allKeys;
var Inst1Components;
function Inst1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst1'-------
    t = 0;
    Inst1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key1.keys = undefined;
    key1.rt = undefined;
    _key1_allKeys = [];
    // keep track of which components have finished
    Inst1Components = [];
    Inst1Components.push(intro1);
    Inst1Components.push(key1);
    
    for (const thisComponent of Inst1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var continueRoutine;
function Inst1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inst1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro1* updates
    if (t >= 0.0 && intro1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro1.tStart = t;  // (not accounting for frame time here)
      intro1.frameNStart = frameN;  // exact frame index
      
      intro1.setAutoDraw(true);
    }

    
    // *key1* updates
    if (t >= 0.5 && key1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key1.tStart = t;  // (not accounting for frame time here)
      key1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key1.clearEvents(); });
    }

    if (key1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key1.getKeys({keyList: ['space'], waitRelease: false});
      _key1_allKeys = _key1_allKeys.concat(theseKeys);
      if (_key1_allKeys.length > 0) {
        key1.keys = _key1_allKeys[_key1_allKeys.length - 1].name;  // just the last key pressed
        key1.rt = _key1_allKeys[_key1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst1'-------
    for (const thisComponent of Inst1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key1.keys', key1.keys);
    if (typeof key1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key1.rt', key1.rt);
        routineTimer.reset();
        }
    
    key1.stop();
    // the Routine "Inst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key2_allKeys;
var Instr2Components;
function Instr2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instr2'-------
    t = 0;
    Instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key2.keys = undefined;
    key2.rt = undefined;
    _key2_allKeys = [];
    // keep track of which components have finished
    Instr2Components = [];
    Instr2Components.push(intro2);
    Instr2Components.push(key2);
    
    for (const thisComponent of Instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro2* updates
    if (t >= 0 && intro2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro2.tStart = t;  // (not accounting for frame time here)
      intro2.frameNStart = frameN;  // exact frame index
      
      intro2.setAutoDraw(true);
    }

    
    // *key2* updates
    if (t >= 0.5 && key2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key2.tStart = t;  // (not accounting for frame time here)
      key2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key2.clearEvents(); });
    }

    if (key2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key2.getKeys({keyList: ['space'], waitRelease: false});
      _key2_allKeys = _key2_allKeys.concat(theseKeys);
      if (_key2_allKeys.length > 0) {
        key2.keys = _key2_allKeys[_key2_allKeys.length - 1].name;  // just the last key pressed
        key2.rt = _key2_allKeys[_key2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instr2'-------
    for (const thisComponent of Instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key2.keys', key2.keys);
    if (typeof key2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key2.rt', key2.rt);
        routineTimer.reset();
        }
    
    key2.stop();
    // the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key2_2_allKeys;
var Inst2_2Components;
function Inst2_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst2_2'-------
    t = 0;
    Inst2_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key2_2.keys = undefined;
    key2_2.rt = undefined;
    _key2_2_allKeys = [];
    // keep track of which components have finished
    Inst2_2Components = [];
    Inst2_2Components.push(intro2_2);
    Inst2_2Components.push(key2_2);
    
    for (const thisComponent of Inst2_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst2_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst2_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inst2_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro2_2* updates
    if (t >= 0.0 && intro2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro2_2.tStart = t;  // (not accounting for frame time here)
      intro2_2.frameNStart = frameN;  // exact frame index
      
      intro2_2.setAutoDraw(true);
    }

    
    // *key2_2* updates
    if (t >= 0.5 && key2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key2_2.tStart = t;  // (not accounting for frame time here)
      key2_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key2_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key2_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key2_2.clearEvents(); });
    }

    if (key2_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key2_2.getKeys({keyList: ['space'], waitRelease: false});
      _key2_2_allKeys = _key2_2_allKeys.concat(theseKeys);
      if (_key2_2_allKeys.length > 0) {
        key2_2.keys = _key2_2_allKeys[_key2_2_allKeys.length - 1].name;  // just the last key pressed
        key2_2.rt = _key2_2_allKeys[_key2_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst2_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst2_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst2_2'-------
    for (const thisComponent of Inst2_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key2_2.keys', key2_2.keys);
    if (typeof key2_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key2_2.rt', key2_2.rt);
        routineTimer.reset();
        }
    
    key2_2.stop();
    // the Routine "Inst2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key2_3_allKeys;
var Inst2_3Components;
function Inst2_3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst2_3'-------
    t = 0;
    Inst2_3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key2_3.keys = undefined;
    key2_3.rt = undefined;
    _key2_3_allKeys = [];
    // keep track of which components have finished
    Inst2_3Components = [];
    Inst2_3Components.push(Intro2_3);
    Inst2_3Components.push(key2_3);
    
    for (const thisComponent of Inst2_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst2_3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst2_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inst2_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Intro2_3* updates
    if (t >= 0.0 && Intro2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro2_3.tStart = t;  // (not accounting for frame time here)
      Intro2_3.frameNStart = frameN;  // exact frame index
      
      Intro2_3.setAutoDraw(true);
    }

    
    // *key2_3* updates
    if (t >= 0.5 && key2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key2_3.tStart = t;  // (not accounting for frame time here)
      key2_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key2_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key2_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key2_3.clearEvents(); });
    }

    if (key2_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key2_3.getKeys({keyList: ['space'], waitRelease: false});
      _key2_3_allKeys = _key2_3_allKeys.concat(theseKeys);
      if (_key2_3_allKeys.length > 0) {
        key2_3.keys = _key2_3_allKeys[_key2_3_allKeys.length - 1].name;  // just the last key pressed
        key2_3.rt = _key2_3_allKeys[_key2_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst2_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst2_3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst2_3'-------
    for (const thisComponent of Inst2_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key2_3.keys', key2_3.keys);
    if (typeof key2_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key2_3.rt', key2_3.rt);
        routineTimer.reset();
        }
    
    key2_3.stop();
    // the Routine "Inst2_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key3_allKeys;
var Inst3Components;
function Inst3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst3'-------
    t = 0;
    Inst3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key3.keys = undefined;
    key3.rt = undefined;
    _key3_allKeys = [];
    // keep track of which components have finished
    Inst3Components = [];
    Inst3Components.push(key3);
    Inst3Components.push(intro3);
    Inst3Components.push(ss_am);
    Inst3Components.push(ss_del);
    Inst3Components.push(ll_am);
    Inst3Components.push(ll_del);
    
    for (const thisComponent of Inst3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inst3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key3* updates
    if (t >= 0.5 && key3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key3.tStart = t;  // (not accounting for frame time here)
      key3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key3.clearEvents(); });
    }

    if (key3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key3.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key3_allKeys = _key3_allKeys.concat(theseKeys);
      if (_key3_allKeys.length > 0) {
        key3.keys = _key3_allKeys[_key3_allKeys.length - 1].name;  // just the last key pressed
        key3.rt = _key3_allKeys[_key3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *intro3* updates
    if (t >= 0.0 && intro3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro3.tStart = t;  // (not accounting for frame time here)
      intro3.frameNStart = frameN;  // exact frame index
      
      intro3.setAutoDraw(true);
    }

    
    // *ss_am* updates
    if (t >= 0.0 && ss_am.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ss_am.tStart = t;  // (not accounting for frame time here)
      ss_am.frameNStart = frameN;  // exact frame index
      
      ss_am.setAutoDraw(true);
    }

    
    // *ss_del* updates
    if (t >= 0.0 && ss_del.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ss_del.tStart = t;  // (not accounting for frame time here)
      ss_del.frameNStart = frameN;  // exact frame index
      
      ss_del.setAutoDraw(true);
    }

    
    // *ll_am* updates
    if (t >= 0.0 && ll_am.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ll_am.tStart = t;  // (not accounting for frame time here)
      ll_am.frameNStart = frameN;  // exact frame index
      
      ll_am.setAutoDraw(true);
    }

    
    // *ll_del* updates
    if (t >= 0.0 && ll_del.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ll_del.tStart = t;  // (not accounting for frame time here)
      ll_del.frameNStart = frameN;  // exact frame index
      
      ll_del.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst3'-------
    for (const thisComponent of Inst3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key3.keys', key3.keys);
    if (typeof key3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key3.rt', key3.rt);
        routineTimer.reset();
        }
    
    key3.stop();
    // the Routine "Inst3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key4_allKeys;
var Inst4Components;
function Inst4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Inst4'-------
    t = 0;
    Inst4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key4.keys = undefined;
    key4.rt = undefined;
    _key4_allKeys = [];
    // keep track of which components have finished
    Inst4Components = [];
    Inst4Components.push(Intro4);
    Inst4Components.push(key4);
    
    for (const thisComponent of Inst4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Inst4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Inst4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Intro4* updates
    if (t >= 0.0 && Intro4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro4.tStart = t;  // (not accounting for frame time here)
      Intro4.frameNStart = frameN;  // exact frame index
      
      Intro4.setAutoDraw(true);
    }

    
    // *key4* updates
    if (t >= 0.5 && key4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key4.tStart = t;  // (not accounting for frame time here)
      key4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key4.clearEvents(); });
    }

    if (key4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key4.getKeys({keyList: ['space'], waitRelease: false});
      _key4_allKeys = _key4_allKeys.concat(theseKeys);
      if (_key4_allKeys.length > 0) {
        key4.keys = _key4_allKeys[_key4_allKeys.length - 1].name;  // just the last key pressed
        key4.rt = _key4_allKeys[_key4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Inst4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Inst4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Inst4'-------
    for (const thisComponent of Inst4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key4.keys', key4.keys);
    if (typeof key4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key4.rt', key4.rt);
        routineTimer.reset();
        }
    
    key4.stop();
    // the Routine "Inst4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Practice;
var currentLoop;
function PracticeLoopBegin(PracticeLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'choiceSet_practice.xlsx',
    seed: undefined, name: 'Practice'
  });
  psychoJS.experiment.addLoop(Practice); // add the loop to the experiment
  currentLoop = Practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice of Practice) {
    const snapshot = Practice.getSnapshot();
    PracticeLoopScheduler.add(importConditions(snapshot));
    PracticeLoopScheduler.add(PractRoutineBegin(snapshot));
    PracticeLoopScheduler.add(PractRoutineEachFrame(snapshot));
    PracticeLoopScheduler.add(PractRoutineEnd(snapshot));
    PracticeLoopScheduler.add(fb_PractRoutineBegin(snapshot));
    PracticeLoopScheduler.add(fb_PractRoutineEachFrame(snapshot));
    PracticeLoopScheduler.add(fb_PractRoutineEnd(snapshot));
    PracticeLoopScheduler.add(endLoopIteration(PracticeLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function PracticeLoopEnd() {
  psychoJS.experiment.removeLoop(Practice);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'choiceSet_trials.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(ITCRoutineBegin(snapshot));
    trialsLoopScheduler.add(ITCRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ITCRoutineEnd(snapshot));
    trialsLoopScheduler.add(fb_TrialsRoutineBegin(snapshot));
    trialsLoopScheduler.add(fb_TrialsRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fb_TrialsRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var corrAns;
var _respP_allKeys;
var PractComponents;
function PractRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Pract'-------
    t = 0;
    PractClock.reset(); // clock
    frameN = -1;
    routineTimer.add(20.000000);
    // create a function to shuffle a list
function shuffle(a) {
  var j, x, i;
  for (i = a.length - 1; i > 0; i--) {
      j = Math.floor(Math.random() * (i + 1));
      x = a[i];
      a[i] = a[j];
      a[j] = x;
  }
  return a;
}
    // update component parameters for each repeat
    shuffle(indices);
    targetPosAmSS = positionsAm[indices[0]];
    targetPosAmLL = positionsAm[indices[1]];
    targetPosDelSS = positionsDel[indices[0]];
    targetPosDelLL = positionsDel[indices[1]];
    corrAns = responses[indices[1]];
    
    ssAm_P.setPos(targetPosAmSS);
    ssAm_P.setText("${0}".format(ssAmount));
    ssDel_P.setPos(targetPosDelSS);
    llAm_P.setPos(targetPosAmLL);
    llAm_P.setText("${0}".format(llAmount));
    llDel_P.setPos(targetPosDelLL);
    llDel_P.setText("en {0} días".format(llDelay));
    respP.keys = undefined;
    respP.rt = undefined;
    _respP_allKeys = [];
    // keep track of which components have finished
    PractComponents = [];
    PractComponents.push(pregunta);
    PractComponents.push(ssAm_P);
    PractComponents.push(ssDel_P);
    PractComponents.push(llAm_P);
    PractComponents.push(llDel_P);
    PractComponents.push(respP);
    
    for (const thisComponent of PractComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var frameRemains;
function PractRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Pract'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PractClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pregunta* updates
    if (t >= 0.0 && pregunta.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pregunta.tStart = t;  // (not accounting for frame time here)
      pregunta.frameNStart = frameN;  // exact frame index
      
      pregunta.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((pregunta.status === PsychoJS.Status.STARTED || pregunta.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      pregunta.setAutoDraw(false);
    }
    
    // *ssAm_P* updates
    if (t >= 0.0 && ssAm_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssAm_P.tStart = t;  // (not accounting for frame time here)
      ssAm_P.frameNStart = frameN;  // exact frame index
      
      ssAm_P.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ssAm_P.status === PsychoJS.Status.STARTED || ssAm_P.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ssAm_P.setAutoDraw(false);
    }
    
    // *ssDel_P* updates
    if (t >= 0.0 && ssDel_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssDel_P.tStart = t;  // (not accounting for frame time here)
      ssDel_P.frameNStart = frameN;  // exact frame index
      
      ssDel_P.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ssDel_P.status === PsychoJS.Status.STARTED || ssDel_P.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ssDel_P.setAutoDraw(false);
    }
    
    // *llAm_P* updates
    if (t >= 0.0 && llAm_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      llAm_P.tStart = t;  // (not accounting for frame time here)
      llAm_P.frameNStart = frameN;  // exact frame index
      
      llAm_P.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((llAm_P.status === PsychoJS.Status.STARTED || llAm_P.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      llAm_P.setAutoDraw(false);
    }
    
    // *llDel_P* updates
    if (t >= 0.0 && llDel_P.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      llDel_P.tStart = t;  // (not accounting for frame time here)
      llDel_P.frameNStart = frameN;  // exact frame index
      
      llDel_P.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((llDel_P.status === PsychoJS.Status.STARTED || llDel_P.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      llDel_P.setAutoDraw(false);
    }
    
    // *respP* updates
    if (t >= 0.5 && respP.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respP.tStart = t;  // (not accounting for frame time here)
      respP.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respP.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respP.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respP.clearEvents(); });
    }

    frameRemains = 0.5 + 19.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((respP.status === PsychoJS.Status.STARTED || respP.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      respP.status = PsychoJS.Status.FINISHED;
  }

    if (respP.status === PsychoJS.Status.STARTED) {
      let theseKeys = respP.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _respP_allKeys = _respP_allKeys.concat(theseKeys);
      if (_respP_allKeys.length > 0) {
        respP.keys = _respP_allKeys[_respP_allKeys.length - 1].name;  // just the last key pressed
        respP.rt = _respP_allKeys[_respP_allKeys.length - 1].rt;
        // was this correct?
        if (respP.keys == corrAns) {
            respP.corr = 1;
        } else {
            respP.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PractComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PractRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Pract'-------
    for (const thisComponent of PractComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (respP.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         respP.corr = 1;  // correct non-response
      } else {
         respP.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('respP.keys', respP.keys);
    psychoJS.experiment.addData('respP.corr', respP.corr);
    if (typeof respP.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respP.rt', respP.rt);
        routineTimer.reset();
        }
    
    respP.stop();
    return Scheduler.Event.NEXT;
  };
}


var fb_PractComponents;
function fb_PractRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fb_Pract'-------
    t = 0;
    fb_PractClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    if ((! respP.keys)) {
        msg = "No respondiste a tiempo!";
    } else {
        if (respP.corr) {
            msg = "Elegiste esperar";
        } else {
            msg = "Elegiste no esperar";
        }
    }
    
    feedbackP.setText(msg);
    // keep track of which components have finished
    fb_PractComponents = [];
    fb_PractComponents.push(feedbackP);
    
    for (const thisComponent of fb_PractComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_PractRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fb_Pract'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fb_PractClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbackP* updates
    if (t >= 0.0 && feedbackP.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackP.tStart = t;  // (not accounting for frame time here)
      feedbackP.frameNStart = frameN;  // exact frame index
      
      feedbackP.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((feedbackP.status === PsychoJS.Status.STARTED || feedbackP.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      feedbackP.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fb_PractComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_PractRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fb_Pract'-------
    for (const thisComponent of fb_PractComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key5_allKeys;
var Instr5Components;
function Instr5RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instr5'-------
    t = 0;
    Instr5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key5.keys = undefined;
    key5.rt = undefined;
    _key5_allKeys = [];
    // keep track of which components have finished
    Instr5Components = [];
    Instr5Components.push(comienzo);
    Instr5Components.push(key5);
    
    for (const thisComponent of Instr5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr5RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instr5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Instr5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comienzo* updates
    if (t >= 0.0 && comienzo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comienzo.tStart = t;  // (not accounting for frame time here)
      comienzo.frameNStart = frameN;  // exact frame index
      
      comienzo.setAutoDraw(true);
    }

    
    // *key5* updates
    if (t >= 0.5 && key5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key5.tStart = t;  // (not accounting for frame time here)
      key5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key5.clearEvents(); });
    }

    if (key5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key5.getKeys({keyList: ['g'], waitRelease: false});
      _key5_allKeys = _key5_allKeys.concat(theseKeys);
      if (_key5_allKeys.length > 0) {
        key5.keys = _key5_allKeys[_key5_allKeys.length - 1].name;  // just the last key pressed
        key5.rt = _key5_allKeys[_key5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr5RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instr5'-------
    for (const thisComponent of Instr5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key5.keys', key5.keys);
    if (typeof key5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key5.rt', key5.rt);
        routineTimer.reset();
        }
    
    key5.stop();
    // the Routine "Instr5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _respT_allKeys;
var ITCComponents;
function ITCRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ITC'-------
    t = 0;
    ITCClock.reset(); // clock
    frameN = -1;
    routineTimer.add(20.000000);
    // create a function to shuffle a list
function shuffle(a) {
  var j, x, i;
  for (i = a.length - 1; i > 0; i--) {
      j = Math.floor(Math.random() * (i + 1));
      x = a[i];
      a[i] = a[j];
      a[j] = x;
  }
  return a;
}
    // update component parameters for each repeat
    shuffle(indices);
    targetPosAmSS = positionsAm[indices[0]];
    targetPosAmLL = positionsAm[indices[1]];
    targetPosDelSS = positionsDel[indices[0]];
    targetPosDelLL = positionsDel[indices[1]];
    corrAns = responses[indices[1]];
    
    ssAm_T.setPos(targetPosAmSS);
    ssAm_T.setText("${0}".format(ss_Amt));
    ssDel_T.setPos(targetPosDelSS);
    llAm_T.setPos(targetPosAmLL);
    llAm_T.setText("${0}".format(ll_Amt));
    llDel_T.setPos(targetPosDelLL);
    llDel_T.setText("en {0} días".format(ll_Delay));
    respT.keys = undefined;
    respT.rt = undefined;
    _respT_allKeys = [];
    // keep track of which components have finished
    ITCComponents = [];
    ITCComponents.push(preguntaT);
    ITCComponents.push(ssAm_T);
    ITCComponents.push(ssDel_T);
    ITCComponents.push(llAm_T);
    ITCComponents.push(llDel_T);
    ITCComponents.push(respT);
    
    for (const thisComponent of ITCComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ITCRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ITC'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ITCClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *preguntaT* updates
    if (t >= 0.0 && preguntaT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      preguntaT.tStart = t;  // (not accounting for frame time here)
      preguntaT.frameNStart = frameN;  // exact frame index
      
      preguntaT.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((preguntaT.status === PsychoJS.Status.STARTED || preguntaT.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      preguntaT.setAutoDraw(false);
    }
    
    // *ssAm_T* updates
    if (t >= 0.0 && ssAm_T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssAm_T.tStart = t;  // (not accounting for frame time here)
      ssAm_T.frameNStart = frameN;  // exact frame index
      
      ssAm_T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ssAm_T.status === PsychoJS.Status.STARTED || ssAm_T.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ssAm_T.setAutoDraw(false);
    }
    
    // *ssDel_T* updates
    if (t >= 0.0 && ssDel_T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssDel_T.tStart = t;  // (not accounting for frame time here)
      ssDel_T.frameNStart = frameN;  // exact frame index
      
      ssDel_T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ssDel_T.status === PsychoJS.Status.STARTED || ssDel_T.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ssDel_T.setAutoDraw(false);
    }
    
    // *llAm_T* updates
    if (t >= 0.0 && llAm_T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      llAm_T.tStart = t;  // (not accounting for frame time here)
      llAm_T.frameNStart = frameN;  // exact frame index
      
      llAm_T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((llAm_T.status === PsychoJS.Status.STARTED || llAm_T.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      llAm_T.setAutoDraw(false);
    }
    
    // *llDel_T* updates
    if (t >= 0.0 && llDel_T.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      llDel_T.tStart = t;  // (not accounting for frame time here)
      llDel_T.frameNStart = frameN;  // exact frame index
      
      llDel_T.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((llDel_T.status === PsychoJS.Status.STARTED || llDel_T.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      llDel_T.setAutoDraw(false);
    }
    
    // *respT* updates
    if (t >= 0.5 && respT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respT.tStart = t;  // (not accounting for frame time here)
      respT.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respT.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respT.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respT.clearEvents(); });
    }

    frameRemains = 0.5 + 19.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((respT.status === PsychoJS.Status.STARTED || respT.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      respT.status = PsychoJS.Status.FINISHED;
  }

    if (respT.status === PsychoJS.Status.STARTED) {
      let theseKeys = respT.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _respT_allKeys = _respT_allKeys.concat(theseKeys);
      if (_respT_allKeys.length > 0) {
        respT.keys = _respT_allKeys[_respT_allKeys.length - 1].name;  // just the last key pressed
        respT.rt = _respT_allKeys[_respT_allKeys.length - 1].rt;
        // was this correct?
        if (respT.keys == corrAns) {
            respT.corr = 1;
        } else {
            respT.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITCComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITCRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ITC'-------
    for (const thisComponent of ITCComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (respT.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         respT.corr = 1;  // correct non-response
      } else {
         respT.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('respT.keys', respT.keys);
    psychoJS.experiment.addData('respT.corr', respT.corr);
    if (typeof respT.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respT.rt', respT.rt);
        routineTimer.reset();
        }
    
    respT.stop();
    return Scheduler.Event.NEXT;
  };
}


var fb_TrialsComponents;
function fb_TrialsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fb_Trials'-------
    t = 0;
    fb_TrialsClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    if ((! respT.keys)) {
        msg = "No respondiste a tiempo!";
    } else {
        if (respT.corr) {
            msg = "Elegiste esperar";
        } else {
            msg = "Elegiste no esperar";
        }
    }
    
    textfbT.setText(msg);
    // keep track of which components have finished
    fb_TrialsComponents = [];
    fb_TrialsComponents.push(textfbT);
    
    for (const thisComponent of fb_TrialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_TrialsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fb_Trials'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fb_TrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textfbT* updates
    if (t >= 0.0 && textfbT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textfbT.tStart = t;  // (not accounting for frame time here)
      textfbT.frameNStart = frameN;  // exact frame index
      
      textfbT.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((textfbT.status === PsychoJS.Status.STARTED || textfbT.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      textfbT.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fb_TrialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_TrialsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fb_Trials'-------
    for (const thisComponent of fb_TrialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var FinComponents;
function FinRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Fin'-------
    t = 0;
    FinClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    FinComponents = [];
    FinComponents.push(Gracias);
    FinComponents.push(key_resp_4);
    
    for (const thisComponent of FinComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function FinRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Fin'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = FinClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Gracias* updates
    if (t >= 0.0 && Gracias.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Gracias.tStart = t;  // (not accounting for frame time here)
      Gracias.frameNStart = frameN;  // exact frame index
      
      Gracias.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((key_resp_4.status === PsychoJS.Status.STARTED || key_resp_4.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FinComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Fin'-------
    for (const thisComponent of FinComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "Fin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
