from cmath import sqrt
from eva import EvaProgram, Input, Output, evaluate
from eva.ckks import CKKSCompiler
from eva.seal import generate_keys
from eva.metric import valuation_mse
import timeit
import networkx as nx
import sys
import matplotlib.pyplot as plt
import math
from random import random, randrange

# Using networkx, generate a random graph
# You can change the way you generate the graph
def generateGraph(n, k, p):
    ws = nx.balanced_tree(2, 2)
    nx.draw(ws, with_labels=True)
    plt.show()
    plt.savefig('graph_new3.png')
    return ws

# If there is an edge between two vertices its weight is 1 otherwise it is zero
# You can change the weight assignment as required
# Two dimensional adjacency matrix is represented as a vector
# Assume there are n vertices
# (i,j)th element of the adjacency matrix corresponds to (i*n + j)th element in the vector representations
def serializeGraphZeroOne(GG,vec_size):
    n = GG.size() + 1
    graphdict = {}
    vertexweight = []
    g = []
    edge = []
    res = [9999999999]

    for row in range(n):
        for column in range(n):
            if GG.has_edge(row, column) or row==column: # I assumed the vertices are connected to themselves
                weight = 1
                if(row != column) & check(edge, row, column):
                    edge.append([row, column])
            else:
                weight = 0 
            g.append( weight  )  
            
            key = str(row)+'-'+str(column)
            graphdict[key] = [weight] # EVA requires str:listoffloat

            
    for j in range(n):
        vertex_weight = randrange(1, 10)
        #g.append(vertex_weight)
        vertexweight.append(vertex_weight)

    for i in range(vec_size - n*n): 
        g.append(0.0)
    
    for i in range(vec_size - n): 
        vertexweight.append(0.0)

    for i in range(vec_size - 1): 
        res.append(0.0)
    
    for i in range(vec_size - len(edge)):
        edge.append(0.0)

    printGraph(g,n)
    print('\n')
    printVertexWeights(vertexweight,n)
    return g, graphdict, vertexweight, res

# To display the generated graph
def printGraph(graph,n):
    for row in range(n):
        for column in range(n):
            print("{:.5f}".format(graph[row*n+column]), end = '\t')
        print() 

def printVertexWeights(vertexweight,n):
    for k in range(n):
        print("{:.5f}".format(vertexweight[k]), end = '\t')
    print() 

def check(edge,row,column):
    if len(edge) == 0:
        return True
    else:
        mylist = [column, row]
        result =  mylist in edge
        if result:
            return False
        else:
            return True

        

# Eva requires special input, this function prepares the eva input
# Eva will then encrypt them
def prepareInput(n, m):
    input = {}
    GG = generateGraph(n,3,0.5)
    graph, graphdict, vertexweight, res = serializeGraphZeroOne(GG,m)
    totalSum = 0

    #input['Graph'] = graph
    input['Weight'] = vertexweight
    input['Res'] = res
    return input


def dfs(u, parent, totalSum, subtree, res, N, res2): 

    edges = [[0,1], [0,2], [1,3], [1,4], [2,5], [2,6]]
    vec_size = 4096

    edge = [[] for i in range(N)] 
    for i in range(N - 1): 
        edge[edges[i][0]].append(edges[i][1]) 
        edge[edges[i][1]].append(edges[i][0])  

    identity = []
    for i in range(N):
        identity2 = []
        for j in range(N):
            if(i == j):
                identity2.append(1)
                continue
            identity2.append(0)
        identity.append(identity2)

    for i in range(N): 
        for j in range(vec_size - N):
            identity[i].append(0.0)

    rev_identity = []
    for i in range(N):
        rev_identity2 = []
        for j in range(N):
            if(i == j):
                rev_identity2.append(0.0)
                continue
            rev_identity2.append(1.0)
        rev_identity.append(rev_identity2)

    for i in range(N): 
        for j in range(vec_size - N):
            rev_identity[i].append(0.0)

    Mul = identity[u] * subtree
    Sum = getSum(Mul)

    # loop for all neighbors except parent 
    # and aggregate Sum over all subtrees 

    for i in range(len(edge[u])): 
        v = edge[u][i] 
        if (v != parent): 
            dfs(v, u, totalSum, subtree, res, N, res2) 
            Mul = identity[v] * subtree
            Sum += getSum(Mul)

    # store Sum in current node's 
    # subtree index 

    Mul = subtree * rev_identity[u]
    temp = identity[u] * Sum
    subtree = Mul + temp

    #subtree[u] = Sum
  
    # at one side subtree Sum is 'Sum' and 
    # other side subtree Sum is 'totalSum - Sum' 
    # so their difference will be totalSum - 2*Sum, 
    # by which we'll update res 

    # if (u != 0 and abs(totalSum - 2 * Sum) < res[0]): 
    #     res[0] = abs(totalSum - 2 * Sum) 

    comp = totalSum - 2 * Sum

    if(u != 0):
        if comp:
            if (res-comp): 
                res2 = res*rev_identity[0]
                res2 = res + comp
    

def getSum(vect):
 
    vect2 = vect
    i = 1
    while i < vect2.program.vec_size:
        y = vect2 << i
        vect2 = vect2 + y
        i <<= 1

    return vect2

# This is the dummy analytic service
# You will implement this service based on your selected algorithm
# you can other parameters using global variables !!! do not change the signature of this function 
def graphanalticprogram(weights):
    vec_size = 4096
    weights2 = weights
    i = 1
    while i < weights2.program.vec_size:
        y = weights2 << i
        weights2 = weights2 + y
        i <<= 1

    totalSum = weights2

    ## Check what kind of operators are there in EVA, this is left shift
    # Note that you cannot compute everything using EVA/CKKS
    # For instance, comparison is not possible
    # You can add, subtract, multiply, negate, shift right/left
    # You will have to implement an interface with the trusted entity for comparison (send back the encrypted values, push the trusted entity to compare and get the comparison output)
    return totalSum
    
# Do not change this 
# the parameter n can be passed in the call from simulate function
class EvaProgramDriver(EvaProgram):
    def __init__(self, name, vec_size=4096, n=4):
        self.n = n
        super().__init__(name, vec_size)

    def __enter__(self):
        super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

# Repeat the experiments and show averages with confidence intervals
# You can modify the input parameters
# n is the number of nodes in your graph
# If you require additional parameters, add them

def simulate(n):
    global res2
    res2 = []
    # res = [999999999999]
    global positive_infinity
    positive_infinity = math.inf
    global negative_infinity
    negative_infinity = -math.inf

    m = 4096
    print("Will start simulation forr ", n)
    config = {}
    config['warn_vec_size'] = 'false'
    config['lazy_relinearize'] = 'true'
    config['rescaler'] = 'always'
    config['balance_reductions'] = 'true'
    inputs = prepareInput(n, m)

    graphanaltic = EvaProgramDriver("graphanaltic", vec_size=m,n=n)
    with graphanaltic:
        res = Input('Res')
        #Output('Res', res)
        weights = Input('Weight')
        Output('Weights', weights)
        totalSum= graphanalticprogram(weights) 
        Output('TotalSum', totalSum)
        #Output('Vect', vect)
        dfs(0, -1, totalSum, weights, res, n, res2)
        #Output('Result', result)
        Output('Result', res)
        #Output('Comp3', res2)
        #Output('Sum', res3)
        
    
    prog = graphanaltic
    prog.set_output_ranges(30)
    prog.set_input_scales(30)

    start = timeit.default_timer()
    compiler = CKKSCompiler(config=config)
    compiled_multfunc, params, signature = compiler.compile(prog)
    compiletime = (timeit.default_timer() - start) * 1000.0 #ms

    start = timeit.default_timer()
    public_ctx, secret_ctx = generate_keys(params)
    keygenerationtime = (timeit.default_timer() - start) * 1000.0 #ms
    
    start = timeit.default_timer()
    encInputs = public_ctx.encrypt(inputs, signature)
    encryptiontime = (timeit.default_timer() - start) * 1000.0 #ms

    start = timeit.default_timer()
    encOutputs = public_ctx.execute(compiled_multfunc, encInputs)
    executiontime = (timeit.default_timer() - start) * 1000.0 #ms

    start = timeit.default_timer()
    outputs = secret_ctx.decrypt(encOutputs, signature)
    decryptiontime = (timeit.default_timer() - start) * 1000.0 #ms

    start = timeit.default_timer()
    reference = evaluate(compiled_multfunc, inputs)
    referenceexecutiontime = (timeit.default_timer() - start) * 1000.0 #ms

    
    # Change this if you want to output something or comment out the two lines below
    for key in outputs:
        print('hello')
        print(key, float(outputs[key][0]), float(outputs[key][1]), float(reference[key][0]), float(reference[key][1]), float(reference[key][2]))

    mse = valuation_mse(outputs, reference) # since CKKS does approximate computations, this is an important measure that depicts the amount of error

    return compiletime, keygenerationtime, encryptiontime, executiontime, decryptiontime, referenceexecutiontime, mse


if __name__ == "__main__":
    simcnt = 1 #The number of simulation runs, set it to 3 during development otherwise you will wait for a long time
    # For benchmarking you must set it to a large number, e.g., 100
    #Note that file is opened in append mode, previous results will be kept in the file

    #resultfile = open("results.csv", "a")  # Measurement results are collated in this file for you to plot later on
    #resultfile.write("NodeCount,PathLength,SimCnt,CompileTime,KeyGenerationTime,EncryptionTime,ExecutionTime,DecryptionTime,ReferenceExecutionTime,Mse\n")
    #resultfile.close()

    resultfile2 = open("results2.csv", "a")  # Measurement results are collated in this file for you to plot later on
    resultfile2.write("NodeCount,PathLength,SimCnt,CompileTime,KeyGenerationTime,EncryptionTime,ExecutionTime,DecryptionTime,ReferenceExecutionTime,Mse\n")
    resultfile2.close()
    
    print("Simulation campaing started:")
    for nc in range(7,9,2): # Node counts for experimenting various graph sizes 36, 64,4 
        n = nc
        resultfile2 = open("results2.csv", "a") 
        
        for i in range(simcnt):
            compiletime, keygenerationtime, encryptiontime, executiontime, decryptiontime, referenceexecutiontime, mse = simulate(n)
            res = str(n) + "," + str(i) + "," + str(compiletime) + "," + str(keygenerationtime) + "," +  str(encryptiontime) + "," +  str(executiontime) + "," +  str(decryptiontime) + "," +  str(referenceexecutiontime) + "," +  str(mse) + "\n"
            print(res)
            resultfile2.write(res)
        resultfile2.close()




        
   
        