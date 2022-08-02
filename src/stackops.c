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

int	main(void)
{
	t_list	*stack1;
	// t_list	*stack2;
	t_list	el;
	int		counter;
	int		n[4] = {4,3,1,2};

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