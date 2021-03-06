# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # frontier to implement DFS is stack
    fringe=util.Stack()
    state=problem.getStartState()
    #list to keep track of visited states
    visited_nodes=[]
    #state=problem.getStartState()
    fringe.push((state,[])) #push starting state and empty list into fringe
    while 1:
        current_state,actions=fringe.pop()
        if(problem.isGoalState(current_state)):
            return actions
            break
        if(current_state not in visited_nodes):
            visited_nodes.append(current_state)  
            successor=problem.getSuccessors(current_state)    
            temp_action=[] # list stores actions to reach child node from given state to reach child nodes
            for s in successor:  
                    temp_action=actions[0:] #append temp_actions with actions 
                    temp_action.append(s[1]) # append with new_actions from sucessor function
                    fringe.push((s[0],temp_action)) #push new_state and temp action into stack
   
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #frontier to implement BFS is Queue
    frontier=util.Queue()
    state=problem.getStartState() # state tupple will store starting state from get.StartState()
    visited_nodes=[] #visited_nodes=[] 
    frontier.push((state,[]))
    while not 0:
        current_state,actions=frontier.pop()
        if(problem.isGoalState(current_state)):
            return actions
            break
        if(current_state not in visited_nodes):
            visited_nodes.append(current_state)  
            successor=problem.getSuccessors(current_state)    
            temp_action=[]
            for s in successor:
                new_state=s[0]
                new_actions=s[1]
                temp_action=actions[0:]
                temp_action.append(new_actions)
                frontier.push((new_state,temp_action))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #start_state=()
    start_state=problem.getStartState()
    visited_nodes=[]
    fringe=util.PriorityQueue()
    fringe.push((start_state,[],0),0) #initial cost is 0 therefore directly pass cost as 0
    while not 0:
       
        current_state,actions,cost=fringe.pop()
        # if current state is goal state then return the solution(actions)
        if(problem.isGoalState(current_state)):
            return actions
            break
        if(current_state not in visited_nodes):#if that state is not goal state then if it is not in visited nodes then append in list
            visited_nodes.append(current_state)
            children=problem.getSuccessors(current_state) 
            moves=[]
            for i in children:
               moves=actions[0:]
               new_state=i[0]
               new_actions=i[1]
               new_cost=i[2]
               moves.append(new_actions)
               calc_cost=cost + new_cost #calculated cost
               fringe.push((new_state,moves,calc_cost),calc_cost)   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #start_state=()
    start_state=problem.getStartState()
    visited_nodes=[]
    #actions=[]
    #cost=0
    fringe=util.PriorityQueue()
    fringe.push((start_state,[],0,0),0) #pass start_state,actions(initially no actions performed,initially goal_cost is 0,heuristic distance is 0 )
    while 1:
       # current_path=fringe.pop()
        current_state,actions,goal_cost,heuristic_dist=fringe.pop()
        cost=goal_cost - heuristic_dist
        if(problem.isGoalState(current_state)):
            return actions
            break
        if(current_state not in visited_nodes):
            visited_nodes.append(current_state)
            children=problem.getSuccessors(current_state) 
            #moves=[]
            for i in children:
               moves=actions[0:]
               moves.append(i[1])
               calc_cost=cost + i[2]
               heuristic_cost=calc_cost + heuristic(i[0],problem)
               fringe.push((i[0],moves,heuristic_cost,heuristic(i[0],problem)),heuristic_cost)  
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
