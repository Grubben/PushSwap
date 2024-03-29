# project name (generate executable with this name)
TARGET		= push_swap

# Project Structure
SRCDIR		= src
OBJDIR		= obj
BINDIR		= bin
DEPSDIR		= deps

SUBDIRS		= libft
LIBS		= ft

## COMPILATION
CC 			= gcc
# Compilation Flags
CFLAGS		= -g3 -Wall -Wextra -Werror

## LINKAGE
# LINKER		= gcc
# # Linking Flags
# LFLAGS		= -Wall -Wextra -Werror -L$(DEPSDIR) -l$(LIBS)


# Removal Flags. Not sure if necessary
RM			= rm -rf


SOURCES		:= $(wildcard $(SRCDIR)/*.c)
OBJECTS		:= $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)


NAME		= $(BINDIR)/$(TARGET)

all			: libft.a $(NAME)

$(NAME)		: all
				# @$(LINKER) $(OBJECTS) $(LFLAGS) -o $@
				$(CC) -o $@ $(OBJECTS) $(DEPSDIR)/libft.a
				@echo "Linking complete!"


$(OBJECTS)	: $(OBJDIR)/%.o : $(SRCDIR)/%.c
				$(CC) $(CFLAGS) -c $< -o $@
				@echo "Compiled "$<" successfully!"

libft.a		:
				$(MAKE) -C libft libft.a
				cp libft/libft.a $(DEPSDIR)
				cp libft/libft.h $(DEPSDIR)


clean		:
				# $(RM) $(OBJECTS)
				$(RM) $(OBJDIR)/*

fclean		: clean
				$(RM) $(BINDIR)/*
				$(RM) $(DEPSDIR)/*
				$(MAKE) -C $(SUBDIRS) fclean

re			: fclean $(NAME)


.PHONY		: all bonus clean fclean re
