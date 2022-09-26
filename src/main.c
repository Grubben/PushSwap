//#include <stdio.h>
#include "../header/push_swap.h"

int main()
{
    t_list *a1;

    int num[3] = {11, 22, 33};
    a1 = ft_lstnew(&num[0]);

    t_list *b1;
    b1 = ft_lstnew(&num[1]);

    // ft_printf("%i\n", *(int *)(a1->content));
    // ft_printf("%i\n", *(int *)(b1->content));

    ft_lstprint(a1);
    ft_printf("\n");
    ft_lstprint(b1);

    p(&a1, &b1);

    ft_lstprint(a1);
    ft_printf("\n");
    ft_lstprint(b1);

    ft_printf("%p\n", b1);

    return 0;
}

