#include "../header/push_swap.h"

int	s(t_list **stack)
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
