"""
Test plotting with matplotlib
"""

def test_simple_mtg():
    """ create a simple mtg tree 
    
    The mtg has 3 scale:
      - 0: the scene
      - 1: the plant
      - 2: the root axes
      - 3: the root segments
      
    It contains 2 plants, eac with 1 primary axe and 2 secondary
    """
    from openalea.mtg import MTG
    
    def add_plant(g,x,y):
        p1 = g.add_component(g.root)       # plant    - scale 1
        a1 = g.add_component(p1)           # axe 1    - scale 2
        n0 = g.add_component(a1, x=x, y=y) # 1st node - scale 3
        ni = g.add_child(n0, x=x, y=y-1)
        ni = g.add_child(ni, x=x, y=y-2)
        b1 = ni
        ni = g.add_child(ni, x=x, y=y-3)
        ni = g.add_child(ni, x=x, y=y-4)
        b2 = ni
        ni = g.add_child(ni, x=x, y=y-5)
        ni = g.add_child(ni, x=x, y=y-6)
        ni = g.add_child(ni, x=x, y=y-6)
        
        ni = g.add_child_and_complex(b1, x=x-1, y=y-3)[0] # axe 2
        ni = g.add_child(ni, x=x-2, y=y-4)
        ni = g.add_child_and_complex(b2, x=x+1, y=y-5)[0] # axe 3
        ni = g.add_child(ni, x=x+2, y=y-6)

    g = MTG()
    add_plant(g, 0,0)
    add_plant(g,10,0)
    
    return g
    
    
def test_plot():
    g = test_simple_mtg()
    
    from matplotlib import pyplot as plt
    from matplotlib import backends
    from rhizobabel import plot
    cur_backend = backends.backend
    
    try:
        plt.switch_backend('Agg') # offline backend
        plot.plot(g)
    finally:
        plt.switch_backend(cur_backend)