#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "../deps/libft.h"
/*
 * Implmenting stack for PS as list
 */
typedef struct s_ilist
{
	int				num;
	struct s_list	*next;
}			t_ilist;


/*
 * Swap the first 2 elements at the top of stack
 */
int s(t_list **stack);

/*
 * Take the first element at the top of stack2 and put it at the top of stack1
 */
int	p(t_list **stack1, t_list **stack2);

/*
 * The first element becomes the last one
 */
int	r(t_list **stack);

/*
 * The last element becomes the first one
 */
int	rr(t_list **stack);

/*
 * Normal rotates the stack
 * the amount specified
 */
int	rotate(t_list **stack, int howMany);

/*
 * Reverse rotates the stack
 * the amount specified
 */
int	revRotate(t_list **stack, int howMany);


/*	PRINTER OPS	*/

int s_p(t_list **stack, char verbChar);

int p_p(t_list **stack1, t_list **stack2, char verbChar);

int r_p(t_list **stack, char verbChar);

int rr_p(t_list **stack, char verbChar);

int	rotate_p(t_list **stack, int howMany, char verbChar);

int	revRotate_p(t_list **stack, int howMany, char verbChar);


/*	STACKOPS	*/

int	is_ascendingP(t_list *stack);

int	is_descendingP(t_list *stack);

int	set_ascending(t_list **stack, char verbChar);

int	set_descending(t_list **stack, char verbChar);

/*
 * Drains all nums in giver to receiver with p
 */
int	drain_p(t_list **giver, t_list **receiver, char verbChar);

/*
 * Returns whether the stack is Turned or not
 */
int	turnedP(t_list *stack);

/*
 * A switched stack is in the order specified by
 * verifierF with a single swap. VerifierF is a predicate
 */
int	switchedP(t_list *stack, int (*f)(t_list *));

/*
 * Swaps at given location
 */
int	swap_at(t_list *stack, int index);

/*
 * Rotates the given stack to get the more efficient
 * lower number to the top
 */
size_t	prepTop(t_list **stack, unsigned int chunks, char verbChar);


/*	BGEARSORT	*/

size_t  bgearSort(t_list **a, t_list **b);

# endif
