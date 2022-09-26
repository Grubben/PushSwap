#include "../header/push_swap.h"

int	is_ascendingP(t_list *stack)
{
	int		before;

	if (!stack)
		return (-1);

	before = *(int *)(stack->content);
	while (stack->next != NULL)
	{
		stack = stack->next;
		if (before > *(int *)(stack->content))
			return (0);
		before = *(int *)(stack->content);
	}
	return (1);
}


int	is_descendingP(t_list *stack)
{
	int		before;

	if (!stack)
		return (-1);

	before = *(int *)(stack->content);
	while (stack->next != NULL)
	{
		stack = stack->next;
		if (before < *(int *)(stack->content))
			return (0);
		before = *(int *)(stack->content);
	}
	return (1);
}


/*
 * [1, 2, 3]
 */
int	set_ascending(t_list **stack)
{
	int	moves;
	
	moves = 0;
	if (ft_lstindex(*stack, ft_lstmax(*stack)) > (ft_lstlen(*stack) / 2))
	{
		while (**(int **)((*stack)->content) != ft_lstmin(*stack))
		{
			rr(stack);
			moves++;
		}
	}
	else
	{
		while (**(int **)((*stack)->content) != ft_lstmin(*stack))
		{
			r(stack);
			moves++;
		}
	}
	return moves;
}

/*
 * [3, 2, 1]
 */
int	set_descending(t_list **stack)
{
	int	moves;
	
	moves = 0;
	if (ft_lstindex(*stack, ft_lstmax(*stack)) > (ft_lstlen(*stack) / 2))
	{
		while (**(int **)((*stack)->content) != ft_lstmax(*stack))
		{
			rr(stack);
			moves++;
		}
	}
	else
	{
		while (**(int **)((*stack)->content) != ft_lstmax(*stack))
		{
			r(stack);
			moves++;
		}
	}
	return moves;
}


/*
 * Drains all nums in giver to receiver with p
 */
int	drain(t_list **giver, t_list **receiver)
{
	size_t	moves;
	
	moves = set_descending(giver);
	while (*giver)
	{
		p(receiver, giver);
		moves++;
	}
	return moves;
}


/*
 * Returns whether the stack is Turned or not
 */
int	turnedP(t_list *stack)
{
	int	exceptions;
	size_t	i;

	if (ft_lstlen(stack) < 2)
		return (0);
	if (ft_lstget_item(stack, 0) < ft_lstget_item(stack, -1))
		return (0);
	exceptions = 0;
	i = 0;
	while (i < ft_lstlen(stack) - 1)
	{
		if (ft_lstget_item(stack, i) > ft_lstget_item(stack, i + 1))
		{
			exceptions++;
			if (exceptions > 1)
				return (0);
		}
		i++;
	}
	return (1);
}


/*
 * A switched stack is in the order specified by
 * verifierF with a single swap. VerifierF is a predicate
 */
int	switchedP(t_list *stack, int (*f)(t_list *))
{
	t_list	*replica;
	size_t		index, rotates;

	if (ft_lstlen(stack) < 2)
		return (-1);
	replica = ft_lstcpy(stack);
	index = 0;
	rotates = 0;
	while (index < ft_lstlen(replica))
	{
		rotates = index;
		while (rotates)
		{
			r(&replica);
			rotates--;
		}
		s(&replica);
		while (rotates < index)
		{
			rr(&replica);
			rotates++;
		}
		if (f(replica))
			return (index);
		
		// Goes back to undo the swap
		while (rotates)
		{
			r(&replica);
			rotates--;
		}

		s(&replica);

		while (rotates < index)
		{
			rr(&replica);
			rotates++;
		}

		index++;
	}
	return (-1);
}

int	swap_at(t_list *stack, int index)
{
	int	moves, rotates;

	if (!stack && !index)
		return (-1);
	moves = 0;
	rotates = index;
	while (rotates)
	{
		moves = moves + r(&stack);
		rotates--;
	}
	moves = moves + s(&stack);
	while (rotates < index)
	{
		moves = moves + rr(&stack);
		rotates++;
	}
	return (moves);
}

/*
int	main(void)
{
	t_list	*stack1;
	// t_list	*stack2;
	t_list	el;
	int		counter;
	int		n[4] = {1,2,3,4};

	counter = 0;
	stack1 = NULL;

	el.content = (void *)(&n);
	el.next = NULL;

	
	stack1 = &el;

	ft_lstadd_back(&stack1, ft_lstnew((void *)&(n[1])));

	ft_lstadd_back(&stack1, ft_lstnew((void *)&(n[2])));

	ft_lstadd_back(&stack1, ft_lstnew((void *)&(n[3])));

	// ft_lstprint(stack1);
	// ft_printf("%d\n", *(int *)(stack1->next->next->next->content));

	// Check asc/desc functions
	ft_printf("%d\n", is_ascendingP(stack1));
	ft_printf("%d\n", is_descendingP(stack1));
}
*/
