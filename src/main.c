#include <stdio.h>
#include "../header/push_swap.h"

int main()
{
    t_list *first;
    int     num;

    num = 32;
    first = ft_lstnew(&num);
    printf("%p", first->content);

    return 0;
}

