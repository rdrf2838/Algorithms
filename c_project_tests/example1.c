#include <stdio.h>
#include "library.h"

# if !defined(HELLO_WORLD)
#   error "must say hello to world"
#endif

int main(void)
{
    printf("result is %d\n", add(1,2));
}
