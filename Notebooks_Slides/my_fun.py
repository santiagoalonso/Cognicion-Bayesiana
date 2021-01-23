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
    sns.lineplot(x,y, ax = ax1, color = co)
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
    sns.lineplot(x_win, y_win, ax = ax1, color = 'black')
    sns.lineplot(x_lose, y_lose, ax = ax1, color = 'red')
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
    sns.lineplot(prob, prob_percept, ax = ax1, color = 'black')
    sns.lineplot(prob, prob, color = 'black')
    ax1.lines[1].set_linestyle("--")
    ax2 = fig.add_subplot(gs[0,1])
    ax2.axis('off')
    ax2.text(0.5,0.5, r'$ W(p) = e^{-(-ln(p)^\theta)}$', fontsize = 25)
    ax1.set_title('W (p) de Prospect Theory')
    ax1.set_xlabel('Prob.')
    ax1.set_ylabel('Percepción de prob.');
    
    
    