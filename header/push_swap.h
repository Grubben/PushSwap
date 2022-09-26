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
 * Normal rotates the stack
 * the amount specified
 */
int	rotate(t_list **stack, int howMany);

/*
 * The last element becomes the first one
 */
int	rr(t_list **stack);

/*
 * Reverse rotates the stack
 * the amount specified
 */
int	revRotate(t_list **stack, int howMany);


# endif
