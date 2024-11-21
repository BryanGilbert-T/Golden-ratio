#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int optimize(char str[20]);

int rilOptimize(char str[20]){
    int len = strlen(str);
    int max = optimize(str);
    for(int i = 0; i < len; i++){
        char tempChar[20];
        strcpy(tempChar, str);
        for(int j = i; j < len; j++){
            tempChar[j] = '0';
            int res = optimize(tempChar);
            if(res > max){
                max = res;
            }
        }
    }

    return max;
}

int optimize(char str[20]){
    int len = strlen(str); 
    int ways = 0;
    for(int i = 0; i < len; i++){
        for(int j = i; j < len; j++){
            while(str[j] == '0'){
                j++;
            }
            if(str[i] == str[j]){
                ways++;
            }
            else{
                break;
            }
        }
    }
    return ways;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int n =0 ; n < T; n++){
        char str[20];
        scanf("%s", str);
        int ways = rilOptimize(str);
        printf("%d\n", ways);
    }
    
    return 0;
}