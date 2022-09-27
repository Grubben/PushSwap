/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps.c                                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amaria-d <amaria-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/27 10:05:38 by amaria-d          #+#    #+#             */
/*   Updated: 2022/09/27 10:54:46 by amaria-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

int main(int argc, char **argv)
{
    t_list  *args, *b;
    int     i, count;
    int     *tmp;

    if (argc < 2)
        return (0);
    tmp = ft_calloc(1, sizeof(int));
    args = ft_lstnew(tmp);
    i = 1;
    while (argv[i])
    {
        tmp = ft_calloc(1, sizeof(int));
        *tmp = ft_atoi(argv[i]);
        ft_lstadd_back(&args, ft_lstnew(tmp));
        i++;
    }
    b = NULL;
    count = bgearSort(&args, &b);

    ft_printf("Number of moves: %d", count);
    
    return (0);
}