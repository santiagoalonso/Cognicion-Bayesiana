import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.image import imread 
from matplotlib.colors import rgb_to_hsv 
import colorsys
from copy import deepcopy 
import seaborn as sns


def dropdown_callback(distr):
    
    if distr == 0:
        x = np.random.normal(0,1,10000)
        distr = 'Normal'
    elif distr == 1:
        x = np.random.uniform(-2,2,10000)
        distr = 'Uniform'
    elif distr == 2:
        x = np.random.lognormal(0,1,10000)
        distr = 'Log-Normal'

    
    fig = plt.figure(constrained_layout=True, figsize = (3.5,3.5))
    gs = GridSpec(1, 1, figure = fig)
    ax1 = fig.add_subplot(gs[0,0])
    #ax2 = fig.add_subplot(gs[0, 4:7])
    sns.kdeplot(data=x, ax = ax1)
    ax1.set_xlabel('Random Variable')
    ax1.set_ylabel('Density')
    ax1.set_title(distr) 

def dropdown_convergence(param, trace):
    bysubj = ['alpha_N', 'beta_N', 'gamma_N', 'delta_N', 'lambda_N',
            'luce_N', 'alpha', 'beta', 'gamma', 'delta', 'lambbda',
            'luce']
    if param in bysubj: #subject-level parameters
        subj = np.random.randint(trace[param].shape[1]) #plots random subject
        y = np.array(trace[param][:,subj])
        x = np.linspace(0,trace[param].shape[0], len(y))
        plt.plot(x,y)
        plt.title(param);
    else: #group-level parameters
        y = np.array(trace[param])
        x = np.linspace(0,len(y), len(y))
        plt.plot(x,y)
        plt.title(param);
            
    
def slider_econ_risk(alpha):
    x = np.linspace(0,5,100)
    y = x**(alpha)
    if alpha < 1:
        title = 'Averso al riesgo'
        co = 'green'
    elif alpha == 1:
        title = 'Neutro'
        co = 'gray'
    elif alpha > 1:
        title = 'Propenso al riesgo'
        co = 'red'
            
    
    fig = plt.figure(constrained_layout=True, figsize = (7,3.5))
    gs = GridSpec(1, 2, figure = fig)
    ax1 = fig.add_subplot(gs[0,0])
    sns.lineplot(x = x, y = y, ax = ax1, color = co)
    ax2 = fig.add_subplot(gs[0,1])
    ax2.axis('off')
    ax2.text(0.5,0.5, r'$ U(x) = x^\alpha$', fontsize = 25)
    ax1.set_title(title)
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Utilidad')
    
    
def slider_econ_beh_risk(alpha_win, alpha_lose, loss_aversion):
    # win
    x_win = np.linspace(0,1500,100)
    y_win = x_win**(alpha_win)

    # lose
    x_lose = np.linspace(-1500,0,100)
    y_lose = -loss_aversion*(-x_lose)**(alpha_lose)

    fig = plt.figure(constrained_layout=True, figsize = (9,3.5))
    gs = GridSpec(1, 2, figure = fig)
    ax1 = fig.add_subplot(gs[0,0])
    sns.lineplot(x = x_win, y = y_win, ax = ax1, color = 'black')
    sns.lineplot(x = x_lose, y = y_lose, ax = ax1, color = 'red')
    ax2 = fig.add_subplot(gs[0,1])
    ax2.axis('off')
    ax2.text(0.5,0.5, r'$ U_{win}(x) = x^{\alpha_{win}}$', fontsize = 25)
    ax2.text(0.5,0.25, r'$ U_{loss}(x) = -\lambda(-x)^{\alpha_{lose}}$', fontsize = 25)
    ax1.set_title('Utilidad de Prospect Theory')
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Utilidad');
    
def slider_econ_beh_prob(theta):
    prob = np.linspace(0,1,100)
    prob_percept = np.exp(-(-np.log(prob))**theta)

    fig = plt.figure(constrained_layout=True, figsize = (9,3.5))
    gs = GridSpec(1, 2, figure = fig)
    ax1 = fig.add_subplot(gs[0,0])
    sns.lineplot(x = prob, y = prob_percept, ax = ax1, color = 'black')
    sns.lineplot(x = prob, y = prob, color = 'black')
    ax1.lines[1].set_linestyle("--")
    ax2 = fig.add_subplot(gs[0,1])
    ax2.axis('off')
    ax2.text(0.5,0.5, r'$ W(p) = e^{-(-ln(p)^\theta)}$', fontsize = 25)
    ax1.set_title('W (p) de Prospect Theory')
    ax1.set_xlabel('Prob.')
    ax1.set_ylabel('Percepción de prob.');
    


def value_fun(x, alpha, beta, lambbda):
    #x: [reward1, reward2]; dataframe
    #alpha, beta: risk attitudes (win, lose)
    #lambbda: loss aversion   
    if (x>=0).all().all():
        return x**alpha
    elif (x<=0).all().all():
        return -lambbda*((-x)**beta)
    else: #mix
        if (x.iloc[:,0]>=0).all():
            return pd.concat([x.iloc[:,0]**alpha, 
                             -lambbda*((-x.iloc[:,1])**beta)], axis=1)
        else:
            return pd.concat([-lambbda*((-x.iloc[:,0])**beta), 
                             x.iloc[:,1]**alpha], axis=1)
            
def weight_fun(x, p, gamma, delta):
    #x: [reward1, reward2]; 
    #p: [prob1, prob2]; 
    #gamma, delta: non-linear prob. perception (win, lose)
    
    if (x>=0).all().all():
        num = p**gamma
        den = pd.concat([num.sum(axis=1)**(1/gamma),
                         num.sum(axis=1)**(1/gamma)], axis=1)        
    elif (x<=0).all().all():
        num = p**delta
        den = pd.concat([num.sum(axis=1)**(1/delta),
                         num.sum(axis=1)**(1/delta)], axis=1)
    else: #mix
        if (x.iloc[:,0]>=0).all():
            num = pd.concat([p.iloc[:,0]**gamma, 
                             p.iloc[:,1]**delta], axis=1)
            den = pd.concat([num.sum(axis=1)**(1/gamma),
                            num.sum(axis=1)**(1/delta)], axis=1)
        else:
            num = pd.concat([p.iloc[:,0]**delta, 
                             p.iloc[:,1]**gamma], axis=1)
            den = pd.concat([num.sum()**(1/delta),
                            num.sum()**(1/gamma)], axis=1)
    
    num.columns = ['Prob_1', 'Prob_2']
    den.columns = ['Prob_1', 'Prob_2']
    
    return num/den

def EV(v,w):
    # v (value) and w (prob. weights)
    # v and w are the output of value_fun and weight_fun
    return pd.DataFrame(v.values*w.values).sum(axis=1)
    
def choice_rule(EV, luce):
    return 1/(1+np.exp(luce*(EV.iloc[:,0] - EV.iloc[:,1]))) #prob. of EV[1]

    