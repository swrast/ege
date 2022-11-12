#include <stdio.h>

int main() {
    for(unsigned int i = 45000000; i < 50000000; i++) {
        int count = 0;

        for(unsigned int k = 0; k < i; k++)
            if(i % k == 0)
                if(k % 2 == 1)
                    count++;

        if(count == 5)
            printf("%d", i);
    }
}
