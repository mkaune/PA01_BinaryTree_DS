"""nodeRLR = PA01 . Node ( 4 ,None,None)
4 nodeRL = PA01 . Node ( 3 ,None, nodeRLR )
5 nodeRR = PA01 . Node ( 7 ,None,None)
6 nodeL = PA01 . Node ( 5 ,None,None)
7 nodeR = PA01 . Node ( 2 , nodeRL , nodeRR )
8 bin 1 = PA01 . Node ( 1 , nodeL , nodeR )

node1=[4,[], []] ist Blatt!
node2=[3, [], [4, [], []]]
node3= ...

"""


"""0 Key: 0, leftChild: *, rightChild: None
1 leftChild:  Key: 1, leftChild: None,rightChild: None,"""



class Node:
    def __init__(self, key, leftChild, rightChild):
        self.key= key
        #self.Baum={"key": key, "leftChild": None, "rightChild": None}

        if leftChild==None:
            self.leftChild=None
        else:
            self.leftChild=leftChild.__dict__
            #self.Baum["leftChild"]=leftChild.__dict__
        if rightChild==None:
            self.rightChild=None
        else:
            self.rightChild=rightChild.__dict__
            #self.Baum["rightChild"]=rightChild.__dict__
        
    #pass
    #build this tree backwards
    def keys(self):
        global count_height
        global knoten
        global leaves
        global liste_heights
        global dos_caminos
        lefttree=self.leftChild
        righttree=self.rightChild
        key_copy=self.key
        baum={"key": key_copy, "leftChild": lefttree, "rightChild": righttree}
        
        knoten=[]
        leaves=[]
        count_height=0
        liste_heights=[0]
        dos_caminos=[0]
        knoten_result=self.recursive_lookup()
        
        self.leftChild=baum["leftChild"]
        self.rightChild=baum["rightChild"]
        self.key=baum["key"]
        
        return knoten
    
    
    def recursive_lookup(self,):

        global count_height
        global knoten
        global leaves
        global liste_heights
        global dos_caminos
        lefttree=self.leftChild
        righttree=self.rightChild
        key_copy=self.key
        d={"key": key_copy, "leftChild": lefttree, "rightChild": righttree}
    

        
        knoten.append(d['key'])
        
        #if k in d: return d
    
        if d['leftChild']!=None or d['rightChild']!= None:
        
            #count_height+=1
            #count: values of keys
            count_height+=1
            if d['rightChild']!= None and d['leftChild']!=None:
                dos_caminos.append(count_height)
                #print(dos_caminos)
            #count_height+=1
            
            if d['leftChild']!=None:
                #count_height+=1
                self.leftChild=d['leftChild']['leftChild']
                self.rightChild=d['leftChild']['rightChild']
                self.key=d['leftChild']['key']
                
                a=self.recursive_lookup()
               # print(count_height)
                
            if d['rightChild']!= None:
                #count_height+=1
                self.leftChild=d['rightChild']['leftChild']
                self.rightChild=d['rightChild']['rightChild']
                self.key=d['rightChild']['key']
                
                a=self.recursive_lookup()
                #print(count_height)
                
            
                
            return a
        else:
            liste_heights.append(count_height)
            leaves.append(d['key'])
            #print(liste_heights
            count_height=dos_caminos.pop()
            #print(str(count_height)+ " cuenta")
            #return max(liste_heights)
            return knoten
            #return leaves   
        

        """{'key': 2, 'leftChild': {'key': 3, 'leftChild': None, 'rightChild':
        {'key': 4, 'leftChild': None, 'rightChild': None}},
         'rightChild': {'key': 7, 'leftChild': None, 'rightChild': None}}"""
        
        #pass
    def height(self):
        global count_height
        global knoten
        global leaves
        global liste_heights
        global dos_caminos
        
        lefttree=self.leftChild
        righttree=self.rightChild
        key_copy=self.key
        baum={"key": key_copy, "leftChild": lefttree, "rightChild": righttree}
        
        knoten=[]
        leaves=[]
        count_height=0
        liste_heights=[0]
        dos_caminos=[0]
        
        knoten_result=self.recursive_lookup()

        self.leftChild=baum["leftChild"]
        self.rightChild=baum["rightChild"]
        self.key=baum["key"]
        
        
        return (max(liste_heights))
        """example: bin1.height(): 3"""
        
    def leaves(self):
        global count_height
        global knoten
        global leaves
        global liste_heights
        global dos_caminos
        
        baum={"key": self.key, "leftChild": self.leftChild, "rightChild": self.rightChild}
        
        knoten=[]
        leaves=[]
        count_height= 0
        liste_heights=[0]
        dos_caminos=[0]
        
        knoten_result=self.recursive_lookup()

        self.leftChild=baum["leftChild"]
        self.rightChild=baum["rightChild"]
        self.key=baum["key"]

        return leaves
    
        #structure=set()
        #example for structre: nodeRLR={key: 4, leftchild: None, rightNode: None}
        
    def __str__(self):
         return " Key: {}, leftChild: {}, rightChild: {}".format(self.key,self.leftChild,self.rightChild)


"""nodeRLR = Node( 4 ,None,None)
nodeRL = Node ( 3 ,None, nodeRLR )
nodeRR = Node ( 7 ,None,None)
nodeL = Node ( 5 ,None,None)
nodeR = Node ( 2 , nodeRL , nodeRR )
bin1 = Node ( 1 , nodeL , nodeR )"""

"""nodeLL = Node(7,None,None)
nodeL = Node(5,nodeLL,None)

nodeRL = Node(3,None,None)

nodeR = Node(2,nodeRL,None)

bin2 = Node(0 ,nodeL ,nodeR)"""


#print(bin1.__dict__)
##print(bin2.

""" Key: 1, leftChild:  Key: 5, leftChild: None,
rightChild: None, rightChild:  Key: 2, leftChild:
Key: 3, leftChild: None, rightChild:  Key: 4, leftChild: None,
rightChild: None, rightChild:  Key: 7, leftChild: None, rightChild: None"""

#print("NodeRl: " + str(nodeRL))

"""NodeRl:  Key: 3, leftChild: None, rightChild:
Key: 4, leftChild: None, rightChild: None"""

""" Key: 1, leftChild: {'key': 5, 'leftChild': None, 'rightChild': None}, rightChild:
{'key': 2, 'leftChild': {'key': 3, 'leftChild': None, 'rightChild':
{'key': 4, 'leftChild': None, 'rightChild': None}}, 'rightChild': {'key': 7, 'leftChild': None, 'rightChild': None}} """

"""T8nodeLL = Node(4,None,None)
T8nodeLR = Node(5,None,None)
T8nodeRL = Node(6,None,None)
T8nodeRR = Node(7,None,None)
T8nodeL = Node(2, T8nodeLL, T8nodeLR) 
T8nodeR = Node(3, T8nodeRL, T8nodeRR)
T8r = Node(1, T8nodeL, T8nodeR)"""
#print(T8r.__dict__)
