Project 
<b>Randomized Meldable Priority Queues</b>

<b>Introduction</b><br>
In this paper we present a randomized approach to the problem of effcient <br>
meldable priority queue implementation. The operations supported by this data <br>
structure are the following<br>
MakeQueue(Q)   returns an empty priority queue.<br>
FindMax(Q)     returns the minimum item from priority queue Q .<br>
DeleteMax (Q) deletes and returns the maximum item from priority queue Q .<br>
Insert ( Q; e ) inserts item e into priority queue Q .<br>
Meld ( Q 1 ; Q 2 ) returns the priority queue formed by combining disjoint priority<br>
queues Q 1 and Q 2 .<br>
Delete ( Q; e ) deletes item e from priority queue Q provided the location of e<br>
in Q is known.<br>
<br>
Heap Implementation:<br>

This page discusses the particulars of my [implementation] (https://github.com/M-abdullah-69/Hello_World) of the heap data structure. My heap is originally based on the pseudocode written in the researchpaper article about Heaps.
The Heap structure

<br><br>
AX-HEAPIFY(A, 1) <br>
  &nbsp; &nbsp; l = LEFT(i) <br>
  &nbsp; &nbsp; r = RIGHT(i) <br>
  &nbsp; &nbsp; if l <= A.heap-size and A[l] > A[i] <br>
  &nbsp; &nbsp;&nbsp;&nbsp;largest = l <br>
  &nbsp; &nbsp;else largest = i <br>
  &nbsp; &nbsp;if r <= s A.heap-size and A [r] > A[largest] <br>
  &nbsp; &nbsp;&nbsp;&nbsp;largest = r <br>
  &nbsp; &nbsp;if largest not equal to l <br>
  &nbsp; &nbsp;&nbsp;&nbsp;exchange A[i] with A [largest] <br>
  &nbsp; &nbsp;&nbsp;&nbsp;MAX-HEAPIFY (A, largest) <br>
<br><br>
The simplest way to describe all remaining priority queue operations is to <br>
de ne them in terms of Meld . In order to Insert item e into heap Q we create <br>
a single node containing item e and meld it with Q . DeleteMin melds the left <br>
and right subtrees of the root and returns the item held in the (old) root. <br>
For DecreaseKey and Delete we need the parent pointer in each node. <br>
In order to decrease the value of node x in heap Q we detach the tree rooted <br>
at x from Q , adjust the item at x accordingly and then meld Q with the heap <br>
rooted at x . Operation Delete also detaches the tree rooted at x from heap <br>
Q , and then performs DeleteMin on heap rooted at x and nally Meld the <br>
resulting heap and Q. <br> 
<br>
<b>Conclusions</b><br>
Before the concluding remarks let us note that the exibility of the randomized<br>
heap can be increased by scaling it in the manner similar to well known d-ary<br>
heaps. Let us x an integer d >= 2 and make the underlying structure of the heap<br>
be a tree with at most d children in each node (kept in an array of size d ). The<br>
only change to operation Meld is that instead of tossing a symmetric coin we<br>
choose value t from { 1 ,....., d } at random and recursively meld the tree with the<br>
bigger key at the root with t -th subtree of the other tree.<br>

<br>
--------------------------------------------------------------------------------------------------------------------
