"""
Simple mtg ploting functionality for the default root format 
"""

def plot(g):
    """
    Plot mtg `g` using matplotlib
    
    `g` should have the default root format
    """
    from matplotlib import pyplot as plt
    
    x = g.property('x')
    y = g.property('y')
    
    color_list = 'rgbyck'
    color_num  = len(color_list)
    for plant in g.components(g.root):
        for i,axe in enumerate(g.components(plant)):
            color = color_list[i%color_num]
            for segment in g.components(axe):
                parent = g.parent(segment)
                if parent is None: continue
                plt.plot([x[parent],x[segment]], [y[parent],y[segment]], color)
    
    
    
