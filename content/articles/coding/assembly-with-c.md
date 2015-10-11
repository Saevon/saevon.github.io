Template: article
Title: Compiling Assembly, Integrating with C
Tagline: No more Inline __asm__ statements!
Date: 2015-08-13
Category: coding
Tags: Real-Time (Trains), assembly, ARM



Compiling assembly with C is actually pretty easy, you can even get pre-processor commands into your assembly so you can re-use constants between the two.




# Situation

While writing my microkernel, it was necessary to add a machine specific context switch, for the ARM-920T processor. This meant I needed to add assembly to my C code.

I also needed to have my user tasks call syscall functions, which ended up being stubs for the `swi` ARM assembly command. Thus I needed assembly there too, however it needed to share the `syscall_id` value between the kernel syscall handler, and the user syscall stubs.



# How to create the code

## Header files

First comes the assemble helpers that will let us add immediate values using standard pre-processor constants.

```c
// asm.h

#define immed(val) # ## val
```

It simply defines adds a `#` in front of the value (since ARM assembly uses a hash sign to mark immediate values)

Then define the function headers, so your C compiler knows that the functions will exist when you call the linker later.

```c
// syscall.h

int Create(int priority, void (*code) ( ));
void Exit(void);
```

Finally we have our shared `syscall_id` definitions.

```c
#define SYSCALL_ID_CREATE    1
#define SYSCALL_ID_EXIT      12
```


## Assembly


!alert! info
    The code highlighter doesn't support this, but the "@..." lines are comments in ARM Assembly
!endalert!

You can see the `immed(SYSCALL_ID_CREATE)` doing its job to put the value properly into assembly



<div class="no-pre-err" markdown="1">
```gas
@ sycall.S

#include <machine/asm.h>
#include <kern/syscall_id.h>

@-----------------------------------------------------------
.text
.align  2
.global Create
.type   Create, %function
Create:
    @ args = 0, pretend = 0, frame = 8
    @ frame_needed = 1, uses_anonymous_args = 0

    @ Push the args
    stmfd sp!, {r0-r1}

    @ Software interrupt, doing the syscall
    swi immed(SYSCALL_ID_CREATE)

    @ Fix the stack pointer
    add sp, sp, #8

    @ Exit back to previous frame
    mov pc, lr
.size   Create, .-Create
@-----------------------------------------------------------


@-----------------------------------------------------------
.text
.align  2
.global Exit
.type   Exit, %function
Exit:
    @ args = 0, pretend = 0, frame = 0
    @ frame_needed = 1, uses_anonymous_args = 0

    @ Software interrupt, doing the syscall
    swi immed(SYSCALL_ID_EXIT)

    @ Exit back to previous frame
    mov pc, lr
.size   Exit, .-Exit
@-----------------------------------------------------------

```
</div>







# How to set-up your Makefile

First we need to find each of the files, remember the `*.S` files are your assembly + preproccessor.

Then we convert their endings to the resulting files that we want: `*.o` files

```make
# Kernel libraries
ASMLIB = $(shell find ./kern/asm/ -name "*.S")
CLIB = $(shell find ./kern/ -name "*.c")

all: $(patsubst %.c,%.o,$(LIBS)) $(patsubst %.S,%.o,$(ASMLIB))
```

Then we have the actual commands that will compile the files.

Notice that the `*.S` files only get pre-processed by gcc (using the `-E` flag). Then they follow the standard chain to become `*.o` files.

```make
%.s: %.c
    $(CC) -S $(CFLAGS) -o $@ $<

%.o: %.s
    $(AS) $(ASFLAGS) -o $@ $<

kern/asm/%.s: kern/asm/%.S
    $(CC) -E $(CFLAGS) -O0 -o $@ $<
```



