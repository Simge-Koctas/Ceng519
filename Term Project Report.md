Data privacy has started to become a significant topic in computer
networks due to the cyber-attacks that causes great losses to the
companies and also to the individuals. Encryption is one of the robust
security techniques to avert cyber-attacks. Moreover, homomorphic
encryption provides more capabilities to traditional encryption
techniques. Arithmetic operations can be performed on the encrypted
data, this can eliminate the need of decryption in every data
modification. In this paper, a solution to the delete edge to minimize
subtree sum difference problem is given using the Microsoft's EVA
homomorphic encryption library. In the problem, in order to find the
edge that divides the tree into two subtrees need to be found. By
finding such an edge, the two formed subtree's weights' summation need
to be close enough to minimize the difference.

# Introduction

The rapid enhancement of computer networks help us to stay connected to
the digital world all the time and from anywhere in the world. It is
said that approximately 18 billion devices are connected to the Internet
by 2022  [@Collela2021] and it is expected to become 30.9 billion
connected devices by 2025  [@Statista2021]. However, this opportunity of
being connected to the cyberspace world also makes us vulnerable to the
cyber-attacks. According to Cyber security Ventures, cyber-attacks
caused loss of 6 trillion dollars and it is projected to become 10.5
trillion dollars by the end of 2025  [@Pitchkites2022]. In order for a
safe information exchange, we need proper solutions.

Encryption is one of the most powerful security techniques for securing
data. By converting plaintext data into an unreadable form of text,
encryption can provide privacy of the data  [@Lakhtaria2011]. This is
also because when the data is encrypted, it can only be decrypted when
the other party has the appropriate key. If the opponent does not have
the required key, it cannot decrypt the contents of the encrypted data
and therefore cannot reveal the hidden information  [@Wang2016].

Traditional encryption techniques maintain security by destroying the
relationship between the plaintext and the ciphertext. This is because,
if the correlation between the plaintext and ciphertext is known or
predicted by malicious people, they can both observe and crack the
ciphertext and violate the privacy of the data. In order to present data
privacy without exposing the relationship between the plaintext and the
ciphertext and if we need to perform arithmetic operations on an
encrypted data, we need to decrypt the ciphertext, perform relevant
operations and then send the newly formed data to the other party which
can take time, can be costly and prone to security problems.
 [@Lakhtaria2011].

# Background and Related Work

## Background

Homomorphic encryption enables implementing arithmetic operations on
encrypted data through preserving the data privacy and without the need
of decrypting the data contents. Microsoft SEAL is an open-source
homomorphic encryption technology that maintains encryption libraries.
On the other hand, PyEVA is a Python embedded DSL in order to implement
EVA programs.  [@Microsoft2022].

With respect to give an encrypted parameter to the EVA program and print
the results, the following example program can be used in Figure 1:

!\[Determining Inputs in EVA\](./images/eva1.png)

In order to compile the program, we are using the 'compile' method and
generating the compiled program, parameters and the signature which is
shown in Figure 2.

!\[Compile in EVA\](./images/eva3.png)

Generating the encryption and decryption keys are computed by the
'encrypt' method that returns the encrypted inputs. Then, the encrypted
inputs can be executed according to the compiled program with 'execute'
command which are shown in Figures 3, 4 and 5.

!\[Key Generation in EVA\](./images/eva4.png)

!\[Encrypt in EVA\](./images/eva5.png)

!\[Execute in EVA\](./images/eva6.png)

The decryption can be done by using the 'decrypt' function on the
encrypted inputs. 'Evaluate' method is also used to compare the
unencrypted computation on unencrypted data. Figures 6 and 7 shows the
usage of 'decrypt' and 'evaluate' methods.

!\[Decrypt in EVA\](./images/eva7.png)

![Evaluate in EVA  [@Microsoft2022]](eva7)

!\[Execute in EVA\](./images/eva8.png)

## Related Work

!\[An Undirected Tree\](./images/extree.png)

In order to find a solution to delete edge to minimize subtree sum
difference, firstly, we need to examine the problem. In the Figure 8,
there are 6 nodes and each of them are associated with a weight. For
example, the node 0 is associated with weight 4 and node 1 is associated
with weight 2. In order to delete the edge that minimizes the subtree
sum difference, we can traverse through the graph and calculate every
subtree weights' summation and then compare it with the remaining nodes'
weights' summation that also form another subtree in the graph. For
instance, in the Figure 8, if the edge between 0 -- 3 is selected to be
deleted, we need to compare the weights' summation of two subtrees,
which are the subtree starting with the node 3 that has one child which
is the node 6, and the other subtree which includes the nodes 0, 1, 2, 4
and 5. The weights' summation of first subtree becomes 8 because node 3
is associated with weight 6 and node 6 is associated with weight 2. The
remaining subtree weights' summation can be found by extracting the
first subtree weights' summation from the total sum of the overall tree.
The total sum is 23 and the other subtree weights' difference becomes 23
-- 8 = 15. Now, if we compare the two subtreee weights' difference, 15
-- 8 which becomes 7. In order to find the minimum subtree sum
difference, we need to traverse all the subtrees in order to find the
minimum subtree weights' summation difference. In the example, if the
edge between nodes 0 -- 2 is deleted, the subtree weights' summation
difference becomes 5 (14 - 9) and it is the smallest difference that we
can calculate in this tree.

In order for a detailed solution for deleting edge to minimize subtree
sum difference problem, a solution from Trivedi can be analyzed
 [@Trivedi2021]. The corresponding algorithm can be found in Figure 9
and 10 below. In his solution, firstly, a 'vertex' list is created in
order to define the weights of the vertexes of the graph. The 2D 'edges'
list is formed in order to determine the edges that the nodes have on
the graph. The 'edges' list for the graph in Figure 8 becomes:

edges = \[\[0, 1\], \[0, 2\], \[0, 3\], \[2, 4\], \[2, 5\], \[3, 6\]\]

The 'getMinSubtreeSumDifference' method firstly creates another list
called 'subtree' and make a copy of the 'vertex' list. Also, the total
sum is calculated by the summation of the weights in the 'vertex' list.
The 'edge' list on the other hand simplifies the 'edges' list by merging
the edge information. According to the Figure 8, the 'edge' list can be
shown above:

edge = \[\[1, 2, 3\], \[0\], \[0, 4, 5\], \[0, 6\], \[2\], \[2\],
\[3\]\]

The 'edge' list includes the edges information based on the 'edges'
list. To illustrate, node 0 has edges to the nodes 1, 2, 3 and it is
written as the first element of the 'edge' list. Secondly, because node
1 only has one edge to the node 0, the 'edge' lists' second element only
contains 0.

After creating the vertex and edge lists, the depth first search method
is called, starting from the node 0. Because the node 0 does not have
any parent, the second argument becomes -1. The 'res' variable is going
to be used to store the minimum subtree sum difference.

In the depth first search method, firstly, the starting nodes' weight is
stored in the 'Sum' variable. Later, 'Sum' variable is going to be used
to store each subtrees' weights' summation. Inside the for loop, the
first child node of the starting node is found by using the 'edge' list.
If the child is not the node that initiates the depth first search
(dfs), the dfs method is called by changing the starting and parent
nodes in order to traverse deeply in the tree. In order to perform dfs,
searching needs to continue until the leaf nodes are accessed. When a
leaf node is found, the 'subtree' list stores the current leaf node's
weight in the corresponding index. Then, the summation is compared
between the previous summation results. If the current summation is
smaller than the previous value of 'res' variable, the 'res' variable is
updated. After the dfs method returns from one leaf node, the other
child nodes of the parent is continued to be called on the dfs. When all
the leaf nodes of a node are accessed, the dfs method returns and
updates the 'Sum' variable in order to store the weights' of the leaf
nodes and the weight of the current node that forms a subtree. The
program continues to call the dfs method from the parent nodes' other
child nodes.

!\[Get Minimum Subtree Sum Difference\](./images/dfs2.png)

!\[Depth First Search\](./images/dfs1.png)

# Main Contributions

In order to preserve privacy when finding the edge that minimizes the
subtree sum difference, we can combine Microsoft EVA library with the
solution from Trivedi that is explained in the previous section.
However, due to EVA library having limitations on the operations that
can be done on encrypted data, we need to modify the given solution in
the previous section in place of conforming with Microsoft EVA. EVA
accepts input variables as vectors and only permits vector arithmetic
such as summation, extraction, multiplication, left and right shifting.
Other operations such as division, comparison or absolute value are not
permitted.

## Creating a Tree

In the implementation, the balanced tree method from the networkx
library is used to form a tree by determining the number of child nodes
and the height of the tree. The edges that are formed between the nodes
in the networkx's balanced tree have a predefined structure. Starting
from the node 0, the nodes that are going to become node 0's child nodes
become the nodes that come in order based on the number of child nodes.
For instance, if there are 7 nodes, each having 2 child nodes in a graph
of height 2, the edges list becomes:

edges = \[\[0, 1\], \[0, 2\], \[1, 3\], \[1, 4\], \[2, 5\], \[2, 6\]\]

## Determining Inputs

We need to formalize the input variables that are going to become inputs
to the EVA program. Moreover, EVA requires large input sizes
 [@Microsoft2022]. For this purpose, 4096 bytes are selected as the
vector size. In order to determine weights of the vertexes, a list that
randomly generates weights between 1 to 50 is created according to the
number of the nodes in the graph. Because the input size needs to be
4096 bytes, we need padding values. After padded the 'weights' list, we
need to give an input name to the 'weights' list in order for the EVA
program to encrypt the 'weights' list and can be used as in input to our
subtree sum difference method. Because the edges in the networkx's
balanced tree has a predefined structure, we can calculate the 'edges'
list rather than writing all the edges of nodes like in the Trivedi's
solution. The algorithm to create 'edge' list is given in Figure 11.

!\[Algorithm for Creating the Edges List\](./images/edges.png)

## Finding the Total Sum of the Graph

The 'weights' list which is encrypted become an input to the
'graphanalticprogram' which calculates the total sum of the graph. In
order to calculate the total sum by using the encrypted 'weights' list,
the algorithm in Figure 12 is used.

!\[Algorithm for Finding the Total Sum of a Tree\](./images/sum.png)

The algorithm calculates the total sum by left shifting the elements of
the vector so that, by adding the elements of the shifted and un-shifted
versions of the vector, at some point, we are able to add all the
elements of the vector. In the end of the iteration, the 'Vect2' vector
contains the total sum in each of its index. For example, if the total
sum of a graph is 23, then all the indexes of the total sum vector
contain 23.

## Depth First Search

After finding the total sum of the graph by using the
'graphanalticprogram', now we need to call dfs function to find the
minimum subtree sum difference. Dfs is called with the parameters (0,
-1, totalSum, weights, edges, N). 0 is the starting node of the dfs and
because it does not have a parent, -1 is given. 'totalSum' is calculated
using the 'graphanalticprogram'. Both 'weights' and 'totalSum' are
encrypted inputs to the dfs function. Inside dfs, firstly, we calculate
the 'edge' vector using the values of 'edges' list. Then, we need to
perform arithmetic operations on 'totalSum' and 'weights' vectors. For
this purpose, supporting identity and reverse identity vectors are
created. Identity vectors are vectors that contain only one element that
is 1 and the remaining elements become 0s. For example, identity\[0\]
contains 1 in its first index and the other remaining elements become 0,
identity\[1\] contains 1 in its second index position and the rest of
the elements become 0. Reverse identity vectors contain only one element
that is 0 and the remaining elements become 1s. For instance,
rev-identity\[0\] contains 0 in its first index position and the other
remaining elements become 1.

Furthermore, the identity and reverse identity vectors are padded in
order to become 4096 bytes so that they can be used for performing
arithmetic operations on the 'totalSum' and 'weights' vectors which are
also 4096 bytes.

Depending on the Trivedi's solution, in order to store the subtree
weights' summation, we need to make arithmetic operations on the
'weights' vector. In order to update the subtree sum, we can do the
following that is shown in Figure 13:

!\[Finding the Subtree Sum\](./images/dfs3.png)

By multiplying the 'weights' vector with the identity\[v\] which
contains 1 in its vth position and 'v' becomes the index number of the
child node, finding the total sum of the 'Mul' vector is going to give
us the total sum of the subtree which has the root node 'u'.

Later, in order to find the weights' summation of the current nodes'
children, we can use the following solution in Figure 14:

!\[Editing Weights Vector\](./images/dfs4.png)

We can multiply 'weights' vector with rev-identity\[u\] which contains 0
in its uth position so that, by multiplying with rev-identity\[u\], we
are making the uth position of the 'weights' vector as 0. Then, by
multiplying the 'Sum' vector with identity\[u\], we are editing the uth
position of the 'Sum' vector and make it 0. Later, by summing 'Mul' and
'temp', we are updating the weights vector's uth position with a new
value that is going to be stored in 'Sum' vector. Thus, 'weights'
vector's uth position now contains the current nodes weight.

Finally, the subtree sum differences need to be compared. In order to
compare the differences, we are going to store all the 'totalSum --
2\*Sum' values which gives the subtree sum differences inside a global
variable and the dfs function returns when the recursive call return
back to the node 0 which is the starting node of the dfs function.

## Determining the Minimum Subtree Sum Difference

After the dfs function returns a list that contains 'totalSum -- 2\*Sum'
values of each subtree in the graph, we are going to decrypt the
contents of the global list.

!\[Comparing the Subtree Sum Differences\](./images/dfs5.png)

In order to find the minimum element from the 'outputs' list which
contains the decryption outputs, the negative values are going to be
ignored because in the original solution given by Trivedi, absolute
value of 'totalSum -- 2\*Sum' value is taken but because of the
limitations in EVA, we need to neglect the negative plaintext values.
Then, 'min' variable is set to a large value in order to compare all the
subtree sum differences and therefore we can find minimum difference
between subtrees. The algorithm can be seen in Figure 15.

# Results and Discussion

## Methodology

In order to implement delete edge to minimize subtree sum difference
problem, firstly, Docker is installed and Visual Studio Code with Docker
extension is utilized. The Docker image file was predefined and it
contains EVA and SEAL dependencies. After building the image, the image
run in the container. In favor of creating and drawing a tree, networkx
libraries balanced-tree method is used. The number of children and
height of the tree is changed for calculating the performance of the
implemented algorithm.

## Results

When we look at the implementation results, in the first example, a tree
with 7 nodes, each having 2 children in a tree of height 2 is created
which is shown in Figure 16. The weights are randomly generated and for
the sake of the example, the random values are generated between 1 -10.
We are going to use the 'weights' vector in Figure 17 (the padding
values are ignored when displaying the 'weights' vector):

!\[Example Tree of 7 Nodes\](./images/topo1.png)

!\[Weights Vector\](./images/weights.png)

The 'edges' list can be printed as in Figure 18:

!\[Edges Lis\](./images/edges2.png)

The results can be shown in Figure 19.

!\[Subtree Sum Difference of the First Tree\](./images/res1.png)

If we recalculate the result, the total sum becomes 33. In order to get
1 as the minimum subtree sum difference, one of the subtree summation
need to be 17, and the other need to be 16. We can find this with:

a - (33 - a) = 1, 2a = 34, a = 17 33 - 17 = 16

By comparing with the edges in the tree, if the the edge between 0 - 2
is deleted, it is going to form a subtree summation of 16 (3 + 5 + 8)
and the remaining tree is going to have a summation of 17 (1 + 3 + 5 +
8). As a result, we can determine that deletion of the edge between the
nodes 0 - 2 gives the minimum subtree sum difference.

In a second example, let's have a balanced tree with each node contains
3 children and having a height of 2. The number of nodes becomes 13 and
it can be calculated using the formula in Figure 20 as k becomes the
number of child nodes and h becomes the height of a tree.

!\[Formula to Find the Number of Nodes in a
Tree\](./images/formulae.png)

The Figure 21 shows the corresponding tree. The result can be shown in
Figure 22.

!\[Example Tree of 13 Nodes\](./images/topo2.png)

!\[Subtree Sum Difference of the Second Tree\](./images/ex4.png)

The total sum is 66. We need to find if there is a subtree that it's
weights' summation is 41, and the other subtree's weights' summation
need to become 25. If the edge between nodes 0 -- 2 is deleted, we can
form two such subtrees.

Let's look another example which has 40 nodes, each node is having 3
child and the height of the tree is 3. The tree can be shown in Figure
23 and the results can be shown in Figures 24 and 25.

!\[xample Tree of 40 Nodes\](./images/topo3.png)

!\[Weights and Edges List of the Third Example Tree\](./images/ex2.png)

!\[Subtree Sum Difference of the Third Tree\](./images/ex3.png)

## Discussion

The performance of the delete edge to find subtree sum difference
algorithm can be observed according to the Compile, Key Generation,
Encryption, Execution, Decryption, Reference Execution and Mse times.
The times are generally increasing linearly which is expected when the
number of nodes and therefore the number of elements to be traversed is
increasing which can be seen in the table in Figure 26. The compile, key
generation and execution times become the determinant factor of the
delete edge minimize subtree sum difference problem which takes longer
compared to the encryption and decryption times. On the other hand, key
generation times are varying a lot, seem not depend on the number of
nodes. Encryption times seem to have a approximately constant value but
decryption times are increasing linearly. The encryption and decryption
times are relatively smaller but as it can be seen from the Figure 22,
decryption process takes more time. This can occur because, for example
in asymmetric encryption techniques, decryption times are generally
larger than encryption times because of the modular exponentiation
requirements  [@Karonen2022]. Moreover, when the number of nodes are
increasing in a tree, the vector arithmetic also take times to complete
so that it affects the compile and execution times. The Figure 26 shows
the times according to the number of nodes and height of the tree, the
average values can be seen in bold. Figures 27, 28, 29, 30 and 31
graphically represent the Compile, Key Generation, Encryption,
Execution, Decryption times respectively.

!\[Performance of the Subtree Sum Difference
Algortihm\](./images/tablo3.png)

!\[Compile Time\](./images/compiletime.png)

!\[Key Generation Time\](./images/keygeneration.png)

!\[Encryption Time\](./images/enctime.png)

!\[Execution Time\](./images/executiontime.png)

!\[Decryption Time\](./images/dectime.png)

# Conclusion

In this paper, a solution is given in order to protect privacy of the
delete edge to minimize subtree sum difference problem. Microsoft EVA
library is used for homomorphic encryption in order to perform
arithmetic operation on encrypted data. Homomorphic encryption provides
a way to use encrypted data without the need of decryption in place of
adjusting the data. This can make the arithmetic operations much faster
because the decryption process is only needed when all the required
modifications are completed. Therefore, only one decryption process is
necessary rather than decrypting the data, making modifications and
encrypting the data every time the data requires adjustments.

However, because of the limitations of the Microsoft EVA library,
alternative ways are presented to perform arithmetic operations in order
to edit vector elements. According to the performance results in
Discussion section, the compile and execution times are take longer time
when compared with the encryption and decryption times. Decryption times
are larger than encryption times and the error rate is approximately
2,09 which states that the variance between the results are low and
acceptable.
