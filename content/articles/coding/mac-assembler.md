Template: article
Title: Using the proper Assembler on Mac OSX
Tagline: Making things work
Date: 2014-06-20
Category: coding
Tags: Mac OSX, assembler, clang, Real-Time (Trains)




The standard compiler `gcc` for Mac OSX is actually the `clang` compiler, this means that you need to use its assembler and linker as well. If you try to do the compilation in steps, you will notice that "`as`" is not the clang assembler however, which causes it to break down.

In this article I will discuss a simple solution to this problem.


# Intro {#intro}

!alert!  info
    Jump straight to the [solution](#solution), or read about the situation ahead.
!endalert!

I was working on a microkernel `(CS 452: Real Time Programming)`, and I needed to do my compilations with a custom compiler, assembler and linker, so I could compile for ARM. However this required me to use an older version of gcc without the `--with-as=` flag, thus I needed to get the assembler to run as a seperate command.

Enter a complication: I needed this to run tests on my local machine (Mac), as well as on those of my partners (Windows running cygwin), I also needed this to compile on a remote Linux server, which could do the necessary cross-compilation.

My resulting makefile had the following basic structure.

```make
# Create the assembly file so that we can use a seperate assembler in the next step
%.s: %.c
    $(CC) -S $(CFLAGS) -o $@ $<

# Use out assembler to compile an object file
%.o: %.s
    $(AS) $(ASFLAGS) -o $@ $<

# Combine the object files using the linker
%.elf: %.o
    $(LD) $(LDFLAGS) -Map $*.map -o $@ $*.o $(INC) -lgcc
    chmod a+r $@
```

First we generate the assembly files, next we assemble the resulting files into object files. Finally we produce the elf file that will represent my Kernel.

This will run properly on the linux machine, however when I try to use the same makefile to generate code locally, it fails.





# Solution {#solution}

The error I get looks like this.

```
test_cbuf.s:5:Unknown pseudo-op: .cfi_startproc
test_cbuf.s:9:Unknown pseudo-op: .cfi_def_cfa_offset
```

So the assemble results from `gcc` can't be read by the assembler?

It seems the `gcc` and the `as` progams that Mac has by default use differing standards.

The correct assembler to use uses a command like the following:

```bash
clang -c -x assembler $@
```

-----------------

Now to solve my situation above:

* I can give a different `AS = "clang -c -x assembler"` variable to my makefile

    * But then I either need to call it that way always (a pain) or add different instructions

* I can add a simple bash script that calls the code above, one that is earlier in my `$PATH`


I opted for the second solution, mostly since this seems to be a more common use-case for me.




