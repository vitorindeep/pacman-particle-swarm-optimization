import pacman as pac
import sys

if __name__ == '__main__':

    """
    Used to start a game, with pacman module
    """
    base = ["-p", "PacmanQAgent", "-x", "2000", "-n", "2010", "-l", "smallGrid", "-a"]
    base.append("epsilon=0.1,alpha=0.3,gamma=0.7")

    args = pac.readCommand( base ) # Get game components based on input    
    averageScore = pac.runGames( **args )

    print(averageScore)

    pass

#--- EXAMPLE ------------------------------------------------------------------+
# python pso.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid -a epsilon=0.1,alpha=0.3,gamma=0.7