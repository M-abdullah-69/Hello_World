Randomized Meldable Priority Queues
Anna Gambin and Adam Malinowski
Instytut Informatyki, Uniwersytet Warszawski,
Banacha 2, Warszawa 02-097, Poland,
f aniag,amal g @mimuw.edu.pl
Abstract. We present a practical meldable priority queue implementa-
tion. All priority queue operations are very simple and their logarithmic
time bound holds with high probability, which makes this data structure
more suitable for real-time applications than those with only amortized
performance guarantees. Our solution is also space-ecient, since it does
not require storing any auxiliary information within the queue nodes.
1 Introduction
In this paper we present a randomized approach to the problem of ecient
meldable priority queue implementation. The operations supported by this data
structure are the following [10]:
returns an empty priority queue.
( Q ) returns the minimum item from priority queue Q .
DeleteMin ( Q ) deletes and returns the minimum item from priority queue Q .
Insert ( Q; e ) inserts item e into priority queue Q .
Meld ( Q 1 ; Q 2 ) returns the priority queue formed by combining disjoint priority
queues Q 1 and Q 2 .
0
0
0
DecreaseKey ( Q; e; e ) replaces item e by e in priority queue Q provided e  e
and the location of e in Q is known.
Delete ( Q; e ) deletes item e from priority queue Q provided the location of e
in Q is known.
MakeQueue
FindMin
(The last two operations are sometimes considered optional.)
In existing priority queue implementations the approach is two-fold. Most
data structures require storing additional balance information associated with
queue nodes in order to guarantee the worst-case eciency of individual opera-
tions (e.g. leftist trees [8], relaxed heaps [5], Brodal queues [3, 4]). Others achieve
good amortized performance by adjusting the structure during some operations
rather than struggling to maintain balance constantly (skew heaps [12, 13], pair-
ing heaps [6]). Experiments indicate that the latter approach is more promising
in practice [1, 7, 9]. This is due to the fact that the worst-case ecient structures
tend to be complex and hard to implement therefore big constant factors hidden
in their complexity estimates prevail their theoretically superior performance.On the other hand, the main disadvantage of the amortized approach is that
it cannot be applied in real-time programs, where the worst-case bound on the
running time of each individual operation is crucial.
Our solution, both simple and worst-case ecient (in the probabilistic sense),
avoids these drawbacks by adopting the randomized approach, earlier applied to
construct abstract data structures mainly in the context of dictionaries (e.g.
[2, 11]). The idea is loosely based on leftist trees and skew heaps. All other
operations are de ned in terms of Meld which in both structures is performed
along right paths in melded trees. The subtrees of a node on the right path are
exchanged in order to keep the path short: in leftist trees { sometimes (depending
on their ranks); in skew heaps { always. In our data structure Meld operation is
performed along random paths in melded trees. This approach has the following
advantages:
Simplicity. All operations are easy to implement and the constant factors in
their complexity bounds are small, thus, given a fast random number gener-
ator, the heaps should perform well in practice.
Space economy. Since we do not need to preserve any balance conditions, no
satellite information within nodes is necessary.
Applicability to parallel computations. A single-pass top-down scheme of
each operation allows to perform a sequence of operations in a pipelined
fashion. Moreover, the loose structure of a heap allows to process disjoint
sets of nodes independently.
Worst-case eciency. The execution time of each individual operation is at
most logarithmic with high probability. The expected time behaviour de-
pends on the random choices made by the algorithm rather than the dis-
tribution of an input sequence, which allows using this data structure in
real-time applications.
The rest of this paper is organized as follows. In Section 2 we describe the
data structure and the implementation of meldable priority queue operations.
Section 3 is devoted to the eciency analysis of these algorithms. Section 4
presents some experimental results. Finally, Section 5 contains discussion of some
extensions of the data structure and the conclusions.
2 The Randomized Heap
The underlying data structure of the randomized heap is a binary tree with one
item per node, satisfying heap property : if x and y are nodes and x is the parent
of y then item ( x )  item ( y ). The heap is accessed by the root of the tree.
Let us now describe the implementation of meldable priority queue operations
for randomized heap. MakeQueue returns an empty tree and FindMin returns
an item held in the root. In order to Meld two nonempty trees with roots Q 1
and Q 2 , respectively, we compare the items held in the roots. The root with the
smaller key, say Q 1 , becomes the root of the resulting tree and Q 2 , the remaining
one, is recursively melded with either left or right child of Q 1 , depending onthe outcome of a coin toss. More formal de nition is given by the following
pseudocode:
heap function
( heap Q ; Q )
if Q =
) return Q
if Q =
) return Q
if item ( Q ) > item ( Q ) ) Q $ Q
if toss coin =
) left ( Q ) :=
( left ( Q ) ; Q )
else right ( Q ) :=
( right ( Q ) ; Q )
return Q
Meld
1 null
2 null
1
2
2
1
1
2
1
heads
1
Meld
2
Meld
1
1
1
2
2
1
(The results of Section 3 imply that the recursion depth is at most logarithmic
with high probability. Moreover, this tail-recursion is easily removable and serves
the purpose of increasing readability only.)
The simplest way to describe all remaining priority queue operations is to
de ne them in terms of Meld . In order to Insert item e into heap Q we create
a single node containing item e and meld it with Q . DeleteMin melds the left
and right subtrees of the root and returns the item held in the (old) root.
For DecreaseKey and Delete we need the parent pointer in each node.
In order to decrease the value of node x in heap Q we detach the tree rooted
at x from Q , adjust the item at x accordingly and then meld Q with the heap
rooted at x . Operation Delete also detaches the tree rooted at x from heap
Q , and then performs DeleteMin on heap rooted at x and nally Meld the
resulting heap and Q .
3 The Eciency Analysis
Since all non-constant-time operations are de ned in terms of Meld , it is enough
to analyze the complexity of melding two randomized heaps.
Let us x an arbitrary binary tree Q with n interior nodes containing keys
and n + 1 exterior null nodes { the leaves of the tree. De ne a random variable
h Q to be the length (the number of edges) of a random path from the root down
to an exterior node (the child following each interior node on a path is chosen
randomly and independently). In other words, the probability space is the set
of all exterior nodes in Q with probability of a node at depth t equal to 2 ? t ,
and h Q is the depth of an exterior node chosen randomly with respect to this
distribution.
Lemma 1. Melding two randomized heaps Q 1 and Q 2 requires time O ( h Q 1 +
h Q 2 ) .
Proof. The melding procedure traverses a random path in each tree until an
exterior node in one of them is reached.
t
It follows from Lemma 1 that in order to bound the complexity of melding
randomized heaps it is enough to estimate h Q for an arbitrary binary tree Q .Theorem 1. Let Q be an arbitrary binary tree with n interior nodes.
(a) The expected value Eh Q  log( n + 1) .
(b) Pr [ h Q > ( c + 1) log n ] < n c , for any constant c > 0 .
1
Proof. (a) The proof follows by induction on n . Assume n > 0 and let n L and
n R be the number of interior nodes in the left ( Q L ) and right ( Q R ) subtree of
Q , respectively (thus n = n L + n R + 1). We have
Eh Q = 2 1 ((1 + Eh Q L ) + (1 + Eh Q R ))  1 + 2 1 (log( n L + 1) + log( n R + 1))
= log 2 ( n + 1)( n + 1)  log 2 ( n L + 1) + ( n R + 1)
p
L
R
2
= log( n L + n R + 2) = log( n + 1)
(b) Note that for any xed path from the root to an exterior node the proba-
bility that is the outcome of a random walk down the tree equals 2 ?j j , where
j j is the length of .
Let ? be the set of all paths from the root to an exterior node in Q with
length exceeding ( c + 1) log n . We have
Pr[ h Q > ( c + 1) log n ] =
X 2 ?j j < X 2 ?
( c +1) log n
2 ?
2 ?
= j ? j n ? ( c +1)  n ? c
t
Corollary 1. The expected time of any meldable priority queue operation on a
n -node randomized heap is O (log n ) . Moreover, for each constant  > 0 there
exists a constant c > 0 such that the probability that the time of each operation
is at most c log n exceeds 1 ? n ?  .
Proof. Immediate by Lemma 1 and Theorem 1.
t
4 Experiments
We have carried out some tests to measure the behaviour of the randomized heap
in practice. It is not hard to see that the value h Q is bigger for more balanced
trees and smaller for \thinner" ones. When we create a tree by inserting the keys
1 ; : : : ; n in the order of some permutation  then the tree is more balanced if 
is closer to the sorted sequence < 1 ; : : : ; n > , and \thinner" if  is closer to the
inverted sequence < n; : : : ; 1 > . Thus our methodology was the following: for a
xed n subsequently we created a tree
{ from an almost sorted permutation ( n transpositions away from < 1 ; : : : ; n > ),
{ from a random permutation,
2{ from an almost inversely sorted permutation ( n transpositions away from
< n; : : : ; 1 > ),
2
then we computed the value of h and the total length of paths traversed while
melding two such trees (both consisting of keys 1 ; : : : ; n ). Since we can get dif-
ferent trees even from a xed permutation, the outcomes were averaged over 100
tests for each value of n .
The results are summarized in the following table (each displayed value is
the factor c in expression c log( n + 1)):
n
50
500
5000
15000
Almost sorted Random Almost inverted
permutation permutation permutation
h meld h meld h
meld
0 : 85 1 : 34 0 : 79 1 : 28 0 : 63 0 : 79
0 : 80 1 : 39 0 : 76 1 : 31 0 : 50 0 : 65
0 : 78 1 : 41 0 : 74 1 : 32 0 : 40 0 : 49
0 : 77 1 : 42 0 : 73 1 : 32 0 : 36 0 : 41
It turns out that in case of a tree obtained from a random permutation the
value of h is just 4 3 of the value for the full tree. Moreover, the total length of
paths traversed while melding two such trees is about 15% smaller than doubled
value of h , as used for an estimation in Lemma 1. (This is not surprising because
only one of two random paths is traversed to the very end while melding.)
5 Conclusions
Before the concluding remarks let us note that the exibility of the randomized
heap can be increased by scaling it in the manner similar to well known d -ary
heaps. Let us x an integer d  2 and make the underlying structure of the heap
be a tree with at most d children in each node (kept in an array of size d ). The
only change to operation Meld is that instead of tossing a symmetric coin we
choose value t from f 1 ; : : : ; d g at random and recursively meld the tree with the
bigger key at the root with t -th subtree of the other tree. An easy adaptation
of the proofs from Section 3 gives the following estimates for the complexity of
operations on a randomized d -heap with at most n nodes:
{ MakeQueue, FindMin | O (1)
{ Meld, DecreaseKey | O (log d n )
{ Insert | O ( d + log d n ) (we have to initialize d pointers in the new node to
null )
{ DeleteMin, Delete | O ( d log d n ) (we have to meld O ( d ) heaps)
We have presented a very simple randomized data structure capable to sup-
port all meldable priority queue operations in logarithmic time with high prob-
ability. The experiments show that the constant factors in the complexity ofthe operations are in fact even smaller than those derived from the theoretical
analysis. Simplicity, exibility and small memory overhead make the randomized
heap seem to be a practical choice for a meldable priority queue with worst-case
performance guarantees.
The following question looks as a good starting point for further research:
does the randomized approach allow us to lower the asymptotic complexity of
some meldable priority queue operations while keeping the data structure sim-
ple?
References
1. T. Altman, B. Chlebus, A. Malinowski, M. S  lusarek, manuscript.
2. C. R. Aragon, R. G. Seidel, Randomized search trees. Algorithmica 16(1996),
464-497.
3. G. S. Brodal, Fast meldable priority queues, Proc. 4th Workshop on Algorithms
and Data Structures, vol. 955 of Lecture Notes in Computer Science, 282-290,
Springer-Verlag, Berlin, 1995.
4. G. S. Brodal, Worst-case ecient Priority Queues, Proc. 17th ACM-SIAM Sym-
posium on Discrete Algorithms, 1996, 52-58.
5. J. R. Driscoll, H. N. Gabow, R. Shrairman, R. E. Tarjan, Relaxed heaps: An
alternative to Fibonacci heaps with applications to parallel computation. Comm.
ACM 31(1988), 1343-1354.
6. M. L. Fredman, R. Sedgewick, D. D. Sleator, R. E. Tarjan, The pairing heap: A
new form of self-adjusting heap. Algorithmica 1(1986), 111-129.
7. D. W. Jones, An empirical comparison of priority queue and event set implemen-
tations, Comm. ACM 29(1986), 300-311.
8. D. E. Knuth, The Art of Computer Programming, Volume 3: Sorting and Search-
ing, Addison-Wesley, Reading, MA, 1973.
9. A. M. Liao, Three priority queue applications revisited. Algorithmica 7(1992),
415-427.
10. K. Mehlhorn, A. K. Tsakalidis, Data Structures, In J. van Leeuwen, editor, Hand-
book of Theoretical Computer Science, Volume A: Algorithms and Complexity,
MIT Press/Elsevier, 1990.
11. W. Pugh, Skip Lists: A probabilistic alternative to balanced trees, Comm. ACM ,
33(1990), 668-676.
12. D. D. Sleator, R. E. Tarjan, Self-adjusting binary trees, Proc. 15th ACM Symp.
on Theory of Computing, 1983, 235-246.
13. D. D. Sleator, R. E. Tarjan, Self-adjusting heaps, SIAM J. Comput. 15(1986),
52-69.
