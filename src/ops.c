#include "../header/push_swap.h"

// Swap the first 2 elements at the top of stack
int s(t_list **stack)
{

	t_list	*oldFirst;
	t_list	*newFirst;

	if (stack && ft_lstsize(*stack) > 1)
	{
		oldFirst = *stack;
		newFirst = (*stack) -> next;
		oldFirst -> next = newFirst -> next;
		newFirst -> next = oldFirst;
		*stack = newFirst;
		return (1);
	}
	return (0);

}
// Take the first element at the top of stack2 and put it at the top of stack1
int	p(t_list **stack1, t_list **stack2)
{
	t_list	*newHeadS1;
		
	if ((stack2 && stack1) && (*stack2 && *stack1))
	{
		newHeadS1 = *stack2;
		(*stack2) = (*stack2) -> next;
		ft_lstadd_front(stack1, newHeadS1);
		return (1);
	}
	return (0);
}
// The first element becomes the last one
int	r(t_list **stack)
{
	t_list *newTail;
	t_list	*newHead;

	if (stack && *stack)
	{
		newTail = *stack;
		newHead = (*stack) -> next;
		newTail -> next = NULL;
		ft_lstadd_back(&newHead, newTail);
		*stack = newHead;
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
		return (1);
	}
	return (0);
}

int	main(void)
{
	t_list	*stack1;
	t_list	*stack2;
	t_list	el;
	int		counter;

	counter = 0;
	stack1 = NULL;

	el.content = (void *)"good";
	el.next = NULL;

	printf("%d\n", ft_lstsize(stack1)); // == 0

	stack1 = ft_lstnew((void *)"hello");
	printf("%d\n", ft_lstsize(stack1)); // == 1

	ft_lstadd_front(&stack1, &el);
	printf("%d\n", ft_lstsize(stack1)); // == 2

	ft_lstadd_back(&stack1, ft_lstnew((void *)"bye"));
	printf("%d\n", ft_lstsize(stack1)); // == 3

	ft_lstadd_back(&stack1, ft_lstnew((void *)"greetings"));
	printf("%d\n", ft_lstsize(stack1)); // == 4

	ft_lstprint(stack1);

	stack2 = ft_lstnew((void *)"Morning");
	ft_lstadd_back(&stack2, ft_lstnew((void *)"Madam"));
	printf("%d\n", ft_lstsize(stack2)); // == 1

	ft_lstprint(stack2);

	// ft_printf("\nChecking S function\n");
	// // Check if s func works
	// printf("%d\n", s(&stack1));
	// ft_lstprint(stack1);
	// s(&stack1);

	// ft_printf("\nChecking P function\n");
	// // Check if p func works
	// counter += p(&stack1, &stack2);
	// ft_lstprint(stack1);
	// ft_printf("\n");
	// ft_lstprint(stack2);

	// // ft_printf("\n");
	// ft_printf("\n");
	// counter += p(&stack2, &stack1);
	// counter += p(&stack2, &stack1);
	// counter += p(&stack2, &stack1);
	// counter += p(&stack2, &stack1);
	// counter += p(&stack2, &stack1);
	// counter += p(&stack2, &stack1);
	// ft_lstprint(stack1);
	// printf("%d\n", ft_lstsize(stack1)); // == 0
	// printf("%d\n", ft_lstsize(stack2)); // == 5

	// ft_printf("\n");
	// ft_lstprint(stack2);


	ft_printf("\nChecking R function\n");
	// Check the r func
	ft_lstprint(stack1);
	counter += r(&stack1);
	counter += r(&	stack1);
	ft_printf("\n");
	ft_lstprint(stack1);

	ft_printf("%d\n", counter);
}