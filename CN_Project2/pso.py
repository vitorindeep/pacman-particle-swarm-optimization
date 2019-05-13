import pacman as pac

import sys

#------------------------------------------------------------------------------+
#
#	Nathan A. Rooy
#	Simple Particle Swarm Optimization (PSO) with Python
#	Last update: 2018-JAN-26
#	Python 3.6
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import random
import math

#--- COST FUNCTION ------------------------------------------------------------+

# we're just aiming for the highest average score, so no special function needed

#--- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.score_best_i=-1        # best score individual
        self.score_i=-1             # score individual

        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(random.random())         # generates numbers betweem 0 and 1

    # evaluate current fitness
    def evaluate(self):
        #
        # TO DO:
        # call pac.runGames and run the game with this particle's parameters
        #
        # base = ["-p", "PacmanQAgent", "-x", "2000", "-n", "2010", "-l", "smallGrid", "-a"]
        # base.append("epsilon=0.1,alpha=0.3,gamma=0.7")

        # args = pac.readCommand( base ) # Get game components based on input    
        # averageScore = pac.runGames( **args )

        self.score_i=averageScore      # save the averageScore this iteration had

        # check to see if the current position is an individual best
        if self.score_i<self.score_best_i or self.score_best_i==-1:
            self.pos_best_i=self.position_i.copy()
            self.score_best_i=self.score_i
                    
    # update new particle velocity
    def update_velocity(self,pos_best_g):
        w=0.5       # constant inertia weight (how much to weigh the previous velocity)
        c1=1        # cognative constant
        c2=2        # social constant
        
        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()
            
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            
            # adjust maximum position if necessary
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i]<bounds[i][0]:
                self.position_i[i]=bounds[i][0]
        
class PSO():
    def __init__(self, numDims, bounds, num_particles, maxiter, verbose=False):
        global num_dimensions

        num_dimensions=numDims
        score_best_g=-1                 # best score for group
        pos_best_g=[]                   # best position for group

        # establish the swarm
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle())

        # begin optimization loop
        i=0
        while i<maxiter:
            if verbose: print(f'iter: {i:>4d}, best solution: {score_best_g:10.6f}')
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,num_particles):
                # here we ask the particle to run his values in the game
                swarm[j].evaluate()

                # determine if current particle is the best (globally)
                if swarm[j].score_i<score_best_g or score_best_g==-1:
                    pos_best_g=list(swarm[j].position_i)
                    score_best_g=float(swarm[j].score_i)
            
            # cycle through swarm and update velocities and position
            for j in range(0,num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        print('\nFINAL SOLUTION:')
        print(f'   > {pos_best_g}')
        print(f'   > {score_best_g}\n')

if __name__ == "__PSO__":
    main()

#--- END ----------------------------------------------------------------------+

if __name__ == '__main__':

    numDims = 3  # number of paremeters to optimize
    bounds=[(0,1),(0,1),(0,1)]  # input bounds [(epsilon_min,epsilon_max),(alpha_min,alpha_max),(gamma_min,gamma_max)]
    PSO(numDims, bounds, num_particles=15, maxiter=30, verbose=True)

    """
    Used to start a game, with pacman module
    """
    #args = pac.readCommand( sys.argv[1:] ) # Get game components based on input
    #averageScore = pac.runGames( **args )

    #print(averageScore)

    pass

#--- EXAMPLE ------------------------------------------------------------------+
# python pso.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid -a epsilon=0.1,alpha=0.3,gamma=0.7