import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
### TBD Zoom region inset https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html
plt.rcParams['font.family'] = 'Arial'
    
def plotWfnImage(wfn,timestep,lines=None,state=0,log=False):
    fig,ax=plt.subplots(figsize=(12, 4))
    if log == True:
        img = ax.imshow(np.log10(np.abs(wfn[timestep,:,:,state])**2),origin="lower",vmin = np.log10(1E-9),vmax = np.log10(1E-4),extent=[-3,3,-3,3])
    else:
        img = ax.imshow(np.abs(wfn[timestep,:,:,state]**2),origin="lower",extent=[-3,3,-3,3])
    # plt.hlines(x=[115, 130, 145, 160], ymin=0, ymax=img.shape[0] - 1, colors='r')  
    
    if lines:
        for line in lines:
            l = -3+line*6/256
            plt.axhline(y=l, color='white', linestyle='--')
    ax.set_xlabel('R$_2$',fontsize=18)
    ax.set_ylabel('R$_1$',fontsize=18)
    ax.tick_params(axis='both',labelsize = 14)

    t1 = ax.text(1.5,-2.75,f't={int(timestep/10)}',color = 'White',fontsize=18)
    t1.set_text(f't={int(timestep/10)}')

    if state==0:
        t2 = ax.text(-2.75,-2.75,f'Ground State',color = 'White',fontsize=18)
        t2.set_text(f'Ground State')
    else:
        t2 = ax.text(-2.75,-2.75,f'Excited State',color = 'White',fontsize=18)
        t2.set_text(f'Excited State')

    t3 = ax.text(3.1,-.09,'e.',color = 'Black',fontsize=18)
    t3.set_text('e.')
    t4 = ax.text(3.2,.23,'f.',color = 'Black',fontsize=18)
    t4.set_text('f.')
    t5 = ax.text(3.1,1.1,'g.',color = 'Black',fontsize=18)
    t5.set_text('g.')
    # ax.set_title('Nuclear Density',fontsize=20)
    plt.suptitle('Cross-Section Positions',ha='center',fontsize=20)
    
    # cbar = plt.colorbar(img,shrink=1)
    # cbar.set_label(label=r'log$_{10}$[$\rho$$_{'f'{state+1}{state+1}''}$(R)]',size=18)
    # cbar.ax.tick_params(labelsize=14)
    
def plotWfnImage2(adi_pop,wfn,timesteplist,state=0,lines=None,log=False):
    # fig, axs = plt.subplots(ncols=3,nrows=1,sharex=True,sharey=False,layout='constrained',figsize=(12, 4),dpi=120)
    fig, axs = plt.subplot_mosaic([['a.','b.','c.']],sharex=True,sharey=False,layout='constrained',figsize=(12, 4),dpi=120)
    for i, ax in enumerate(fig.axes):
        timestep = timesteplist[i]
        if log == True:
            img = ax.imshow(np.log10(np.abs(wfn[timestep,:,:,state])**2),origin="lower",vmin = np.log10(1E-9),vmax = np.log10(1E-4),extent=[-3,3,-3,3])
        else:
            img = ax.imshow(np.abs(wfn[timestep,:,:,state]**2),origin="lower",extent=[-3,3,-3,3])
        # plt.hlines(x=[115, 130, 145, 160], ymin=0, ymax=img.shape[0] - 1, colors='r')  
        
        if lines:
            for line in lines:
                plt.axhline(y=line, color='white', linestyle='--')
        ax.set_xlabel('R$_2$',fontsize=18)
        ax.set_ylabel('R$_1$',fontsize=18)
        ax.tick_params(axis='both',labelsize = 14)
        # ax.set_title(f't={timestep/10}')
        
        t1 = ax.text(1.5,-2.75,f't={int(timestep/10)}',color = 'White',fontsize=18)
        t1.set_text(f't={int(timestep/10)}')

        if state==0:
            t2 = ax.text(-2.75,-2.75,f'Ground State',color = 'White',fontsize=18)
            t2.set_text(f'Ground State')
        else:
            t2 = ax.text(-2.75,-2.75,f'Excited State',color = 'White',fontsize=18)
            t2.set_text(f'Excited State')
        
        t3 = ax.text(-2.75,2.50,f'Pop = {np.round(adi_pop[timestep,state],decimals=2)}',color = 'White',fontsize=18)
        t3.set_text(f'Pop = {np.round(np.real(adi_pop[timestep,state]),decimals=2)}')

        # cbar = plt.colorbar(img,shrink=.7)
        # cbar.set_label(label=r'log$_{10}$[$\chi$$_{'f'{state+1}''}^*$(R)'r'$\chi$$_{'f'{state+1}''}$(R)]',size=18)
    plt.suptitle('Nuclear Density',fontsize=20)
    cbar = plt.colorbar(img,shrink=1)
    # cbar.set_label(label=r'log$_{10}$[$\chi$$^*$$_{'f'{state+1}'r'(R)}$\chi$$_{'f'{state+1}''}$(R)]',size=18)
    cbar.set_label(label=r'log$_{10}$[$\chi$$_{'f'{state+1}''}^*$(R)'r'$\chi$$_{'f'{state+1}''}$(R)]',size=18)
    cbar.ax.tick_params(labelsize=14)
    # plt.suptitle('Nuclear Density',fontsize=20)

def plotCuts(wfn,timesteplist,cutloclist,state=0,xmin=-1.5,xmax=1.5):
    x = np.linspace(-3,3,256)
    fig, axs = plt.subplots(ncols=3,nrows=1,sharex=True,sharey=False,layout='constrained',figsize=(12, 4),dpi=120)
    for i, ax in enumerate(fig.axes):
        timestep = timesteplist[i]
        cutloc = cutloclist[i]
        
        formatter = ScalarFormatter(useMathText=True)
        formatter.set_scientific(True)
        formatter.set_powerlimits((-1, 1)) # Forces scientific notation
        ax.yaxis.set_major_formatter(formatter)
        ax.tick_params(labelleft=True)
        ax.plot(x,np.real(wfn[timestep,cutloc,:,state]),'-o',label=r'Re[$\chi$$_1$]',markersize=2.5)
        ax.plot(x,np.imag(wfn[timestep,cutloc,:,state]),'-o',label=r'Im[$\chi$$_1$]',markersize=2.5)
        ax.set_title(f'$t$ = {timestep/10}, $R$$_1$ = {np.round(-3+cutloc*6/256,decimals=2)}')
        ax.vlines(128,ymin=np.min(np.real(wfn[timestep,cutloc,:,state])),ymax=np.max(np.real(wfn[timestep,cutloc,:,state])),color='k',linestyles='dotted')
        ax.hlines(0,xmin=xmin,xmax=xmax,color='k',linestyles='dotted')
        ax.set_xlim(xmin,xmax)
        ax.set_xlabel('R$_2$',fontsize=18)
        ax.set_ylabel('Amplitude',fontsize=18)
        ax.tick_params(axis='both',labelsize = 14)
        ax.legend(loc=3)

        # t1 = ax.text(.75,-1.75,f't={int(timestep/10)}',color = 'Black',fontsize=18)
        # t1.set_text(f't={int(timestep/10)}')
        
    plt.suptitle('Vibronic Wavefunction Cross-Sections',fontsize=20)


def reflectionExpectationR2(psi):
    """
    psi shape: (nR1, nR2)

    Returns <R2-reflection> = <psi|R psi>/<psi|psi>.
    Uses grid indices and assumes R2 reflection corresponds to axis reversal.
    """

    psiReflected = psi[:, ::-1]

    numerator = np.sum(np.conj(psi) * psiReflected)
    denominator = np.sum(np.abs(psi)**2)

    return numerator / denominator

def reflectionExpectationR2TimeSeries(wfn, state=0):
    """
    wfn shape: (time, nR1, nR2, nState)

    Returns complex array S(t).
    """

    numTimes = wfn.shape[0]
    S = np.zeros(numTimes, dtype=complex)

    for t in range(numTimes):
        psi = wfn[t, :, :, state]
        S[t] = reflectionExpectationR2(psi)

    return S

def reflectionExpectationR2WithAxis(psi, axisIndex):
    """
    Reflection about a specified R2 axis index.

    psi shape: (nR1, nR2)
    axisIndex: index corresponding to R2=0
    """

    nR1, nR2 = psi.shape

    maxOffset = min(axisIndex, nR2 - axisIndex - 1)

    center = psi[:, axisIndex:axisIndex+1]

    lower = psi[:, axisIndex-maxOffset:axisIndex]
    upper = psi[:, axisIndex+1:axisIndex+1+maxOffset]

    reflected = np.zeros_like(psi)

    # center maps to itself
    reflected[:, axisIndex:axisIndex+1] = center

    # upper maps to reflected lower
    reflected[:, axisIndex+1:axisIndex+1+maxOffset] = lower[:, ::-1]

    # lower maps to reflected upper
    reflected[:, axisIndex-maxOffset:axisIndex] = upper[:, ::-1]

    numerator = np.sum(np.conj(psi) * reflected)
    denominator = np.sum(np.abs(psi)**2)

    return numerator / denominator

def reflectionExpectationR2WithAxisTimeSeries(wfn, state=0, axisIndex=128):
    numTimes = wfn.shape[0]
    S = np.zeros(numTimes, dtype=complex)

    for t in range(numTimes):
        psi = wfn[t, :, :, state]
        S[t] = reflectionExpectationR2WithAxis(psi, axisIndex)

    return S