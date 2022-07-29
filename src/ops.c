#include "../header/push_swap.h"

int s(t_list **stack)
//TODO: TBC and verified
{
	t_list *newFirst;

	if (stack && ft_lstsize(*stack) > 1)
	{
		newFirst = (*stack)->next;
		ft_lstadd_back(stack, *stack);
		stack = &newFirst;
		return (1);
	}
	return (0);
}

int	p(t_list **stack1, t_list **stack2)
//TODO: TBC and verified
{
	t_list	*newHeadS1;
		
	if (stack2)
	{
		newHeadS1 = *stack2;
		(*stack2) = (*stack2) -> next;
		ft_lstadd_front(stack1, newHeadS1);
		return (1);
	}
	return (0);
}

int	r(t_list **stack)
//TODO: TBC and verified
{
	t_list *newTail;
	t_list	*newHead;

	if (stack)
	{
		newTail = *stack;
		newHead = (*stack) -> next;
		newTail -> next = NULL;
		ft_lstadd_back(&newHead, newTail);
		return (1);
	}
	return (0);
}

int	rr(t_list **stack)
//TODO: TBC and verified
{
	t_list	*newHead;
	t_list	*newTail;

	if (stack)
	{
		newHead = ft_lstlast(*stack);
		newTail = ft_lstindex(*stack, -2);
		newTail -> next = NULL;
		newHead -> next = *stack;
		*stack = newHead;
	}
}